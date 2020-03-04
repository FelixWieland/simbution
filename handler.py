from src.githubhandlers import handle_github_issue


def simbution(event, context):
    statusCode, body = handle_github_issue()
    return {
        "statusCode": statusCode,
        "body": body
    }
