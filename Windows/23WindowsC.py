import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Monitor(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")
    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")
    def on_moved(self, event):
        print(f"Moved: {event.src_path} → {event.dest_path}")

def watch(path):
    h = Monitor()
    o = Observer()
    o.schedule(h, path, recursive=True)
    o.start()
    print(f"Watching: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        o.stop()
    o.join()

if __name__ == "__main__":
    p = input("Enter directory path: ").strip()
    watch(p)
