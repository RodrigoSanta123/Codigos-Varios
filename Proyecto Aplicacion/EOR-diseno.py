#librerias
import os
import pandas as pd
import numpy as np

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


#main frame de tkinter, importamos project data sheet
root=Tk()
root.title('Data Sheet import')
root.geometry('1000x1000')

#definimos comandos de la barra menu
def importar():
    root.filename= filedialog.askopenfilename(initialdir=r'C:\Users\rodri\Downloads',title='Seleccione un Archivo',filetypes=[("Excel files", ".xlsx .xls")])
    df=pd.read_excel(root.filename)

    #construccion de interfaz de importacion

    top = Toplevel()   
    top.geometry("1000x900")
    tratamiento_name=Label(top,text = "Tipo de tratamiento: ").place(x = 270,y = 40)   
    operadora_name = Label(top,text = "Operadora: ").place(x = 140,y = 120)  
    provincia_name = Label(top,text = "Provincia: ").place(x = 140,y = 220)  
    yac_name = Label(top,text = "Yacimiento: ").place(x = 140,y = 320)
    pozo_name = Label(top,text = "Pozo: ").place(x = 140,y = 420)
    cuenca_name=Label(top,text= "Cuenca: ").place(x=500,y=120)
    formacion_name = Label(top,text = "Formacion: ").place(x = 500,y = 220)
    formation_type_name = Label(top,text = "Tipo de formacion: ").place(x = 500,y = 320)
    prof_name = Label(top,text = "Profundidad (ft): ").place(x = 500,y = 420)
    a_name = Label(top,text = " a ").place(x = 650,y = 420)
    logs_name= Label(top,text = "Digitalizacion de Perfiles interpretados (.las, excel,etc): ").place(x = 140,y = 500)
    wso_name=Label(top,text = "Perfiles de Produccion del pozo: ").place(x = 140,y = 600)
    conformance_name=Label(top,text = "Data de trazadores: ").place(x = 140,y = 700)
    casing_leak_name=Label(top,text = "Digitalizacion de perfil MIT-MTT: ").place(x = 140,y = 800)

    aceptar_button = Button(top,text = "Aceptar",height = 2, width = 20).place(x = 800,y = 800)

    tratamientos=StringVar()
    tratment_type_dropdown =OptionMenu(top,tratamientos,'Conformance','Water Shut-Off','Casing Leak Repair')
    tratment_type_dropdown.place(x = 410,y = 35)
    tratment_type_dropdown.config(width=30)    

    operadora_input = Entry(top,width = 25)
    operadora_input.insert(END,str(df['Unnamed: 1'][0]))
    operadora_input.place(x = 220,y = 120)

    provincia_input = Entry(top,width = 25)
    provincia_input.insert(END,str(df['Unnamed: 1'][2]))
    provincia_input.place(x = 220,y = 220)

    yac_input = Entry(top,width = 25)
    yac_input.insert(END,str(df['Unnamed: 1'][6]))
    yac_input.place(x = 220,y = 320)

    pozo_input = Entry(top,width = 25)
    pozo_input.insert(END,str(df['Unnamed: 1'][5]))
    pozo_input.place(x = 220,y = 420)

    cuenca_input=Entry(top,width = 25)
    cuenca_input.insert(END,str(df['Unnamed: 1'][7]))
    cuenca_input.place(x = 580,y = 120)

    formacion_input = Entry(top,width = 25)
    formacion_input.insert(END,str(df['Unnamed: 1'][9]))
    formacion_input.place(x = 580,y = 220)

    formaciones=StringVar()
    formation_type_dropdown =OptionMenu(top,formaciones,'Matrix-Rock Sandstone','Matrix-Rock Carbonate','Unconsolidated Sandstone','Wormhole Dominated Carbonates','Karst/Vuggy','Naturally Fractured Formation','Matrix-Rock/Assisted with fractures')
    formation_type_dropdown.place(x = 620,y = 315)
    formation_type_dropdown.config(width=30)

    prof_input_1 = Entry(top,width = 5)
    prof_input_1.insert(END,str(df['Unnamed: 1'][11]))
    prof_input_1.place(x = 610,y = 420)

    prof_input_2 = Entry(top,width = 5)
    prof_input_2.insert(END,str(df['Unnamed: 1'][11]+df['Unnamed: 1'][12]))
    prof_input_2.place(x = 670,y = 420)


    #funcion de importacion
    def import_general(x):
        if x==1:
            top.filename= filedialog.askopenfilename(initialdir=r'C:\Users\rodri\Downloads',title='Seleccione un Archivo',filetypes=[("Excel files", ".xlsx .xls"),("CSV files", ".csv"),("TXT files", ".txt"),("LAS files", ".las")])
  


    #botones de importacion
    logs_button= Button(top,text = "Importar",height = 2, width = 20,command=lambda:import_general(1)).place(x = 470,y = 485)
    log_format=StringVar()
    logs_format_drop=OptionMenu(top,log_format,'.xlsx .xls',".csv",".txt",".las")
    logs_format_drop.place(x = 650,y = 485)
    logs_format_drop.config(width=10,height = 2)
    wso_button= Button(top,text = "Importar",height = 2, width = 20,command=lambda:import_general(2)).place(x = 350,y = 585)
    wso_format=StringVar()
    wso_format_drop=OptionMenu(top,wso_format,'.xlsx .xls',".csv",".txt",".las")
    wso_format_drop.place(x = 530,y = 585)
    wso_format_drop.config(width=10,height = 2)
    conformance_button= Button(top,text = "Importar",height = 2, width = 20,command=import_general(3)).place(x = 350,y = 685)
    casing_leak_button= Button(top,text = "Importar",height = 2, width = 20,command=lambda:import_general(4)).place(x = 350,y = 785)
    casing_leak_format=StringVar()
    casing_leak_format_drop=OptionMenu(top,casing_leak_format,'.xlsx .xls',".csv",".txt",".las")
    casing_leak_format_drop.place(x = 530,y = 785)
    casing_leak_format_drop.config(width=10,height = 2)

    top.mainloop() 

#creamos barra menu

menubar=Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Importar", command=importar)
filemenu.add_command(label="Guardar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)



root.mainloop()