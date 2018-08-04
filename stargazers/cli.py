"""The command-line interface for py-stargazers."""


from json import dumps

from click import (
    command,
    echo,
    option
)

from stargazers.lib import (
    get_repos,
    get_stargazers_for_one_repo,
    get_stargazers_for_all_repos,
    write_results
)


API = "https://api.github.com"


@command()
@option("--user", "-u", required=True, type=str, help="User of interest")
@option("--repo", "-r", type=str, help="Repo of interest")
@option("--write", "-w", is_flag=True, help="Write results to disk")
def get_stargazers(user=None, repo=None, write=False):
    """Util that retrieves a list of stargazers for a given GitHub user and repo."""

    if (user is not None) and (repo is not None):
        stargazers = get_stargazers_for_one_repo(API, user, repo)

    if (user is not None) and (repo is None):
        repos = get_repos(API, user)
        stargazers = get_stargazers_for_all_repos(API, user, repos)

    stargazers = dumps(stargazers, indent=2)

    if write:
        write_results(user=user, repo=repo, stargazers=stargazers)

    echo(stargazers)


if __name__ == "__main__":
    get_stargazers()
