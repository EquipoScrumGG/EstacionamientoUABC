import tkinter as tk

class ModTeacher:
  def __init__(self,master,number):
    self.master = master
    self.master.geometry("400x400+200+200")
    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Modificar Docente").pack()

    self.label = tk.Label(master,text="Numero del Docente").pack()
    self.clave = tk.Entry(master,width=50).pack()
    self.search = tk .Button(master,text="Buscar").pack()
    self.label = tk.Label(master,text="Nombre del Docente").pack()
    self.name = tk.Entry(master,width=50).pack()
    self.label = tk.Label(master,text="Turno").pack()
    self.turno = tk.Entry(master,width=50).pack()
    self.label = tk.Label(master,text="Cajon").pack()
    self.cajon = tk.Entry(master,width=50).pack()
    self.save = tk .Button(master,text="modificar Docente").pack()

    self.quit = tk.Button(self.frame,text= "Cerrar",command= self.close_window)
    self.quit.pack()
    self.frame.pack()

  def close_window(self):
    self.master.destroy()