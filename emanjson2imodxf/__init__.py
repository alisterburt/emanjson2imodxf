try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
__author__ = "Alister Burt"
__email__ = "alisterburt@gmail.com"

from .emanjson2imodxf import emanjson2imodxf
