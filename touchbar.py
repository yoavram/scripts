# http://osxdaily.com/2017/01/11/manually-refresh-touch-bar-mac/
kill_controlstrip_cmd = 'killall ControlStrip'.split(' ')
kill_touchbar_cmd = 'sudo pkill "Touch Bar agent"'.split(' ')

import click
import subprocess

@click.command()
@click.option('--tb', default=False, is_flag=True, help='Refresh the touchbar')
@click.option('--cs', default=False, is_flag=True, help='Refresh the control strip')
def main(tb, cs):
	if cs:
		subprocess.call(kill_controlstrip_cmd)
	elif tb:
		subprocess.call(kill_touchbar_cmd)


if __name__ == '__main__':
	main()