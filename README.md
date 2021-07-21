# emanjson2imodxf

[![License](https://img.shields.io/pypi/l/emanjson2imodxf.svg?color=green)](https://github.com/alisterburt/emanjson2imodxf/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/emanjson2imodxf.svg?color=green)](https://pypi.org/project/emanjson2imodxf)
[![Python Version](https://img.shields.io/pypi/pyversions/emanjson2imodxf.svg?color=green)](https://python.org)
[![tests](https://github.com/alisterburt/emanjson2imodxf/workflows/tests/badge.svg)](https://github.com/alisterburt/emanjson2imodxf/actions)
[![codecov](https://codecov.io/gh/alisterburt/emanjson2imodxf/branch/master/graph/badge.svg)](https://codecov.io/gh/alisterburt/emanjson2imodxf)

Convert tilt-series alignments from EMAN2 to IMOD format

```sh
pip install emanjson2imodxf
```

```sh
Usage: emanjson2imodxf [OPTIONS]

  Convert an EMAN2 json file into an IMOD xf file.

Options:
  -i, --input PATH   EMAN2 json file  [required]
  -o, --output PATH  IMOD xf file (output)  [required]
  --help             Show this message and exit.
```