import PIL
from PIL import Image as Pil_image, ImageTk as Pil_imageTk
import os
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from pandastable import Table, TableModel
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D


clicked=0
d=None
prei=[]


root=Tk()
root.title('MWD Analysis')
c=root.iconbitmap(r'C:\Users\rodri\Documents\Python\Proyecto Aplicacion\Mcdo-Design-Compass-Compass-Gold-Black.ico')
root.geometry('530x670')
my_img0=PIL.ImageTk.PhotoImage(PIL.Image.open(r'C:\Users\rodri\Documents\Python\Proyecto Aplicacion\Compass-Gold-Black-icon.png'))
main_label=Label(image=my_img0)
main_label.grid(row=0,column=0,columnspan=3)
def seleccion():
    global df
    global calco
    global d
    global interpreter
    root.filename= filedialog.askopenfilename(initialdir=r'C:\Users\rodri\Documents\Python\Proyecto Aplicacion\DATA',title='Seleccione un Archivo',filetypes=(('Archivos CSV','*.csv'),('Archivos Excel','*.xlsx'),('Archivos Excel 2003','*.xls')))
    base=os.path.basename(root.filename)
    ext=(os.path.splitext(base)[1])
    d=(root.filename,ext)
    def csv_reader():
        global separador
        global decimal
        topo=Toplevel()
        topo.title('Importando archivo CSV')
        topo.geometry('330x115')
        separador=StringVar()
        decimal=StringVar()
        label_separador=Label(topo,text='Seleccione separador de valores').grid(row=0,column=0)
        label_decimal=Label(topo,text='Seleccione separador decimal').grid(row=1,column=0)
        drop_separador=OptionMenu(topo,separador,',',';','.').grid(row=0,column=1)
        drop_decimal=OptionMenu(topo,decimal,',','.').grid(row=1,column=1)
        finish_button=Button(topo,text='Aceptar',height = 1,width = 7,command=lambda:finisher(topo)).grid(row=2,column=2)
    
    def excel_reader():
        global interpreter
        global selected
        xls = pd.ExcelFile(str(d[0]))
        interpreter=xls.sheet_names

        topo=Toplevel()
        topo.title('Importando archivo Excel')
        topo.geometry('500x80')
        selected=StringVar()
        label_excel=Label(topo,text='Seleccione hoja donde estan los valores').grid(row=0,column=0)
        drop_excel=OptionMenu(topo,selected,*interpreter)
        drop_excel.grid(row=0,column=1)
        drop_excel.config(width=16)
        finish_button=Button(topo,text='Aceptar',height = 1,width = 7,command=lambda:finisher(topo)).grid(row=2,column=2)
    def finisher(window):
        global calco
        global interpreter
        global selected
        global separador
        global decimal
        global df
        global d
        window.destroy()
        try:
            df=pd.read_csv(str(d[0]),sep=str(separador.get()),decimal=str(decimal.get()))
        except:
            df=pd.read_excel(str(d[0]),sheet_name=str(selected.get()))    
        calc_button=Button(frame_main,text='Calcular',command=lambda:calcular(calco.get()),width = 20,state=NORMAL).grid(row=1,column=2)

    if d[1]=='.csv':
        csv_reader()
    elif d[1]==('.xlsx' or '.xls'):
        excel_reader()

