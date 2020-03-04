from github import Github, Issue, GithubObject
import datetime
import os

GITHUB_USER = os.environ['githubUser']
GITHUB_PW = os.environ['githubPw']

REPO_OWNER = 'FelixWieland'
REPO_NAME = 'simbution'

ghb = Github(GITHUB_USER, GITHUB_PW)


def handle_github_issue():
    try:
        make_simbution_github_issue()
        return (200, "Issue wurde erstellt")
    except Exception as e:
        return (500, e)


def make_simbution_github_issue():
    title = datetime.datetime.now().isoformat() + " - simulated contribution"
    body = "This is a simulated contribution to keep the contribution graph green."
    make_github_issue(title, body, labels=['simbution'])


def make_github_issue(title, body=GithubObject.NotSet, assignee=GithubObject.NotSet, milestone=GithubObject.NotSet, labels=GithubObject.NotSet):
    repo = get_repo(REPO_OWNER, REPO_NAME)
    issue = repo.create_issue(title, body, assignee, milestone, labels)
    close_issue(issue)


def get_repo(owner, name):
    return ghb.get_repo(REPO_OWNER + "/" + REPO_NAME)


def close_issue(issue):
    issue.edit(state='closed')
