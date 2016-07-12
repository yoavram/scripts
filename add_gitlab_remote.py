import re
import subprocess
import sys

import git

pattern = "git@([-_\w\.]+):([-_\w]+)\/([-_\w]+).git"
template = "git config --add remote.origin.url git@{host}:{username}/{repo}.git"
new_host = "gitlab.com"

if __name__ == "__main__":
    repo = git.Repo()
    origin = repo.remote("origin")
    url = next(origin.urls)
    m = re.match(pattern, url)
    if not m:
        print("Regexp failed on", url)
        sys.exit(1)
    host, username, repo = m.groups()
    command = template.format(host=new_host, username=username, repo=repo)
    retcode = subprocess.call(command.split())
    if retcode:
        print("git config failed with code", retcode)
        sys.exit(retcode)
    sys.exit(subprocess.call("git remote -v".split()))