def calcular(modo):
    global clicked
    global df
    clicked=1
    dogleg_angle=[0]
    temp_ns=[0]
    temp_ew=[0]
    temp_tvd=[0]
    dls=[0]
    F_corr=[1]
    tvd_total=0
    ns_total=0
    ew_total=0
    tvd_final=[0]
    ns_final=[0]
    ew_final=[0]
    error=0
    try:
        df['Inclinacion']=df['Inclinacion'].astype(float)
        df["Inclinacion"]=0.5*0.03490658503*df["Inclinacion"]
        df['Azimuth']=df['Azimuth'].astype(float)
        df['Azimuth']=0.5*0.03490658503*df['Azimuth']
    except:
        messagebox.showerror('Formato no valido','Recuerde que la informacion debe contar con columnas con los terminos TVD(ft),MD(ft),Azimuth(°),Inclinacion(°)')
    
    if modo=='Minima Curvatura':

        try:
            df=df[['MD','Inclinacion','Azimuth','TVD']]
        except:
            messagebox.showerror('Formato no valido','Recuerde que la informacion debe contar con columnas con los terminos TVD(ft),MD(ft),Azimuth(°),Inclinacion(°)')
        df.loc[-1] = [0,0,0,0]
        df.index = df.index + 1
        df = df.sort_index()

        for n in range(1,(len(df))):
            b=np.arccos(np.cos(df["Inclinacion"][n]-df["Inclinacion"][n-1])-np.sin(df["Inclinacion"][n])*np.sin(df["Inclinacion"][n-1])*(1-(np.cos((df["Azimuth"][n])-(df["Azimuth"][n-1])))))
            dogleg_angle.append(b)
        df["Dogleg_angle"] = dogleg_angle

        for n in range(1,(len(df))):
            if df["Dogleg_angle"][n]==0:
                f=1
            else:
                f=(2/df["Dogleg_angle"][n])*np.tan(df["Dogleg_angle"][n]/2)
            F_corr.append(f)
        df["Factor de Correcion"] = F_corr

        for n in range(1,(len(df))):
            ns=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.cos(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*(np.cos(df["Azimuth"][n])))*df["Factor de Correcion"][n]
            temp_ns.append(ns)
        df["Delta Norte-Sur"] = temp_ns

        for n in range(1,(len(df))):
            ew=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.sin(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*(np.sin(df["Azimuth"][n])))*df["Factor de Correcion"][n]
            temp_ew.append(ew)
        df["Delta Este-Oeste"] = temp_ew

        for n in range(1,(len(df))):
            ns_total=ns_total+df["Delta Norte-Sur"][n]
            ns_final.append(ns_total)

        for n in range(1,(len(df))):
            ew_total=ew_total+df["Delta Este-Oeste"][n]
            ew_final.append(ew_total)

        for n in range(1,(len(df))):
            temp_dls=100*df["Dogleg_angle"][n]/(df["MD"][n]-df["MD"][n-1])
            dls.append(temp_dls/(0.5*0.03490658503))

    elif modo=='Angulo Medio':

        try:
            df=df[['MD','Inclinacion','Azimuth']]
        except:
            messagebox.showerror('Formato no valido','Recuerde que la informacion debe contar con columnas con los terminos MD(ft),Azimuth(°),Inclinacion(°)')        
        df.loc[-1] = [0,0,0]
        df.index = df.index + 1
        df = df.sort_index()

        for n in range(1,(len(df))):
            tvd=((df["MD"][n]-df["MD"][n-1]))*(np.cos((df["Inclinacion"][n-1]+df["Inclinacion"][n])/2))
            temp_tvd.append(tvd)
        df["Delta TVD"] = temp_tvd

        for n in range(1,(len(df))):
            try:
                if abs(df["Azimuth"][n]-df["Azimuth"][n-1])>5:
                    raise Exception
                ns=((df["MD"][n]-df["MD"][n-1]))*((np.sin((df["Inclinacion"][n-1]+df["Inclinacion"][n])/2)*abs((np.cos((df["Azimuth"][n-1]+df["Azimuth"][n])/2)))))
            except:
                error=1
                ns=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.cos(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*np.cos(df["Azimuth"][n]))
            temp_ns.append(ns)
        df["Delta Norte-Sur"] = temp_ns

        for n in range(1,(len(df))):
            try:
                if abs(df["Azimuth"][n]-df["Azimuth"][n-1])>5:
                    raise Exception
                ew=((df["MD"][n]-df["MD"][n-1]))*((np.sin((df["Inclinacion"][n-1]+df["Inclinacion"][n])/2)*(np.sin((df["Azimuth"][n-1]+df["Azimuth"][n])/2))))
            except:
                error=1
                ew=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.sin(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*np.sin(df["Azimuth"][n]))
            temp_ew.append(ew)
        df["Delta Este-Oeste"] = temp_ew

        for n in range(1,(len(df))):
            tvd_total=tvd_total+df["Delta TVD"][n]
            tvd_final.append(tvd_total)
  
        for n in range(1,(len(df))):
            ns_total=ns_total+df["Delta Norte-Sur"][n]
            ns_final.append(ns_total)

        for n in range(1,(len(df))):
            ew_total=ew_total+df["Delta Este-Oeste"][n]
            ew_final.append(ew_total)


    elif modo=='Tangencial':

        try:
            df=df[['MD','Inclinacion','Azimuth']]
        except:
            messagebox.showerror('Formato no valido','Recuerde que la informacion debe contar con columnas con los terminos MD(ft),Azimuth(°),Inclinacion(°)')        
        df.loc[-1] = [0,0,0]
        df.index = df.index + 1
        df = df.sort_index()

        for n in range(1,(len(df))):
            tvd=(df["MD"][n]-df["MD"][n-1])*np.cos(df["Inclinacion"][n])
            temp_tvd.append(tvd)
        df["Delta TVD"] = temp_tvd

        for n in range(1,(len(df))):
            ns=(df["MD"][n]-df["MD"][n-1])*np.sin(df["Inclinacion"][n])*np.cos(df["Azimuth"][n])
            temp_ns.append(ns)
        df["Delta Norte-Sur"] = temp_ns

        for n in range(1,(len(df))):
            ew=(df["MD"][n]-df["MD"][n-1])*np.sin(df["Inclinacion"][n])*np.sin(df["Azimuth"][n])
            temp_ew.append(ew)
        df["Delta Este-Oeste"] = temp_ew

        for n in range(1,(len(df))):
            tvd_total=tvd_total+df["Delta TVD"][n]
            tvd_final.append(tvd_total)

        for n in range(1,(len(df))):
            ns_total=ns_total+df["Delta Norte-Sur"][n]
            ns_final.append(ns_total)

        for n in range(1,(len(df))):
            ew_total=ew_total+df["Delta Este-Oeste"][n]
            ew_final.append(ew_total)

        for n in range(1,(len(df))):
            temp_dls=100/((df["MD"][n]-df["MD"][n-1])*((np.sin(df["Inclinacion"][n])*np.sin(df["Inclinacion"][n-1]))*(np.sin(df["Azimuth"][n])*np.sin(df["Azimuth"][n-1])+np.cos(df["Azimuth"][n])*np.cos(df["Azimuth"][n-1]))+(np.cos(df["Inclinacion"][n])*np.cos(df["Inclinacion"][n-1]))))
            dls.append(temp_dls)


    elif modo=='Radio de Curvatura':
        try:
            df=df[['MD','Inclinacion','Azimuth']]
        except:
            messagebox.showerror('Formato no valido','Recuerde que la informacion debe contar con columnas con los terminos MD(ft),Azimuth(°),Inclinacion(°)')        
        df.loc[-1] = [0,0,0]
        df.index = df.index + 1
        df = df.sort_index()

        for n in range(1,(len(df))):
            with np.errstate(all='raise'):
                try:
                    tvd=((df["MD"][n]-df["MD"][n-1]))*(np.sin(df["Inclinacion"][n])-np.sin(df["Inclinacion"][n-1]))/(df["Inclinacion"][n]-df["Inclinacion"][n-1])
                except:
                    error=1
                    tvd=((df["MD"][n]-df["MD"][n-1])/2)*(np.cos(df["Inclinacion"][n])+np.cos(df["Inclinacion"][n-1]))
                temp_tvd.append(tvd)
        df["Delta TVD"] = temp_tvd

        for n in range(1,(len(df))):
            with np.errstate(all='raise'):
                try:
                    if abs(df["Azimuth"][n]-df["Azimuth"][n-1])>5:
                        raise Exception
                    ns=(df["MD"][n]-df["MD"][n-1])*(np.cos(df["Inclinacion"][n-1])-np.cos(df["Inclinacion"][n]))*(np.sin(df["Azimuth"][n])-np.sin(df["Azimuth"][n-1]))/((df["Inclinacion"][n]-df["Inclinacion"][n-1])*(df["Azimuth"][n]-df["Azimuth"][n-1]))
                except:
                    error=1
                    ns=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.cos(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*np.cos(df["Azimuth"][n]))
            temp_ns.append(ns)
        df["Delta Norte-Sur"] = temp_ns

        for n in range(1,(len(df))):
            with np.errstate(all='raise'):
                try:
                    if abs(df["Azimuth"][n]-df["Azimuth"][n-1])>5:
                        raise Exception
                    ew=((df["MD"][n]-df["MD"][n-1]))*(np.cos(df["Inclinacion"][n-1])-np.cos(df["Inclinacion"][n]))*(np.cos(df["Azimuth"][n-1])-np.cos(df["Azimuth"][n]))/((df["Inclinacion"][n]-df["Inclinacion"][n-1])*(df["Azimuth"][n]-df["Azimuth"][n-1]))
                except:
                    error=1
                    ew=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.sin(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*np.sin(df["Azimuth"][n]))
                temp_ew.append(ew)
        df["Delta Este-Oeste"] = temp_ew

        for n in range(1,(len(df))):
            tvd_total=tvd_total+df["Delta TVD"][n]
            tvd_final.append(tvd_total)

        for n in range(1,(len(df))):
            ns_total=ns_total+df["Delta Norte-Sur"][n]
            ns_final.append(ns_total)

        for n in range(1,(len(df))):
            ew_total=ew_total+df["Delta Este-Oeste"][n]
            ew_final.append(ew_total)

        for n in range(1,(len(df))):
            temp_dls=np.arccos(np.cos(df['Inclinacion'][n])*np.cos(df['Inclinacion'][n-1])+np.sin(df['Inclinacion'][n])*np.sin(df['Inclinacion'][n-1])*np.cos(df["Azimuth"][n]-df["Azimuth"][n-1]))*(100/(df["MD"][n]-df["MD"][n-1]))
            dls.append(temp_dls/(0.5*0.03490658503))

    elif modo=='Tangencial Balanceada':

        try:
            df=df[['MD','Inclinacion','Azimuth']]
        except:
            messagebox.showerror('Formato no valido','Recuerde que la informacion debe contar con columnas con los terminos MD(ft),Azimuth(°),Inclinacion(°)')        
        df.loc[-1] = [0,0,0]
        df.index = df.index + 1
        df = df.sort_index()

        for n in range(1,(len(df))):

            tvd=((df["MD"][n]-df["MD"][n-1])/2)*(np.cos(df["Inclinacion"][n])+np.cos(df["Inclinacion"][n-1]))
            temp_tvd.append(tvd)
        df["Delta TVD"] = temp_tvd

        for n in range(1,(len(df))):
            ns=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.cos(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*np.cos(df["Azimuth"][n]))
            temp_ns.append(ns)
        df["Delta Norte-Sur"] = temp_ns

        for n in range(1,(len(df))):
            ew=((df["MD"][n]-df["MD"][n-1])/2)*(np.sin(df["Inclinacion"][n-1])*np.sin(df["Azimuth"][n-1])+np.sin(df["Inclinacion"][n])*np.sin(df["Azimuth"][n]))
            temp_ew.append(ew)
        df["Delta Este-Oeste"] = temp_ew

        for n in range(1,(len(df))):
            tvd_total=tvd_total+df["Delta TVD"][n]
            tvd_final.append(tvd_total)

        for n in range(1,(len(df))):
            ns_total=ns_total+df["Delta Norte-Sur"][n]
            ns_final.append(ns_total)

        for n in range(1,(len(df))):
            ew_total=ew_total+df["Delta Este-Oeste"][n]
            ew_final.append(ew_total)

        for n in range(1,(len(df))):
            temp_dls=100/((df["MD"][n]-df["MD"][n-1])*((np.sin(df["Inclinacion"][n])*np.sin(df["Inclinacion"][n-1]))*(np.sin(df["Azimuth"][n])*np.sin(df["Azimuth"][n-1])+np.cos(df["Azimuth"][n])*np.cos(df["Azimuth"][n-1]))+(np.cos(df["Inclinacion"][n])*np.cos(df["Inclinacion"][n-1]))))
            dls.append(temp_dls)

    df["Norte-Sur"] = ns_final
    df["Este-Oeste"] = ew_final
    df=df.astype(float).round(3)
    df=df.astype(object)
    if error==1:
        messagebox.showerror('Error de calculo','Los datos subidos son incompatibles con el metodo seleccionado, algunos valores han sido calculados con el metodo Tangencial Balanceada en su lugar.')
    top=Toplevel(root)
    f = Frame(top, width=800, height=400)
    f.pack(fill=BOTH,expand=1)
    pt = Table(f, dataframe=df,showtoolbar=True, showstatusbar=True)
    try:
        df["TVD"] = tvd_final
        pt.setColumnColors(cols=[0,1,2],clr='gray')
    except:
        pt.setColumnColors(cols=[0,1,2,3],clr='gray')
    try:
        df['Dogleg Severity'] = dls
    except:
        'do nothing'
    pt.show()
    #enabler_grafo(grafo)


