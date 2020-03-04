import json, os, requests, datetime
from github import Github, Issue, GithubObject

GITHUB_USER = os.environ['githubUser']
GITHUB_PW = os.environ['githubPw']

REPO_OWNER = 'FelixWieland'
REPO_NAME = 'simbution'

ghb = Github(GITHUB_USER, GITHUB_PW)

def make_github_issue(title, body=GithubObject.NotSet, assignee=GithubObject.NotSet, milestone=GithubObject.NotSet, labels=GithubObject.NotSet):
    try:
        repo = ghb.get_repo(REPO_OWNER + "/" + REPO_NAME)
        issue = repo.create_issue(title, body, assignee, milestone, labels)
        issue.edit(state='closed')
        return "Created new issue, and closed it afterwards"
    except:
        return "Failed to create new issue"

def simbution(event, context):
    title = datetime.datetime.now().isoformat() + " - simulated contribution"
    body = "This is a simulated contribution to keep the contribution graph green."
    resp = make_github_issue(title, body, labels=['simbution'])

    response = {
        "statusCode": 200,
        "body": resp
    }

    return response