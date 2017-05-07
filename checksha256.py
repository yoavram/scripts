from hashlib import sha256

import click

@click.command()
@click.argument('filename', type=click.Path())
@click.argument('hash', type=str)
def checksum(filename, hash):
	h = sha256()
	with open(filename, 'rb') as f:
		h.update(f.read())
	digest = h.hexdigest()
	if digest == hash:
		click.secho("OK", fg='green')
	else:
		click.secho("FAILED\7", fg='black', bg='red')

if __name__ == '__main__':
	checksum()
