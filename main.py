from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
file_path = "" #file path will be empty for files that are unsaved(new)

# set file locstion in the computer
def set_file_path(path):
    global file_path
    file_path = path

# create a window
compiler = Tk()
compiler.title("!VSCode")

# define functions that we are going to use for the menu bar
# run function to execute our code
def run():
    global file_path

    if file_path == "":
        # if the file is new and not saved, save it to a temporary file
        path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
        with open(path, 'w') as file:
            code = editor.get('1.0', END)
            file.write(code)
            set_file_path(path)
    else:
        path = file_path

    # run the code using the saved or temporary file
    command = f'python {path}'
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
    code_terminal.insert('1.0', result.stdout)
    code_terminal.insert('1.0', result.stderr)


#save as function which uses the asksaveasfilename method to open a pop up to save your file in your computer
def save_as():
    # if not saved previously (in case of  a new file)
    if file_path == "":
        path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    else:
        #if it is already saved before fetch the whole code and save it
        #used as a save command
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


# function to browse and open a file from your computer 
def open_file():
    path = askopenfilename(filetypes=[("Python Files", "*.py")])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


#function to open a blank file
def new_file():
    editor.delete('1.0', END)
    editor.insert('1.0')


#create a menu bar
menu_bar = Menu(compiler)

# create a run bar inside the menu bar 
run_bar = Menu(menu_bar, tearoff=0) 
run_bar.add_command(label="Run", command = run)
menu_bar.add_cascade(label="Run", menu = run_bar)

#vreate a file bar inside the menu bar
file_bar = Menu(menu_bar, tearoff=0) 
file_bar.add_command(label="Open", command = open_file)#opens files using open function
file_bar.add_command(label="New file", command = new_file)#creates a new file using new_file function
file_bar.add_command(label="Save", command = save_as)#saves a pre existing file using save as function
file_bar.add_command(label="Save As", command = save_as)#saves a new file using save as function
file_bar.add_command(label="Exit", command = exit)#exits the window
menu_bar.add_cascade(label="File", menu = file_bar)


compiler.config(menu=menu_bar)

# create the section where we write the code
editor = Text(background='#D4D4D4', fg='blue')
editor.pack()

# create the terminal section inside our window
code_terminal = Text(height = 10, background='black', fg='white')
code_terminal.pack()

# runs our window
compiler.mainloop()

