import tkinter as tk
import sqlite3

class DeleteTeacher:
  db_name = 'database.db'
  def __init__(self,master,number):
    self.master = master
    self.master.geometry("400x400+200+200")
    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Eliminar Docente").pack()

    self.label = tk.Label(master,text="Numero del Docente").pack()
    self.clave = tk.Entry(master,width=50)
    self.clave.pack()
    self.delete = tk .Button(master,text="Elininar Docente",command= self.delmaestro).pack()

    self.quit = tk.Button(self.frame,text= "Cerrar",command= self.close_window)
    self.quit.pack()
    self.frame.pack()

  def close_window(self):
    self.master.destroy()

  def delmaestro(self):
    if self.validacion():
      cla = self.clave.get()
      query= 'DELETE FROM Maestros WHERE Clave ='+cla
      print(query)
      self.run_query2(query)
    else:
      print('Faltaron valores')

  def run_query2(self,query):
    with sqlite3.connect(self.db_name, timeout=10) as conn:
      esx = conn.cursor()
      result = esx.execute(query)

  def validacion(self):
    return len(self.clave.get())!= 0