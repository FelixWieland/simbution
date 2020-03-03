import json, os, requests

GITHUB_USER = os.environ['githubUser']
GITHUB_PW = os.environ['githubPw']

# The repository to add this issue to
REPO_OWNER = 'FelixWieland'
REPO_NAME = 'simbution'

def make_github_issue(title, body=None, assignee=None, milestone=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (GITHUB_USER, GITHUB_PW)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'assignee': assignee,
             'milestone': milestone,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        return 'Successfully created Issue'
    else:
        return 'Could not create Issue'

def simbution(event, context):

    resp = make_github_issue('Issue Title', 'Body text', 'assigned_user', None, ['bug'])

    response = {
        "statusCode": 200,
        "body": resp
    }

    return response