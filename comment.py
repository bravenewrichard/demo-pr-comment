import os
import re
from github import Github


GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
GITHUB_REPO = 'bravenewrichard/demo-pr-comment'

# First create a Github instance:
# using an access token
g = Github(GITHUB_TOKEN)

# parse log file for succinct results
parse_exec_tests = "EXECUTE TEST(S)"
parse_device = "device"
parse_flank = "flank"
parse_matrix_res = "MatrixResultsReport"
parse_task_finished = "=== Task Finished ==="

with open("log.txt") as file:
   data = file.read()
   a = data.split(parse_exec_tests)

   # test results
   results = a[1]
   device = results.split(parse_device)[1]
   flank = device.split(parse_flank)[0]
   flank = flank.replace(":", "")
   poll_matrices = results.split(parse_matrix_res)[1]
   poll_matrices = poll_matrices.split(parse_task_finished)[0]

   comment = "{0}\n{1}\n{2}\n{3}\n{4}".format('**DEVICES**', 'X86', flank, '**TEST REPORT**', poll_matrices)

clean = re.compile(r'\[task.*\]')
results = re.sub(clean, '', comment)

repo = g.get_repo(GITHUB_REPO)
pr = repo.get_pull(7)
pr.create_issue_comment(results)
