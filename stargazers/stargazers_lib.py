"""The library of functions used by py-stargazers."""


from requests import get


def get_repos(api, user):
    """Get list of all repos for a given user.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    The parameters help to form the API endpoint.

    Returns
    -------
    repos : list
        The repos for the user of interest.
    """

    repos = []

    endpoint = "{}/users/{}/repos".format(api, user)
    response = get(endpoint)
    response_body = response.json()

    for element in response_body:
        repo = element["name"]
        repos.append(repo)

    return repos


def get_stargazers_for_one_repo(api, user, repo):
    """Get list of all stargazers for a given repo.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    repos : str
        The repo of interest.

    The parameters help to form the API endpoint.

    Returns
    -------
    stargazers : dict
        The stargazers for the repo of interest.
    """

    stargazers = {}

    endpoint = "{}/repos/{}/{}/stargazers".format(api, user, repo)
    response = get(endpoint)
    response_body = response.json()
    stargazers[repo] = response_body

    return stargazers


def get_stargazers_for_all_repos(api, user, repos):
    """Get list of all stargazers for a given list of repos.

    Parameters
    ----------
    api : str
        The API's fully-qualified domain name.

    user : str
        The user of interest.

    repos : list
        The repos of interest.

    The parameters help to form the API endpoint.

    Returns
    -------
    stargazers : dict
        The stargazers for the repos of interest.
    """

    stargazers = {}

    for repo in repos:
        endpoint = "{}/repos/{}/{}/stargazers".format(api, user, repo)
        response = get(endpoint)
        response_body = response.json()
        stargazers[repo] = response_body

    return stargazers


def write_results(user=None, repo=None, stargazers=None):
    """Write results to disk.

    Parameters
    ---------
    user : str
      The user of interest.

    repo : str, optional
      The repo of interest.

    stargazers : str in JSON format
      The stargazers associated with the user and repo.

    The parameters help to form the filename.

    Returns
    -------
    N/A
    """

    if user and repo:
        filename = "stargazers-{0}-{1}.json".format(user, repo)
    elif user and not repo:
        filename = "stargazers-{0}.json".format(user)

    with open(filename, "w") as output:
        output.write(stargazers)
