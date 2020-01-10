import tkinter as tk
import sqlite3

class AddTeacher:
  db_name = 'database.db'
  def __init__(self,master,number):
    self.master = master
    self.master.geometry("400x400+200+200")
    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Agregar Docente").pack()

    self.label = tk.Label(master,text="Nombre del Docente").pack()
    self.name = tk.Entry(master,width=50)
    self.name.pack()
    self.label = tk.Label(master,text="Numero del Docente").pack()
    self.clave = tk.Entry(master,width=50)
    self.clave.pack()
    self.label = tk.Label(master,text="Turno").pack()
    self.turno = tk.Entry(master,width=50)
    self.turno.pack()
    self.label = tk.Label(master,text="Cajon").pack()
    self.cajon = tk.Entry(master,width=50)
    self.cajon.pack()
    self.save = tk .Button(master,text="Guardar Docente",command=self.add_maestro).pack()

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

  def validacion(self):
    return len(self.name.get())!= 0 and len(self.clave.get()) !=0 and len(self.turno.get()) !=0


  def add_maestro(self):
    if self.validacion():
      query= 'INSERT INTO Maestros VALUES(?,?,?,?)'
      parameters = (self.name.get(),self.clave.get(),self.turno.get(),self.cajon.get())
      self.run_query(query,parameters)
        
    else:
      print('Faltaron Valores')
        
    # self.get_Datos()