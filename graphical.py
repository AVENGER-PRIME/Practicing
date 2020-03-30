from tkinter import *
from core import *
def get_lib():
	library = Library_Name.get()
	print(library)


root = Tk()
root.title("Library Management Software")
root.geometry("655x544")


Extra = StringVar()
Library_Name = StringVar()
f1 = Frame(root).grid()
Label(f1, text = "____Library Management form____", font = "lucida 10 bold").pack()
f2 = Frame(root).grid(row = 1)
Label(f2, text = "Enter the Library Name : ", font = "lucida 8 bold").grid(row = 1, column = 3)
Entry(f2, textvariable = Library_Name).grid(row = 1, column = 5)
Label(f2, text = "Enter the books name seperated by commas : ", font = "lucida 8 bold").grid(row = 2, column = 3)
Entry(f2, textvariable = Extra).grid(row = 2, column = 5)
f3 = Frame(root).grid(row = 2)
Button(f3, text = "Submit", command = get_lib).grid(row = 3, column = 5)


root.mainloop()
