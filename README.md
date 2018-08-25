[![Build Status](https://travis-ci.com/critical-path/py-stargazers.svg?branch=master)](https://travis-ci.com/critical-path/py-stargazers) [![Coverage Status](https://coveralls.io/repos/github/critical-path/py-stargazers/badge.svg)](https://coveralls.io/github/critical-path/py-stargazers)

## py-stargazers v1.0.0

py-stargazers is a util that retrieves a list of stargazers for a given GitHub user and repo.


## Dependencies

py-stargazers requires Python and the pip package.  It also requires the following packages for usage and testing.

__Usage__:
- click
- requests

__Testing__:
- coveralls
- pylint
- pytest
- pytest-cov
- radon
- responses


## Installing py-stargazers with test cases and testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command and the `--editable` option.

```
sudo pip install --editable .[test]
```


## Installing py-stargazers without test cases or testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command.

```
sudo pip install .
```


## Using py-stargazers with long options

To retrieve a list of stargazers for all repos associated with a given user, run `stargazers` with the `--user` option.

```
stargazers --user <user>
```

To retrieve a list of stargazers associated with a given user and a given repo, run `stargazers` with the `--user` and `--repo` options.

```
stargazers --user <user> --repo <repo>
```

To write the retrieved list of stargazers to disk, run `stargazers` with the `--write` option.

```
stargazers --user <user> --write
stargazers --user <user> --repo <repo> --write
```


## Using py-stargazers with short options

To retrieve a list of stargazers for all repos associated with a given user, run `stargazers` with the `-u` option.

```
stargazers -u <user>
```

To retrieve a list of stargazers associated with a given user and a given repo, run `stargazers` with the `-u` and `-r` options.

```
stargazers -u <user> -r <repo>
```

To write the retrieved list of stargazers to disk, run `stargazers` with the `-w` option.

```
stargazers -u <user> -w
stargazers -u <user> -r <repo> -w
```


## Testing py-stargazers after installation

1. Run `radon` with the `mi` command and the `--show` option.

```
radon mi --show stargazers
```

2. Run `pylint`.

```
pylint stargazers
```

3. Run `pytest` with the `-vv`, `--cov`, and `--cov-report` options.

```
pytest -vv --cov --cov-report=term-missing
```


## Note

py-stargazers makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.
