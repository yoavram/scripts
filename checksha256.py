import hashlib as hl
import click

@click.command()
@click.argument('filename', type=click.Path())
@click.option('--hash')
def checksum(filename, hash):
	h = hl.sha256()
	with open(filename, 'rb') as f:
        h.update(f.read())
    digest = h.hexdigest()
	return digest == hash

if __name__ == '__main__':
	checksum