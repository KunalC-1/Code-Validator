from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import asksaveasfilename, askopenfilename

file_path = ""
def open_file(event=None):
    global file_path
    open_path = askopenfilename(filetypes=[("Text File", "*.txt")])
    if len(open_path) == 0:
        return
    file_path = open_path

def create_file(event=None):
    global file_path
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Text File", "*.txt")])
    if len(save_path) == 0:
        return
    file_path = save_path
    with open(save_path, "w") as file:
        pass

def add_test_case():
    global file_path
    if len(file_path) == 0:
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="Select/Create Test Case File")
        msg.pack()
        return
    with open(file_path, "a+") as file:
        data = "\nInput:\n" + input.get(1.0, END) + "Output:\n" + output.get(1.0, END)
        file.write(data)
    messagebox.showinfo(title='Test Case info', message='Test Case Added Successfully!')

def clear_test_case():
    input.delete(1.0, END)
    output.delete(1.0, END)

window = Tk()
window.title('Add Test Cases')
window.configure(background='#f7f7f7')
menu = Menu(window)
window.config(menu=menu)

style = ttk.Style()
style.configure('TFrame', background='#f7f7f7')
style.configure('TButton', background='#e1d8b9')
style.configure('TLabel', background='#f7f7f7', font=('Arial', 12))

file_menu = Menu(menu, tearoff=0)
# Adding Menu
menu.add_cascade(label="File", menu=file_menu)

window.bind("<Control-o>", open_file)
file_menu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)

window.bind("<Control-c>", create_file)
file_menu.add_command(label="Create", accelerator="Ctrl+C", command=create_file)



ttk.Label(window, text='Input:').pack()
input = ScrolledText(window, font=("haveltica 10"), wrap=None, height= 15, width= 70)
input.pack(fill=BOTH, expand=1)
input.focus()

ttk.Label(window, text='Output:').pack()
output = ScrolledText(window, font=("haveltica 10"), wrap=None, height= 15, width= 70)
output.pack(fill=BOTH, expand=1)
output.focus()

ttk.Button(window, text='Add Test Case',
            command=add_test_case).pack(side=LEFT)
ttk.Button(window, text='Clear Test Case',
                command=clear_test_case).pack(side= RIGHT)
window.mainloop()


