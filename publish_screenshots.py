from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep


class NewPngHandler(FileSystemEventHandler):
	def on_any_event(self, event):
		if event.is_directory: return
		if not event.event_type == 'created': return
		if not event.src_path.endswith('.png'): return
		print(event.src_path)


if __name__ == '__main__':
	path = '/Users/yoavram/Documents'
	event_handler = NewPngHandler()
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try:
		while True:
			sleep(1)	
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
