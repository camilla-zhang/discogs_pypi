# discogs_pypi 

![](https://github.com/camilla-zhang/discogs_pypi/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/camilla-zhang/discogs_pypi/branch/main/graph/badge.svg)](https://codecov.io/gh/camilla-zhang/discogs_pypi) ![Release](https://github.com/camilla-zhang/discogs_pypi/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/discogs_pypi/badge/?version=latest)](https://discogs_pypi.readthedocs.io/en/latest/?badge=latest)

This package contains several functions related to collecting data related to music releases from the Discogs website

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ discogs_pypi
```

## Github Link

https://github.com/camilla-zhang/discogs_py

## Features

### 1. User Authentication

With this package, the user should already have an account with Discogs. There is typically a strenuous 5-step process to obtain data, where the user must frequently enter in and copy-paste several different credentials. Using the functions provided however, they will be able to easily obtain release information without having to interact with the Discogs website at all and only need a username and password (given that they have never created developer applications on the website before).

### 2. Extract Data
We obtain two datasets:
- Artist Releases: The user can enter in one or more numeric artist IDs (each ID can be found on the top-right corner of an artist's Discogs URL), and receive a list of releases for the selected artists as well as basic information on each release
- User Wantlist: The user can get data that displays a list of releases in their wantlist, with additional data for each release (i.e. genre, artists affiliated, etc.)
- Artist Releases and User Affiliation: A dataset of the original artist releases with an additional variable indicating whether a specified user has that release in their own wantlist

### 3. Summary Statistics
1. A table containing basic info for each artist based on their release history (i.e. years active, average collectors per release, etc)
2. A data visualization showing the average number of wantlisters and collectors for each release of each selected artist.

## Dependencies

- python = ^3.8
- oauth2 = ^1.9.0.post1
- requests = ^2.28.1
- selenium = ^4.7.2
- numpy = ^1.23.4
- pandas = ^1.5.1
- matplotlib = ^3.6.2

## Documentation

The official documentation is hosted on Read the Docs: https://discogs_pypi.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/camilla-zhang/discogs_pypi/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
