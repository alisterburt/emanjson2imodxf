# emanjson2imodxf

[![License](https://img.shields.io/pypi/l/emanjson2imodxf.svg?color=green)](https://github.com/alisterburt/emanjson2imodxf/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/emanjson2imodxf.svg?color=green)](https://pypi.org/project/emanjson2imodxf)
[![Python Version](https://img.shields.io/pypi/pyversions/emanjson2imodxf.svg?color=green)](https://python.org)
[![tests](https://github.com/alisterburt/emanjson2imodxf/workflows/tests/badge.svg)](https://github.com/alisterburt/emanjson2imodxf/actions)
[![codecov](https://codecov.io/gh/alisterburt/emanjson2imodxf/branch/master/graph/badge.svg)](https://codecov.io/gh/alisterburt/emanjson2imodxf)

Convert tilt-series alignments from EMAN2 json files to IMOD format xf files.

```sh
pip install emanjson2imodxf
```

```sh
Usage: emanjson2imodxf [OPTIONS]

  Convert an EMAN2 json file into an IMOD xf file.

Options:
  -i, --input PATH            EMAN2 json file  [required]
  -o, --output-basename PATH  basename for IMOD .xf and .tlt files  [required]
  --help                      Show this message and exit.

```

## Changelog
- v0.0.1 produce .xf file
- v0.0.2 produce .xf and corresponding .tlt file, API change
- v0.0.3 fix a bug in the output .tlt file (thanks @alexjnoble)
- v0.0.4 include tilt azimuth (untested, based on a suggestion from @alexjnoble)
