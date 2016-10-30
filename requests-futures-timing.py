from builtins import range
import time
from contextlib import contextmanager
from concurrent.futures import as_completed

import click
from requests import Session
from requests_futures.sessions import FuturesSession # v0.9.7


@contextmanager
def tictoc():
	tic = time.time()
	yield tic
	toc = time.time()
	click.echo("Elapsed time {:.2f} seconds".format(toc - tic))


@click.command()
@click.argument('url', default='http://httpbin.org/delay/6', type=str)
@click.option('--n', default=10, help="number of requests")
def main(url, n):
	"""Compare the time it takes requests and requests-futures to get n responses from a given URL. By default n=10 for ten responses and the URL is httpbin/delay/6 for a total time of 60 seconds for requests, which works in sync, and 6 seconds for requests-futures, which works in async. Before you run, install dependencies with `pip install requests requests-futures click`. Compatible with Python 3.
	"""
	click.echo("# requests:")
	with tictoc(), Session() as sess: 
		responses = [sess.get(url) for i in range(n)]
	for r in responses:
		assert r.ok

	click.echo("# requests_futures:")
	with tictoc(), FuturesSession(max_workers=n) as sess: 
		futures = [sess.get(url) for i in range(n)]
	for f in as_completed(futures):
		assert f.result().ok


if __name__ == '__main__':
	main()