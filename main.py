import tkinter as tk
from tkinter.filedialog import askopenfilename
import Views.addTeacher as at
import Views.addParking as ap
import Views.dataTeachers as dt
import Views.modTeacher as mt
import Views.deleteTeacher as delt
import Views.seeParking as sp
import generarHorario #Para generar el horario
from PIL import ImageTk, Image
import os
from ddt import ddt,data,unpack
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Date, String, VARCHAR
import pandas as pd
from read_data import getCSVData

@ddt
class Main():

  def __init__(self,master):
    self.master = master
    self.master.geometry("400x400")
    self.master.title("Estacionamiento")
    self.frame = tk.Frame(self.master)
    # img= ImageTk.PhotoImage(Image.open("cimarron.png"))
    # self.panel(img)
    self.btnCargarArchivo("Cargar Archivo")
    self.btnnew("Agregar Docente","2",at.AddTeacher) 
    self.btnnew("Datos de los Docentes","4",dt.DataTeachers)
    self.btnnew("Modificar Docente","5",mt.ModTeacher)
    self.btnnew("Eliminar Docente","6",delt.DeleteTeacher)
    self.btnnew("Ver Cajones",'7',sp.SeeParking)
    self.frame.pack()

  def btnCargarArchivo(self,text):
    tk.Button(self.frame,text= text,width= 30,command= lambda: self.callback()).pack(pady=5) 

  def btnnew(self,text,number,_class):
    tk.Button(self.frame,text= text,width= 30,command= lambda: self.new_window(number,_class)).pack(pady=5)

  def new_window(self,number,_class):
    self.new = tk.Toplevel(self.master)
    _class(self.new,number)

  # @data(*getCSVData("horario_generado.csv"))
  # @unpack
  def callback(self):
    # print("click")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    #print(filename)
    generarHorario.generar(filename) #Envia la direccion absoluta del archivo de texto para generar el csv
    # getCSVData("horario_generado.csv")
    # with open("horario_generado.csv", 'r') as file:
    #   data = file.read()
    # print(data)
    # print(NumeroEmpleado)
    #Borrar columna maestros
    data = pd.read_csv("horario_generado.csv") 
    df = pd.DataFrame(data)
    del df['MAESTRO']
    #df.drop ([df['column name'].map(len) < 1])
    #df.drop(df[(df["Martes"].str.len()< 1 )])
    #df[(df['Lunes'].str.len()< 2) & (df['Martes'].str.len()< 2) & (df['Miercoles'].str.len()< 2) & (df['Jueves'].str.len()< 2) & (df['Viernes'].str.len()< 2)]
    # Get names of indexes for which column Age has value 30
    #for i, row in df.iterrows():
      #numEmpleado = row['NumEmpleado']
      #print(numEmpleado)
      #df = df.replace({"X": numEmpleado})
    #print(df)
   # VariableAux = 0

    #for i in range(5354):
     # j = 4
      #a = df.loc[df.index[i], 'NumEmpleado']
      #for j in range(9):
       # if (df[i][j] == 'X'):
        #    df[VariableAux][j] = a
        #if (j==8):
        #  VariableAux+1

    df.to_csv('horario_generado.csv')

    engine  = create_engine('sqlite:///prueba.db')
    #conn = engine.connect()
    #res = conn.execute('Delect Maestros FROM Maestros')
    #df = pd.DataFrame(res.fetchall())
    #df.columns = res.keys()
    #conn.close()
    #print(df)
    Base = declarative_base()
    Base.metadata.create_all(engine)

    class cdb1(Base):
      #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
      __tablename__ = 'Maestros'
      __table_args__ = {'sqlite_autoincrement': True}
      #tell SQLAlchemy the name of column and its attributes:
      id = Column(Integer, primary_key=True, nullable=False) 
      NumEmpleado = Column(VARCHAR(40))
      Nombre = Column(VARCHAR(40))
      Horario = Column(Integer)
      #Payments = Column(Integer)
      #Status = Column(VARCHAR)

    file_name = 'horario_generado.csv'
    df = pd.read_csv(file_name)
    df.to_sql(con=engine, index_label='id', name=cdb1.__tablename__, if_exists='replace')

    #df = pd.DataFrame(res.fetchall())
    #df.columns = res.keys()
    #conn.close()

    
root = tk.Tk()
pp = Main(root)
root.mainloop()