def graficar(grafo):
    global df

    setter=max(1.25*max(abs(df["Norte-Sur"])),1.25*max(abs(df["Este-Oeste"])))

    if grafo=='Grafico Tridimensional':
        class Arrow3D(FancyArrowPatch):
            def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
                super().__init__((0,0), (0,0), *args, **kwargs)
                self._xyz = (x,y,z)
                self._dxdydz = (dx,dy,dz)

            def draw(self, renderer):
                x1,y1,z1 = self._xyz
                dx,dy,dz = self._dxdydz
                x2,y2,z2 = (x1+dx,y1+dy,z1+dz)

                xs, ys, zs = proj_transform((x1,x2),(y1,y2),(z1,z2), renderer.M)
                self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
                super().draw(renderer)

        def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
            '''Add an 3d arrow to an `Axes3D` instance.'''

            arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
            ax.add_artist(arrow)

        setattr(Axes3D,'arrow3D',_arrow3D)

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_zlim(1.25*max(abs(df["TVD"])),0)
        

        z =list(df['TVD'])
        x =list(df["Norte-Sur"])
        y =list(df["Este-Oeste"])
        ax.plot(x, y, z, label='Trayectoria del pozo')
        arrow=ax.arrow3D(-setter,1.25*-setter,0,
            2*setter,0,0,
            mutation_scale=20,
            arrowstyle="-|>",
            label='NORTE')
        
        ax.set_xlabel('Sur(-)Norte(+) (ft)',rotation=0)
        ax.set_ylabel('Oeste(-)Este(+) (ft)',rotation=0)
        ax.set_zlabel('Profundidad (ft)')
        ax.legend()
        plt.show()

    elif grafo=='Corte N-S/TVD':
        fig, ax = plt.subplots()
        x=list(df["Norte-Sur"])
        y=list(df['TVD'])
        ax.plot(x, y)

        ax.set(xlabel='Sur(-)Norte(+) (ft)', ylabel='Profundidad (ft)',
            title='Corte N-S/TVD')
        ax.set_xlim(-setter,setter)
        ax.set_ylim(1.25*max(abs(df["TVD"])),0)

        ax.grid()
        plt.show()

    elif grafo=='Corte E-W/TVD':

        fig, ax = plt.subplots()
        x=list(df["Este-Oeste"])
        y=list(df['TVD'])
        ax.plot(x, y)

        ax.set(xlabel='Oeste(-)Este(+) (ft)', ylabel='Profundidad (ft)',
            title='Corte E-W/TVD')
        ax.set_xlim(-setter,setter)
        ax.set_ylim(1.25*max(abs(df["TVD"])),0)

        ax.grid()
        plt.show()  

    elif grafo=='Corte Superior':

        fig, ax = plt.subplots()
        x=list(df["Este-Oeste"])
        y=list(df["Norte-Sur"])
        ax.plot(x, y)

        ax.set(xlabel='Oeste(-)Este(+) (ft)', ylabel='Sur(-)Norte(+) (ft)',
            title='Corte Superior')
        ax.set_xlim(-setter,setter)
        ax.set_xlim(-setter,setter)

        ax.grid()
        plt.show()

    elif grafo=='DogLeg Severity':
        try:
            fig, ax = plt.subplots()
            x=list(df['Dogleg Severity'])
            y=list(df['MD'])
            ax.plot(x, y)

            ax.set(xlabel='Dogleg Severity (°/100ft)', ylabel='Profundidad Medida (ft)',
                title='Dogleg Severity')
            ax.set_ylim(1.1*max(abs(df["MD"])),0)

            ax.grid()
            plt.show()
        except:   
            messagebox.showerror('Error al Graficar','El metodo de calculo seleccionado no estima severidad de dogleg')    
            plt.close()








