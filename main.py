from tkinter import *
from tkinter.filedialog import askopenfilename
window = Tk()

def callback():
  print("click")
  filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
  with open(filename, 'r') as file:
    data = file.read()
  print(data)

window.geometry("800x500")
window.title("Sistema de Estacionamiento")
btnSearchFile = Button(window, text="search", command=callback).pack()
window.mainloop()