from subprocess import run, PIPE
from tempfile import mktemp
from os.path import exists
from os import remove
from warnings import warn

# pip install click
import click


# install poppler: brew install poppler
command_name = 'pdfdetach'


@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--password', prompt=True, hide_input=True)
def main(filename, password):
	list_cmd = [
		command_name, 
		'-list', 
		'-upw', password, 
		filename
	]
	res = run(list_cmd, stdout=PIPE)
	lines = res.stdout.decode('utf8').split('\n')
	num_attach = int(lines[0].split()[0])
	click.echo("{} attachments will be extracted".format(num_attach))
	attachments = [line.partition(' ')[-1] for line in lines[1:] if line]
	if len(attachments) != num_attach:		
		raise ValueError("Failed parsing {} -list".format(command_name))

	for i, attach in enumerate(attachments):
		click.echo("Extracting {}".format(attach))
		tmp_fname = mktemp(suffix=attach)
		save_cmd = [
			command_name, 
			'-save', str(i + 1), 
			'-o', tmp_fname, 
			'-upw', password, 
			filename
		]
		run(save_cmd)
		if exists(tmp_fname):
			run(['open', tmp_fname])			
			click.echo("Press 'return' to continue...")
			input()
			remove(tmp_fname)
		else:
			warn('Failed extracting {}'.format(attach))


if __name__ == '__main__':
	main()
