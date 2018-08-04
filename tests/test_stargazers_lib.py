from json import dumps

from os import (
    remove,
    stat
)

from stargazers.lib import (
    get_repos,
    get_stargazers_for_all_repos,
    get_stargazers_for_one_repo,
    write_results
)

from responses import (
    activate,
    add,
    GET
)

from constants import (
    API,
    FILENAME_USER,
    FILENAME_USER_REPO,
    STARGAZERS,
    REPO0,
    REPO1,
    REPOS,
    REPO0_AND_STARGAZERS,
    REPOS_AND_STARGAZERS,
    USER
)


@activate
def test_get_repos():
    endpoint = "{}/users/{}/repos".format(API, USER)

    add(
        method=GET,
        url=endpoint,
        body=dumps(REPOS),
        status=200
    )

    repos = get_repos(API, USER)

    assert repos == ["test-repo0", "test-repo1"]


@activate
def test_get_stargazers_for_one_repo():
    endpoint = "{}/repos/{}/{}/stargazers".format(API, USER, REPO0)

    add(
        method=GET,
        url=endpoint,
        body=dumps(STARGAZERS),
        status=200
    )

    stargazers = get_stargazers_for_one_repo(API, USER, REPO0)

    assert stargazers == REPO0_AND_STARGAZERS


@activate
def test_get_stargazers_for_all_repos():
    repos_endpoint = "{}/users/{}/repos".format(API, USER)

    add(
        method=GET,
        url=repos_endpoint,
        body=dumps(REPOS),
        status=200
    )

    stargazers_endpoint0 = "{}/repos/{}/{}/stargazers".format(API, USER, REPO0)

    add(
        method=GET,
        url=stargazers_endpoint0,
        body=dumps(STARGAZERS),
        status=200
    )

    stargazers_endpoint1 = "{}/repos/{}/{}/stargazers".format(API, USER, REPO1)

    add(
        method=GET,
        url=stargazers_endpoint1,
        body=dumps(STARGAZERS),
        status=200
    )

    repos = get_repos(API, USER)
    stargazers = get_stargazers_for_all_repos(API, USER, repos)

    assert stargazers == REPOS_AND_STARGAZERS


def test_write_results_user_repo():
    write_results(user=USER, repo=REPO0, stargazers=dumps(REPO0_AND_STARGAZERS))

    assert stat(FILENAME_USER_REPO)
    remove(FILENAME_USER_REPO)


def test_write_results_user_no_repo():
    write_results(user=USER, stargazers=dumps(REPOS_AND_STARGAZERS))

    assert stat(FILENAME_USER)
    remove(FILENAME_USER)
