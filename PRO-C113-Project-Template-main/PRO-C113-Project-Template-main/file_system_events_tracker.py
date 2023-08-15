import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Shaurya Gandhi/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
  def on_created(self, event): 
    print(f"Hey, {event.src_path} has been created!")



    #1_on_created

    #2_on_deleted
    def on_deleted(self, event):
       print(f"Hey, {event.src_path} has been deleted!")
  
    #3_on_modified
    def on_modified(self, event):
       print(f"Hey, {event.src_path} has been modified!")
    #4_on_moved
    def on_moved(self, event):
       print(f"Hey, {event.src_path} has been moved!")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try: 
    while True:
       time.sleep(2)
       print("running...")
except KeyboardInterrupt:
   print("stopped")
   observer.stop()
   
   






