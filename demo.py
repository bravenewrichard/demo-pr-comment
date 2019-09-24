import os
import re
from github import Github


GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

# First create a Github instance:
# using an access token
g = Github(GITHUB_TOKEN)


parse_string = "EXECUTE TEST(S)"
with open("log.txt") as file:
   data = file.read()
   a = data.split(parse_string)

   # test results
   results = a[1]
   device = results.split('device')[1]
   flank = device.split('flank')[0]
   poll_matrices = results.split('MatrixResultsReport')[1]
   poll_matrices = poll_matrices.split("=== Task Finished ===")[0]

   comment = "{0}\n{1}\n{2}\n{3}\n{4}".format('**DEVICES**', 'X86', flank, '**TEST REPORT**', poll_matrices)

clean = re.compile(r'\[task.*\]')
results = re.sub(clean, '', comment)

repo = g.get_repo('bravenewrichard/demo-pr-comment')
pr = repo.get_pull(1)
pr.create_issue_comment(results)
