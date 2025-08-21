import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Monitor(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file: {event.src_path}")

path = r"C:\Windows\Temp"
h = Monitor()
o = Observer()
o.schedule(h, path, recursive=False)
o.start()
print(f"Watching: {path}")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    o.stop()
o.join()
