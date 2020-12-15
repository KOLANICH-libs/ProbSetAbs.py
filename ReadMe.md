ProbSetAbs.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
================================
~~[wheel (GitLab)](https://gitlab.com/KOLANICH-libs/ProbSetAbs.py/-/jobs/artifacts/master/raw/dist/ProbSetAbs-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/ProbSetAbs.py/workflows/CI/master/ProbSetAbs-0.CI-py3-none-any.whl)
~~![GitLab Build Status](https://gitlab.com/KOLANICH-libs/ProbSetAbs.py/badges/master/pipeline.svg)~~
~~![GitLab Coverage](https://gitlab.com/KOLANICH-libs/ProbSetAbs.py/badges/master/coverage.svg)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/ProbSetAbs.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/ProbSetAbs.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/ProbSetAbs.py.svg)](https://libraries.io/github/KOLANICH-libs/ProbSetAbs.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

This is an abstraction layer around various implementations of probabilistic membership-testing (set-like) data structures, such as

* [Bloom filters](https://en.wikipedia.org/wiki/Bloom_filter)
* [cuckoo filters](https://en.wikipedia.org/wiki/Cuckoo_filter)
* [xor filters](https://lemire.me/blog/2019/12/19/xor-filters-faster-and-smaller-than-bloom-filters/)

Backends
--------

* [pyprobables](https://github.com/barrust/pyprobables)
* https://github.com/huydhn/cuckoo-filter
* ~~[https://github.com/glitzflitz/pyxorfilter](pyxorfilter)~~
* https://github.com/michael-the1/python-cuckoo
* https://github.com/remram44/python-bloom-filter
