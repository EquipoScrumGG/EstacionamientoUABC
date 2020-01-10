import tkinter as tk
import sqlite3

class ModTeacher:
  db_name = 'database.db'
  def __init__(self,master,number):
    self.master = master
    self.master.geometry("400x400+200+200")
    self.result = tk.StringVar()
    self.rturno = tk.StringVar()
    self.rcajon = tk.StringVar()

    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Modificar Docente").pack()

    self.label = tk.Label(master,text="Numero del Docente").pack()
    self.clave = tk.Entry(master,width=50)
    self.clave.pack()
    self.search = tk .Button(master,text="Buscar",command=self.search_data).pack()

    self.label = tk.Label(master,text="Nombre del Docente").pack()
    self.name = tk.Entry(master,width=50,textvariable = self.result)
    self.name.pack()
    self.label = tk.Label(master,text="Turno").pack()
    self.turno = tk.Entry(master,width=50,textvariable = self.rturno)
    self.turno.pack()
    self.label = tk.Label(master,text="Cajon").pack()
    self.cajon = tk.Entry(master,width=50,textvariable = self.rcajon)
    self.cajon.pack()
    self.save = tk .Button(master,text="modificar Docente",command= self.mod_data).pack()

    self.quit = tk.Button(self.frame,text= "Cerrar",command= self.close_window)
    self.quit.pack()
    self.frame.pack()

  def close_window(self):
    self.master.destroy()

  def search_data(self):
    if self.validacion():
      cla = self.clave.get()
      query= 'SELECT Nombre,Turno,Cajon FROM Maestros WHERE Clave='+cla
      # parameters = (self.name.get(),self.clave.get(),self.turno.get(),self.cajon.get())
      r = self.run_query(query,cla)
      for row in r:
        self.result.set(row[0])
        self.rturno.set(row[1])
        self.rcajon.set(row[2])
    else:
      print('Faltaron Valores')

  def mod_data(self):
    if self.validacion2():
      cla = self.clave.get()
      nom = self.name.get()
      tur = self.turno.get()
      caj = self.cajon.get()
      query ='UPDATE Maestros SET Nombre = "'+nom+'", Turno = '+tur+', Cajon = '+caj+' WHERE Clave = '+cla
      print(query)
      self.run_query2(query)
    else:
      print('Faltaron Valores')

  def run_query(self,query,cla):
    with sqlite3.connect(self.db_name, timeout=10) as conn:
      esx = conn.cursor()
      result = esx.execute(query)
      records = result.fetchall()
      conn.commit()
      for row in records:
        print(row[0])
        print(row[1])
    return records

  def run_query2(self,query):
    with sqlite3.connect(self.db_name, timeout=10) as conn:
      esx = conn.cursor()
      result = esx.execute(query)
      # records = result.fetchall()
      # for row in records:
        # print(row[0])
        # print(row[1])
    # return records

  def validacion(self):
    return len(self.clave.get())!= 0

  def validacion2(self):
    return len(self.name.get())!= 0 and len(self.clave.get()) !=0 and len(self.turno.get()) !=0 and len(self.cajon.get()) !=0