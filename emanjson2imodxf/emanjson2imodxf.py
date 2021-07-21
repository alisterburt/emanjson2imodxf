from os import PathLike

import click
import numpy as np

from .data_munging import read_tlt_params, angle2rotm


def emanjson2imodxf(input_json_file: PathLike):
    # Get useful info from EMAN json file
    # shifts in px, theta in radians
    dxy_eman, theta = read_tlt_params(json_file=input_json_file)
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
    return xf


@click.command()
@click.option(
    '--input', 'input_json_file',
    type=click.Path(exists=True),
    required=True,
    prompt=True,
)
@click.option(
    '--output', 'output_xf_file',
    type=click.Path(),
    required=False,
    prompt=True,
)
def cli(input_json_file, output_xf_file=None):
    click.echo(f'Input file: {input_json_file}')
    click.echo(f'Output file: {output_xf_file}')
    xf = eman2imod(input_json_file)
    np.savetxt(output_xf_file, xf, fmt='%.6f', delimiter=' ')
    click.echo(f'Success!')
