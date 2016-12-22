brew update
brew install reattach-to-user-namespace
brew upgrade reattach-to-user-namespace
echo "set -g default-command \"reattach-to-user-namespace -l ${SHELL}\"" >> ~/.tmux.conf