from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def add_test_case():
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


# ttk.Label(window, text='Input:').grid(row=2, column=0, padx=5, sticky='sw')
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


