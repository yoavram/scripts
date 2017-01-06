import os
import subprocess
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import click
from click_spinner import spinner


class PandocHandler(FileSystemEventHandler):
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename

    def on_modified(self, event):
        if event.src_path.endswith(self.input_filename):
            args = [
                'pandoc', 
                self.input_filename, 
                '-o', self.output_filename, 
                '--latex-engine', 'xelatex'                
            ]
            # https://docs.python.org/3/library/subprocess.html
            subprocess.run(args)
            args = [
                'open',
                self.output_filename
            ]
            subprocess.run(args)

@click.command()
@click.argument('filename', type=click.Path(exists=True, readable=True))
def main(filename):
    if not filename.endswith('.md'):
        raise click.BadParameter("Please provide a Markdown file ending with .md")
    input_filename = filename
    output_filename = filename.replace('md', 'pdf')
    event_handler = PandocHandler(input_filename, output_filename)
    observer = Observer()
    observer.schedule(event_handler, path='.')
    observer.start()

    try:
        with spinner():        
            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



if __name__ == '__main__':
    main()
