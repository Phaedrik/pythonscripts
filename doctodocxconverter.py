from glob import glob
import re
import os
import sys
import win32com.client as win32
from win32com.client import constants
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import time
import thread
import pythoncom


path = sys.argv[1]
# Create list of paths to .doc files
time.sleep(4)
pythoncom.CoInitialize()
path1 = 'C:\\Users\\jw185257\\Desktop\\Disaster Recovery\\' + path + '\\*.doc'
paths = glob(path1)
mouse = Controller()

def my_mouse():
    time.sleep(2)
    mouse.position = (953, 364)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)

    time.sleep(2)
    mouse.position = (991, 413)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    thread.exit()

def save_as_docx(path):
    # Opening MS Word
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path)
    doc.Activate()

    # Rename path with .docx
    new_file_abs = os.path.abspath(path)

    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    # Save and Close
    #If the documents require a sensitivity tag, we spawn a thread to automate the clicking of the tags to move forward
    #saving the document
    thread.start_new_thread(my_mouse, ( ))
    time.sleep(2)
    word.ActiveDocument.SaveAs(new_file_abs, FileFormat=constants.wdFormatXMLDocument)

    time.sleep(1)
    doc.Close(False)


for path in paths:
    print "New Path: "+ path
    save_as_docx(path)








