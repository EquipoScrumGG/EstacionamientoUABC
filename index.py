import sqlite3
from tkinter import ttk
from tkinter import Tk,Label,LabelFrame,Entry,W,E,CENTER


class Maestros:

    db_name = 'database.db'


    def __init__(self,window):
        self.wind = window
        self.wind.geometry("1100x750+0+0")
        self.wind.title('Estacionamiento')

        #Crear Frame
        frame = LabelFrame(self.wind, text='Subir Archivo')
        frame.grid(row=0,column=0,columnspan=3,pady=20)

        #boton
        ttk.Button(frame,text='Abrir').grid(row=0,column=0,columnspan=2)
        
        #Barra Nombre
        Label(frame,text='Nombre de Maestro:').grid(row=2,column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=2,column=1)
        
        #barra Clave
        Label(frame,text='Clade de Maestro:').grid(row=3,column=0)
        self.numeroid = Entry(frame)
        self.numeroid.grid(row=3,column=1)

        #guardar Maestro
        ttk.Button(frame, text = 'Salvar Matestro',command=self.add_maestro).grid(row=4,columnspan=2,sticky=W+E)



        #tabla
        self.tree = ttk.Treeview(height=10, column=2)
        self.tree.grid(row=4,column=0,columnspan=2)
        self.tree.heading('#0', text= 'Nombre',anchor=CENTER)
        self.tree.heading('#1',text= 'Clave', anchor=CENTER)
        self.get_Datos()

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


if __name__ == '__main__':
    window = Tk()
    application = Maestros(window)
    window.mainloop()