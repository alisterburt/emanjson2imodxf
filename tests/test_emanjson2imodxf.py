from pathlib import Path

import numpy as np

from emanjson2imodxf import emanjson2imodxf

TEST_DIRECTORY = Path(__file__).parent
EMAN_JSON_FILE = TEST_DIRECTORY / 'example.json'
IMOD_XF_FILE = TEST_DIRECTORY / 'example.xf'


def test_emanjson2imodxf():
    """Check that output of emanjson2imodxf matches the expected xf file.
    """
    xf = emanjson2imodxf(EMAN_JSON_FILE)
    expected = np.loadtxt(IMOD_XF_FILE)
    np.testing.assert_allclose(xf, expected, atol=1e-3)
