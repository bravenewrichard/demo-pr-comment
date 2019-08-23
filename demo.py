import os
from github import Github

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
# First create a Github instance:
# or using an access token
g = Github(GITHUB_TOKEN)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)
