from __future__ import annotations

import json
from typing import TYPE_CHECKING, Tuple

import numpy as np

if TYPE_CHECKING:
    from os import PathLike


def read_tlt_params(json_file: PathLike) -> Tuple[np.ndarray]:
    """Read an EMAN2 json file and extract alignment parameters.

    In EMAN2 tilt-series alignment translations are applied first, followed by
    rotations.

    Parameters
    ----------
    json_file : PathLike
        An EMAN2 json file containing alignment parameters from a tilt-series
        alignment experiment.

    Returns
    -------
    dxy, theta, projection_angles : tuple[np.ndarray]
        shifts and rotation angles from the json file.
        dxy is an (n, 2, 1) array of dx, dy in pixels.
        theta is an (n, ) array of rotation angles in degrees.
        projection_angles is an (n, ) array of tilt angles for reconstruction.
    """
    with open(json_file) as f:
        data = json.load(f)
    tlt_params = np.array(data['tlt_params'])

    # extract useful information
    # reshape shifts to (n, 2, 1) array of column vectors
    dx = tlt_params[:, 0]
    dy = tlt_params[:, 1]
    dxy = np.stack((dx, dy), axis=-1).reshape((-1, 2, 1))
    theta = np.deg2rad(tlt_params[:, 2])

    projection_angles = tlt_params[:, 3]

    return dxy, theta, projection_angles


def angle2rotm(theta: np.ndarray) -> np.ndarray:
    """Convert angles into a stack of 2D rotation matrices.

    R(theta) = [[cos(theta), -sin(theta)],
                [sin(theta), cos(theta)]])

    Parameters
    ----------
    theta : np.ndarray
        An (n, ) array of angles in radians.

    Returns
    -------
    rotation_matrices : np.ndarray
        An (n, 2, 2) stack of rotation matrices.
    """
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    r = np.array([[cos_theta, -sin_theta],
                  [sin_theta, cos_theta]])
    return r.swapaxes(0, 2)

