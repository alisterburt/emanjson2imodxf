from os import PathLike

import click
import numpy as np

from .data_munging import read_tlt_params, angle2rotm


def emanjson2imodxf(input_json_file: PathLike):
    # Get useful info from EMAN json file
    # shifts in px, theta in radians, y tilt in degrees
    dxy_eman, theta, tilt_angles = read_tlt_params(json_file=input_json_file)
    rotation_matrices = angle2rotm(theta)

    # EMAN translates then rotates, IMOD rotates then translates
    # R(x+dx, y+dy) = R(x, y) + R(dx, dy)
    # IMOD (dx, dy) is the rotated EMAN (dx, dy)
    dxy_imod = rotation_matrices @ dxy_eman

    # get lines for IMOD xf file
    A11 = rotation_matrices[:, 0, 0]
    A12 = rotation_matrices[:, 0, 1]
    A21 = rotation_matrices[:, 1, 0]
    A22 = rotation_matrices[:, 1, 1]
    dx_imod = dxy_imod[:, 0].squeeze()
    dy_imod = dxy_imod[:, 1].squeeze()

    xf = np.stack((A11, A12, A21, A22, dx_imod, dy_imod), axis=-1)
    return xf, tilt_angles


@click.command()
@click.option(
    '-i', '--input', 'input_json_file',
    help='EMAN2 json file',
    type=click.Path(exists=True),
    required=True,
)
@click.option(
    '-o', '--output-basename', 'output_basename',
    help='basename for IMOD .xf and .tlt files',
    type=click.Path(),
    required=True,
)
def cli(input_json_file, output_basename):
    """Convert an EMAN2 json file into an IMOD xf file.
    """
    output_xf_file = f'{output_basename}.xf'
    output_tlt_file = f'{output_basename}.tlt'

    click.echo(f'Input file: {input_json_file}')
    click.echo(f'Output files: {output_xf_file}, {output_tlt_file}')

    xf, tilt_angles = emanjson2imodxf(input_json_file)
    np.savetxt(output_xf_file, xf, fmt='%.6f', delimiter=' ')
    np.savetxt(output_tlt_file, tilt_angles, fmt='%.2f')
    click.echo(f'Success!')
