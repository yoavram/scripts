if [ "$TERM" != "screen" ]
then
    if type tmux >/dev/null 2>&1
    then
        tmux att || tmux \
            new -s Yoav -n jupyter "cd Work && jupyter notebook" \; \
            neww -n ipython  "source activate scipy && ipython" \; \
            neww
    fi
fi