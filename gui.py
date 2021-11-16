from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.scrolledtext import ScrolledText
from tkinter.font import BOLD, Font
import subprocess
import sys
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re


"""
    Syntax Highlighting for Python Codes
    https://stackoverflow.com/questions/38594978/tkinter-syntax-highlighting-for-text-widget
""" 

cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#FFFFFF'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#FFFFFF'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#FFFFFF'}
cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#FFFFFF'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#FFFFFF'}




# Creating window instance
window = Tk()

# Setting title for window
window.title("Python IDE")
# window.geometry("500x500")

# Creating and configuring menu for display
menu = Menu(window)
window.config(menu=menu)


# Adding zoom in / zoom out
font =Font(family="Courier", size=12, weight="bold")

def zoom(size):
    font.configure(size=int(float(size)))

zoom_scale = ttk.Scale(window, orient='vertical', from_=1, to=30)
zoom_scale.config(command=zoom)

zoom_scale.pack(fill='y', side='right')

zoom_scale.set(12)

# Editor window 
editor = ScrolledText(window, font=font, wrap=None)
editor.pack(fill=BOTH, expand=1)
editor.focus()
ip.Percolator(editor).insertfilter(cdg)

file_path = ""
testcase_file_path = ""

# Opening existing file
def open_file(event=None):
    global code, file_path
    open_path = askopenfilename(filetypes=[("Python File", "*.py")])
    if len(open_path) == 0:
        return
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)

# Binding CTRL + O to open file
window.bind("<Control-o>", open_file)

# Saving current files content
def save_file(event=None):
    global code, file_path
    if file_path == '':
        # Asking for fileName
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        if len(save_path) == 0:
            return
        file_path =save_path
    else:
        save_path = file_path
    try:
        with open(save_path, "w") as file:
            code = editor.get(1.0, END)
            file.write(code) 
    except:
        return

# Binding CTRL + S for saving 
window.bind("<Control-s>", save_file)

# Save as Function 
def save_as(event=None):
    global code, file_path
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    if len(save_path) == 0:
        return
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 

# Binding CTRL + S for save as
window.bind("<Control-S>", save_as)

# Execute code in editor
def run(event=None):
    global code, file_path,testcase_file_path

    if file_path == "":
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="First Save File to Test")
        msg.pack()
        return
    if testcase_file_path == "":
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="First Choose Test Case File to Test")
        msg.pack()
        return

    save_file()
    # command to python code in file
    cmd = f"python3 testingCases.py"

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin = subprocess.PIPE,shell=True)
    inputStr = f"{testcase_file_path}\n{file_path}\n".encode()
    output, error =  process.communicate(input=inputStr)
    
    output_window.configure(state="normal")
    # Delete previous output
    output_window.delete(1.0, END)

    # Insert new output
    output_window.insert(1.0, output.decode())

    # Insert Error to output box
    output_window.insert(1.0, error)

    output_window.configure(state="disabled")

# Binding <F-5> to run
window.bind("<F5>", run)

# Close window
def close(event=None):
    window.destroy()

# Bind CTRL + Q to close    
window.bind("<Control-q>", close)

# Cut text 
def cut_text(event=None):
    editor.event_generate(("<<Cut>>"))

# Copy text
def copy_text(event=None):
    editor.event_generate(("<<Copy>>"))

# Paste text
def paste_text(event=None):
    editor.event_generate(("<<Paste>>"))
     
# Creating Menu
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
run_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
test_menu = Menu(menu, tearoff=0)

# Adding Menu
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Run", menu=run_menu)
menu.add_cascade(label ="View", menu=view_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
menu.add_cascade(label ="Test Case", menu=test_menu)

# Adding commands for File Menu
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=close)

# Adding commands in Edit Menu
edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Adding command in Run Menu
run_menu.add_command(label="Run", accelerator="F5", command=run)

# Hiding status bar
status_bar = BooleanVar()
status_bar.set(True)

def hide_statusbar():
    global status_bar
    if status_bar:
        status_bars_menu.pack_forget()
        status_bar = False 
    else :
        status_bars_menu.pack(side=BOTTOM)
        status_bar = True
        
# Adding check button in View Menu
view_menu.add_checkbutton(label = "Status Bar" , onvalue = True, offvalue = False,variable = status_bar , command = hide_statusbar)

# Lable for status bar
status_bars_menu = ttk.Label(window,text = f"KK Code Validator {testcase_file_path} {file_path} characters: 0 words: 0")
status_bars_menu.pack(side = BOTTOM)

# Display Character and word count
text_change = False
def change_word(event = None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ",""))
        testcase = testcase_file_path.split("/")[-1]
        filepath = file_path.split("/")[-1]
        status_bars_menu.config(text = f"KK Code Validator {testcase} {filepath} \t\t\t\t characters: {chararcter} words: {word}")
    editor.edit_modified(False)

editor.bind("<<Modified>>",change_word)

# Light Mode
def light():
    editor.config(bg="white",fg="black")
    output_window.config(bg="white", fg="green")

# Dark Mode
def dark():
    editor.config(fg="white", bg="grey")
    output_window.config(fg="green", bg="grey")

# Addind commands to Theme Menu
theme_menu.add_command(label="light", command=light)
theme_menu.add_command(label="dark", command=dark)

def choose_test_case():
    global testcase_file_path
    open_path = askopenfilename(filetypes=[("Text File", "*.txt")])
    if len(open_path) == 0:
        return
    testcase_file_path = open_path
    editor.edit_modified(True)

window.bind("<Control-t>", choose_test_case)

# Addind commands to Test Case Menu
test_menu.add_command(label="Choose", accelerator="Ctrl+T", command=choose_test_case)

# create output window to display output of written code
output_window = ScrolledText(window,font=font,foreground="green", height=16)
output_window.pack(fill=BOTH, expand=1)
output_window.configure(state="disabled")
window.mainloop()
