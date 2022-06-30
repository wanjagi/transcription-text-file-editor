from tkinter import *
from tkinter import filedialog
import re

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
print (root.filename)

def delete_strings(text):
    text = re.sub("uh", "", text)
    text = re.sub("Uh", "", text)
    text = re.sub("um", "", text)
    text = re.sub("Um", "", text)
    text = re.sub("mm-hmm", "", text)
    text = re.sub("Mm-hmm", "", text)
    text = re.sub("uh-huh", "", text)
    text = re.sub("you know", "", text)
    text = re.sub("Speaker 0", "", text)
    text = re.sub("Speaker 1", "", text)
    text = re.sub("Speaker 2", "", text)
    text = re.sub("    \d\d:\d\d:\d\d    ", "", text)
    return text

with open(root.filename, "r") as f:
    text = f.read()

text = delete_strings(text)

with open(root.filename, "w") as f:
    f.write(text)
    
root.mainloop()