import tkinter
from tkinter import *
from tkinter import ttk,messagebox


# Functions 


class comingSoon:
    def __init__(self, mainWindow):
        text = Label(mainWindow, text="Coming soon......")
        text.place(relx=0.4, rely=0.5)


def press(val, entry):
    if val == "Enter":
        pass
    else:
        entry.insert('end', val)

class alegbra:

    def __init__(self, mainWindow):


        # instruction button
        self.questionMarkPath = PhotoImage(file = r"C:\Users\haoju\OneDrive\Desktop\CS361\Assignment5\questionMark.png" )
        self.questionMarkImage = self.questionMarkPath.subsample(10,10)
        self.questionButton = Button(mainWindow, image=self.questionMarkImage, height=50, width=50, command=self.questionButtonClick)
        self.questionButton.grid(row = 5, column=6)

        #Contact Button
        self.emailPath = PhotoImage(file = r"C:\Users\haoju\OneDrive\Desktop\CS361\Assignment5\email.png" )
        self.EmailImage = self.emailPath.subsample(50,50)
        self.EmailButton = Button(mainWindow, image=self.EmailImage, height=50, width=50, command=self.emailButoonClick)
        self.EmailButton.grid(row = 5, column= 7)
        # Dropdown box
        self.keyPad()

        
        # Entry Field
        self.entry = ttk.Entry(mainWindow , width=50)
        self.entry.grid(row = 5, column= 8)
        

    # The function open up a pop up window that display a set of instruction of how to use the application
        mainWindow.protocol("WM_DELETE_WINDOW", self.on_closing) 
    def questionButtonClick(self):
        top = Toplevel()
        top.geometry("400x400")
        top.title("Insturction Window")
        Label(top, text= "Instructions....(Will be fill later)",).place(x=0,y=0)

    def emailButoonClick(self):
        top = Toplevel()
        top.geometry("400x400")
        top.title("Email Window")
        Label(top, text= "Email chenhaoj@oregonstate.edu for Q&A, debugging, and more features",).place(x=0,y=0)
    
    def on_closing(self):

        if len(self.entry.get()) != 0:
            if tkinter.messagebox.askokcancel("Quit", "Do you want to quit, you still have content?"):
                root.destroy()
        else:
            root.destroy()
    def keyPad(self):
        keys = [
                ['1', '2', '3'],    
                ['4', '5', '6'],    
                ['7', '8', '9'],    
                ['+', '0', '-'], 
                ['*',  'Enter', '/']   
            ]
        for y, row in enumerate(keys, 1):
            for x, key in enumerate(row):
                # `lambda` inside `for` has to use `val=key:code(val)` 
                # instead of direct `code(key)`
                b = Button(root, text=key, command=lambda val=key:press(val,self.entry))
                b.grid(row=x+12,column=y+12)



root = Tk()
root.geometry("750x750")
root.resizable(False,False)
Logo = Label(root, text="Graphing Calulator Beta")
Logo.place(relx=0.4, rely=0)

alegbra = alegbra(root)
# coming = comingSoon(root)

options = [
        "Algebra", 
        "Coming Soon....."
]

# Dropdown menu
clicked = StringVar()
clicked.set("Algebra")
drop = OptionMenu(root, clicked, *options)
drop.grid(column= 5, row= 5)


root.mainloop()













# # Input Field
# # Check if the entry box is empty or not



# warning()
