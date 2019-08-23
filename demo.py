import os
from github import Github


GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

# First create a Github instance:
# using an access token
g = Github(GITHUB_TOKEN)

repo = g.get_repo('bravenewrichard/demo-pr-comment')
pr = repo.get_pull(1)
pr.create_issue_comment('test')
