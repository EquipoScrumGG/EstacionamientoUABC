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
    self.btnnew("Agregar Cajon","3",ap.AddParking)
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

  def callback(self):
    # print("click")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    #print(filename)
    generarHorario.generar(filename) #Envia la direccion absoluta del archivo de texto para generar el csv
    # with open(filename, 'r') as file:
    #   data = file.read()
    # print(data)
    
root = tk.Tk()
pp = Main(root)
root.mainloop()
