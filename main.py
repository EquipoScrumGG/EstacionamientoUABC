import tkinter as tk
from tkinter.filedialog import askopenfilename
import Views.addTeacher as at
import Views.addParking as ap
import Views.dataTeachers as dt

class Main():

  def __init__(self,master):
    self.master = master
    self.master.geometry("400x400")
    self.frame = tk.Frame(self.master)
    self.btnCargarArchivo("Cargar Archivo")
    self.btnnew("Agregar Docente","2",at.AddTeacher)
    self.btnnew("Agregar Cajon","3",ap.AddParking)
    self.btnnew("Datos de los Docentes","4",dt.DataTeachers)
    self.frame.pack()

  def btnCargarArchivo(self,text):
    tk.Button(self.frame,text= text,command= lambda: self.callback()).pack() 

  def btnnew(self,text,number,_class):
    tk.Button(self.frame,text= text,command= lambda: self.new_window(number,_class)).pack()

  def new_window(self,number,_class):
    self.new = tk.Toplevel(self.master)
    _class(self.new,number)


  def callback(self):
    # print("click")
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    # with open(filename, 'r') as file:
    #   data = file.read()
    # print(data)

  # def principal(self):
  #   window.geometry("800x500")
  #   window.title("Sistema de Estacionamiento")
  #   btnSearchFile = Button(window,text="Cargar Archivo",width=25,command= self.callback)
  #   btnAddTeacher = Button(window,text="Agregar Docente",command= self.addTeacher)
  #   btnDeleteTeacher = Button(window, text="Eliminar Docente",command= self.deleteTeacher)
  #   btnAddBox = Button(window,text="Agregar cajon",command= self.addBox)
  #   btnTeacherData = Button(window,text="Datos de los docentes",command= self.teacherData)
    
root = tk.Tk()
pp = Main(root)
root.mainloop()