frame_main=LabelFrame(root,padx=5,pady=5,bd=2,text='Calculos')
frame_main.grid(row=1,column=0,columnspan=3,padx=2,pady=2)
frame_sec=LabelFrame(root,padx=5,pady=5,bd=2,text='Graficos')
frame_sec.grid(row=2,column=0,columnspan=3,padx=2,pady=2)

def enabler_select():
    select_button=Button(frame_main,text='Seleccion MWD Data',command=seleccion,width = 20).grid(row=1,column=1)
def enabler_grafo():
    global clicked
    if grafo!='Seleccione Tipo de Grafico' and clicked!=0:
        graph_button=Button(frame_sec,text='Graficar',command=lambda:graficar(grafo.get()),width = 20).grid(row=0,column=1)

calco=StringVar()
calco.set('Metodo de Calculo...')
grafo=StringVar()
grafo.set('Seleccione Tipo de Grafico')
drop_calco=OptionMenu(frame_main,calco,'Angulo Medio','Radio de Curvatura','Tangencial','Tangencial Balanceada','Minima Curvatura',command=lambda _:enabler_select())
drop_calco.grid(row=1,column=0)
drop_calco.config(width=16)
select_button=Button(frame_main,text='Seleccion MWD Data',command=seleccion,width = 20,state=DISABLED).grid(row=1,column=1)
calc_button=Button(frame_main,text='Calcular',command=calcular,width = 20,state=DISABLED).grid(row=1,column=2)
drop_grafo=OptionMenu(frame_sec,grafo,'Grafico Tridimensional','Corte N-S/TVD','Corte E-W/TVD','Corte Superior','DogLeg Severity',command=lambda _:enabler_grafo())
drop_grafo.grid(row=0,column=0)
drop_grafo.config(width=19)
graph_button=Button(frame_sec,text='Graficar',command=graficar,width = 20,state=DISABLED).grid(row=0,column=1)













mainloop()