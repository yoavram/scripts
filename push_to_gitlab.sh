#!/bin/bash
# http://stackoverflow.com/questions/14290113/git-pushing-code-to-two-remotes
REPO_PATH=$(git rev-parse --show-toplevel)
REPO_NAME=$(basename $REPO_PATH)
git remote set-url --add --push origin git@github.com:yoavram/$REPO_NAME.git
git remote set-url --add --push origin git@gitlab.com:yoavram/$REPO_NAME.git