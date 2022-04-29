from collections import Counter

import requests


def request_to_github_api(url: str):
    r = requests.get(f"https://api.github.com/{url}")

    if r.status_code != 200:
        raise Exception(r.json())

    return r.json()


class GitHubRepo:
    def __init__(self, name: str, description: str, languages):
        self.name = name
        self.description = description
        self.languages = languages


class GitHubUser:
    def __init__(self, username: str):
        self.username = username

        info = request_to_github_api(f"users/{self.username}")
        self.number_of_repos = info["public_repos"]
        self.number_of_followers = info["followers"]

        self.repos = []
        languages = {}

        for repo in request_to_github_api(f"users/{self.username}/repos"):
            repo_name = repo["name"]
            repo_description = repo["description"]
            repo_languages = request_to_github_api(f"repos/{self.username}/{repo_name}/languages")

            for language in repo_languages.keys():
                languages[language] = languages.setdefault(language, 0) + 1

            self.repos.append(GitHubRepo(repo_name, repo_description, repo_languages))

        self.languages = Counter(languages)
