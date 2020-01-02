import tkinter as tk
import sqlite3

class AddTeacher:
  def __init__(self,master,number):
    self.master = master
    self.master.geometry("400x400+200+200")
    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Agregar Docente").pack()

    self.label = tk.Label(master,text="Nombre del Docente").pack()
    self.name = tk.Entry(master,width=50).pack()
    self.label = tk.Label(master,text="Clave del Docente").pack()
    self.clave = tk.Entry(master,width=50).pack()
    self.save = tk .Button(master,text="Salvar Docente")

    self.quit = tk.Button(self.frame,text= "Cerrar",command= self.close_window)
    self.quit.pack()
    self.frame.pack()

  def close_window(self):
    self.master.destroy()

  def run_query(self,query,parameters=()):
        with sqlite3.connect(self.db_name, timeout=10) as conn:
            esx = conn.cursor()
            result = esx.execute(query,parameters)
            conn.commit()
        return result

  def get_Datos(self):
    #limpiamos las tablas
    records = self.tree.get_children()
    for element in records:
      self.tree.delete(element)
    #consultando la base de datos
    query = 'SELECT * FROM Maestros ORDER BY Nombre DESC'
    db_rows = self.run_query(query)
    for row in db_rows:
      self.tree.insert('',0,text=row[0],values=row[1])

  def validacion(self):
    return len(self.name.get())!= 0 and len(self.numeroid.get()) !=0


  def add_maestro(self):
    if self.validacion():
      query= 'INSERT INTO Maestros VALUES(?,?)'
      parameters = (self.name.get(),self.numeroid.get())
      self.run_query(query,parameters)
        
    else:
      print('Faltaron Valores')
        
    self.get_Datos()