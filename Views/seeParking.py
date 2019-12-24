import tkinter as tk

class SeeParking:
  def __init__(self,master,number):
    self.master = master
    self.master.geometry("400x400+200+200")
    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Ver Cajones").pack()
    self.quit = tk.Button(self.frame,text= "Cerrar",command= self.close_window)
    self.quit.pack()
    self.frame.pack()

  def close_window(self):
    self.master.destroy()