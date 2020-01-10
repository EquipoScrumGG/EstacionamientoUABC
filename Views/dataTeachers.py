import tkinter as tk
from tkinter import ttk
from tkinter import Tk,Label,LabelFrame,Entry,W,E,CENTER
import sqlite3

class DataTeachers:

  db_name = 'database.db'

  def __init__(self,master,number):
    self.master = master
    self.master.geometry("800x400+200+200")
    self.frame = tk.Frame(self.master)
    self.label = tk.Label(master,text="Datos de los docentes").pack()

    #tabla
    self.tree = ttk.Treeview(self.master)
    # self.tree.grid(row=4,column=0,columnspan=2)
    self.tree["columns"]=("clave","turno","cajon")
    self.tree.heading('#0',text= 'Nombre',anchor=tk.W)
    self.tree.heading('clave',text= 'Clave', anchor=tk.W)
    self.tree.heading('turno',text= 'Turno', anchor=tk.W)
    self.tree.heading('cajon',text= 'Cajon', anchor=tk.W)
    self.tree.pack(side=tk.TOP,fill=tk.X)
    self.get_Datos()

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
      self.tree.insert('',0,text=row[0],values=(row[1],row[2],row[3]))