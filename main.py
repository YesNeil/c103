import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "C:/Users/User/Desktop/c103"
to_dir = "C:/Users/User/Desktop/Downloaded_Files"
#Event Handler class

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(event)
        
#Initialize Event Handler class
event_handler = FileMovementHandler()

#Initialize Observer
observer = Observer()

#Schedule the observer
observer.schedule(event_handler,from_dir,recursive = True)

#Start the Observer
observer.start()

while True:
    time.sleep(2)
    print("running")



