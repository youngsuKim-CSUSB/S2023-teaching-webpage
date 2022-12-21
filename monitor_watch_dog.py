# https://stackoverflow.com/questions/32923451/how-to-run-an-function-when-anything-changes-in-a-dir-with-python-watchdog
# import sys
import subprocess
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

class Event(LoggingEventHandler):
    def dispatch(self, event):
        subprocess.run(["sphinx-build",".","_build"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = './'
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()