# pexels

![PyPI - package version](https://img.shields.io/pypi/v/pexels?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/pexels?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/pexels?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/pexels?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/Zselter07/py_pexels?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/Zselter07/py_pexels?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/Zselter07/py_pexels?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/Zselter07/py_pexels?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/Zselter07/py_pexels?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/Zselter07/py_pexels?label=repo%20license&style=flat-square)

## Description

Get pexels video ids with selenium firefox

## Install

~~~~bash
pip install pexels
# or
pip3 install pexels
~~~~

## Usage

~~~~python
from pexels import Pexels
from pexels.models.enums import Orientation, Size

pexels = Pexels()
video_ids = pexels.get_video_ids(
    'dogs',
    videos_orientation=Orientation.HORIZONTAL,  # Optional
    videos_size=Size.FOUR_K                     # Optional
)
~~~~

## Dependencies

[randomua](https://pypi.org/project/randomua), [selenium-firefox](https://pypi.org/project/selenium-firefox)