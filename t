if [ "$TERM" != "screen" ]
then
    if type tmux >/dev/null 2>&1
    then
        tmux -CC attach || tmux -CC \
            new -s Yoav -n jupyter "cd Work && jupyter lab --no-browser" \; \
            neww -n ipython  "source activate scipy && ipython" \; \
            #neww -n julia  "julia" \; \
            neww -n term
    fi
fi

