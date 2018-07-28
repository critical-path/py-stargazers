## py-stargazers v1.0.0

py-stargazers is a util that retrieves a list of stargazers for a given GitHub user and repo.


## Dependencies

py-stargazers requires Python as well as the pip, click, requests, pylint, pytest-cov, and responses packages.


## Installing py-stargazers with test cases and testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command and the --editable option.

```
sudo pip3 install --editable .[test] .
```


## Installing py-stargazers without test cases or testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command.

```
sudo pip3 install .
```


## Using py-stargazers with long options

To retrieve a list of stargazers for all repos associated with a given user, run stargazers with the --user option.

```
stargazers --user <user>
```

To retrieve a list of stargazers associated with a given user and a given repo, run stargazers with the --user and --repo options.

```
stargazers --user <user> --repo <repo>
```

To write the retrieved list of stargazers to disk, run stargazers with the --write option.

```
stargazers --user <user> --write
stargazers --user <user> --repo <repo> --write
```


## Using py-stargazers with short options

To retrieve a list of stargazers for all repos associated with a given user, run stargazers with the -u option.

```
stargazers -u <user>
```

To retrieve a list of stargazers associated with a given user and a given repo, run stargazers with the -u and -r options.

```
stargazers -u <user> -r <repo>
```

To write the retrieved list of stargazers to disk, run stargazers with the -w option.

```
stargazers -u <user> -w
stargazers -u <user> -r <repo> -w
```


## Testing py-stargazers after installation

1. Run pylint.

```
pylint stargazers
```

2. Change to the tests directory.

```
cd ./tests
```

3. Run pytest with the -v, --cov, and, --cov-report options.

```
pytest -v --cov=stargazers --cov-report=term-missing
```


## Note

py-stargazers makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.
