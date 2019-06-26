if [ "$TERM" != "screen" ]
then
    if type tmux >/dev/null 2>&1
    then
        tmux -CC attach || tmux -CC new;
    fi
fi

