from pathlib import Path

import numpy as np

from emanjson2imodxf import emanjson2imodxf

TEST_DIRECTORY = Path(__file__).parent
EMAN_JSON_FILE = TEST_DIRECTORY / 'example.json'
IMOD_XF_FILE = TEST_DIRECTORY / 'example.xf'
IMOD_TLT_FILE = TEST_DIRECTORY / 'example.tlt'


def test_emanjson2imodxf():
    """Check that output matches expected xf and tlt files.
    """
    xf, tilt_angles = emanjson2imodxf(EMAN_JSON_FILE)

    expected_xf = np.loadtxt(IMOD_XF_FILE)
    np.testing.assert_allclose(xf, expected_xf, atol=1e-3)

    expected_tlt = np.loadtxt(IMOD_TLT_FILE)
    np.testing.assert_allclose(tilt_angles, expected_tlt, atol=1e-2)