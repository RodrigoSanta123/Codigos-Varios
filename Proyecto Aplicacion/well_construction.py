
import os
import pandas as pd
import numpy as np

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PIL
from PIL import Image as Pil_image, ImageTk as Pil_imageTk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import ( FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

from scipy.ndimage import gaussian_filter1d

global d
d=None


root=Tk()
root.title('Well Construction')
c=root.iconbitmap(r'C:\Users\rodri\Documents\Python\Proyecto Aplicacion\iconfinder_refinery-oil_industry-power-factory-illustration-energy-gas-refinery-fuel-symbol-industrial_3652518.ico')
root.geometry('530x670')
my_img0=PIL.ImageTk.PhotoImage(PIL.Image.open(r'C:\Users\rodri\Documents\Python\Proyecto Aplicacion\iconfinder_refinery-oil_industry-power-factory-illustration-energy-gas-refinery-fuel-symbol-industrial_3652518.png'))
main_label=Label(image=my_img0)
main_label.grid(row=0,column=0,columnspan=3)


def enabler_select():
    select_button=Button(root,text='Importar',command=importar,width = 20).grid(row=1,column=1)

def importar():
    global raw,calco,interpreter

    root.filename= filedialog.askopenfilename(initialdir=r'C:\Users\rodri\Documents\Python\Proyecto Aplicacion\DATA',title='Seleccione un Archivo',filetypes=(('Archivos CSV','*.csv'),('Archivos Excel','*.xlsx'),('Archivos Excel 2003','*.xls')))
    base=os.path.basename(root.filename)
    ext=(os.path.splitext(base)[1])
    d=(root.filename,ext)
    def csv_reader():
        global separador,decimal

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
        global dato, prof
        def finishero(window):
            global df

            window.destroy()
            df=raw[[(str(prof.get())),(str(dato.get()))]]
            df=df.rename(columns={str(prof.get()):'Profundidad',str(dato.get()):'Dato'})
            df['Profundidad']=df['Profundidad'].astype(float)
            df['Dato']=df['Dato'].astype(float)
            df.dropna(axis=0, inplace=True)
            calc_button=Button(root,text='Calcular',command=lambda:calcular(curvas.get()),width = 20,state=NORMAL).grid(row=1,column=2)

        window.destroy()
        prof=StringVar()
        dato=StringVar()
        try:
            raw=pd.read_csv(str(d[0]),sep=str(separador.get()),decimal=str(decimal.get()))
        except:
            raw=pd.read_excel(str(d[0]),sheet_name=str(selected.get())) 
        topo=Toplevel()
        heads=list(raw)
        topo.title('Seleccion de columnas')
        topo.geometry('500x110') 
        label_prof=Label(topo,text='Seleccione columna con valores de profundidad').grid(row=0,column=0)
        label_dato=Label(topo,text='Seleccione columna con valores correspondientes').grid(row=1,column=0)
        drop_prof=OptionMenu(topo,prof,*heads).grid(row=0,column=1)
        drop_dato=OptionMenu(topo,dato,*heads).grid(row=1,column=1)
        finish_button=Button(topo,text='Aceptar',height = 1,width = 7,command=lambda:finishero(topo)).grid(row=2,column=2)

    if d[1]=='.csv':
        csv_reader()
    elif d[1]==('.xlsx' or '.xls'):
        excel_reader()

def calcular(modo):
    global r
    try:
        r=r
    except:
        r=0
    global clicked, exported
    
    p=8.33333333*df['Dato'][0]
    Ppg_RHOB=[p]
    Psi_Incr=[0]
    cum=8.6*0.052*df['Profundidad'][0]
    Psi_cum=[cum]
    Obg=[cum/(0.052*df['Profundidad'][0])]

    if modo=='Densidad (g/cc)':
    
        for n in range(1,(len(df))):
            b=8.33333333*df['Dato'][n]
            Ppg_RHOB.append(b)
        df["Ppg_RHOB"] = Ppg_RHOB

        for n in range(1,(len(df))):
            p=0.052*df["Ppg_RHOB"][n]*(df['Profundidad'][n]-df['Profundidad'][n-1])
            Psi_Incr.append(p)
        df["Psi_Incr"] = Psi_Incr

        for n in range(1,(len(df))):
            cum=cum+df["Psi_Incr"][n]
            Psi_cum.append(cum)
        df["Psi_cum"] = Psi_cum

        for n in range(1,(len(df))):
            obg_temp=df["Psi_cum"][n]/(0.052*df['Profundidad'][n])
            Obg.append(obg_temp)
        df["OBG"] = Obg

        #export values

        x=list(df['OBG'])
        y=list(df['Profundidad'])
        exported=np.polyfit(np.log(x), np.log(y), 1)
    
        #graph
        global figu,axon
        root.geometry('1300x750')
        figu, axon = plt.subplots(figsize=(6,7))
        x=list(df['OBG'])
        y=list(df['Profundidad'])
        axon.plot(x, y,color='blue', label='Overburden Gradient')
        axon.invert_yaxis()
        axon.set(xlabel='PPG', ylabel='Profundidad(ft)',
            title='Gradientes')
        axon.legend()
        axon.grid()
        axon.set_xlim(left=0)
        canvas = FigureCanvasTkAgg(figu, master=root)
        placer_button=Button(root,width=15).grid(column=4,row=5,pady=(50,0))
        canvas.get_tk_widget().grid(column=5,row=0)
        

    elif modo=='Resistividad':

        global fig
        r=r+1
        top=Toplevel()
        top.title('Resistividad Analisis')
        top.geometry('1300x1000')
        alfa_min = 1
        alfa_max = 2*df["Profundidad"].max()*df["Dato"].mean()
        beta_min = df["Profundidad"].max()
        beta_max = 2*df["Profundidad"].max()*df["Dato"].mean()
        fig, ax = plt.subplots(figsize=(7,9))
        x=list(df['Dato'])
        y=list(df['Profundidad'])
        ax.plot(x, y,color='red')

        ts = pd.Series(df['Dato'].values, index=df['Dato'])
        upper=ts.quantile(.9)
        lower=ts.quantile(.1)
        

        ax.set_xlim(-lower*2,upper*2)


        ax.set(xlabel='Resistividad '+str(r), ylabel='Profundidad(ft)',
            title='Resistividad Analisis')
        ax.grid()
        
        canvas2 = FigureCanvasTkAgg(fig, master=top)

        canvas2.get_tk_widget().grid(column=1,row=0)

        def a_resistividad(alfa,beta):
            
            Resistivity_Trendline=[(-beta+df['Profundidad'][0])/-alfa]
            exp_Trendline=[np.exp((np.log(df['Profundidad'][0])-exported[1])/exported[0])]
            eaton_result=[exp_Trendline[0]-((exp_Trendline[0]-8.6)*(df['Dato'][0]/Resistivity_Trendline[0])**1.2)]
            frac_gradient=[0.8*(exp_Trendline[0]-eaton_result[0])+eaton_result[0]]


            for n in range(1,(len(df))):

                expo=np.exp((np.log(df['Profundidad'][n])-exported[1])/exported[0])
                exp_Trendline.append(expo)


            for n in range(1,(len(df))):

                res_tl=(-beta+df['Profundidad'][n])/(-alfa)
                Resistivity_Trendline.append(res_tl)

            for n in range(1,(len(df))):

                eaton=exp_Trendline[n]-((exp_Trendline[n]-8.6)*(df['Dato'][n]/Resistivity_Trendline[n])**1.2)
                eaton_result.append(eaton)
            df['Pore Pressure Resistividad (RES'+str(r)+')']=eaton_result
            
            for n in range(1,(len(df))):

                frac=0.8*(exp_Trendline[n]-df['Pore Pressure Resistividad (RES'+str(r)+')'][n])+df['Pore Pressure Resistividad (RES'+str(r)+')'][n]
                frac_gradient.append(frac)
            df['Gradiente de Fractura (RES'+str(r)+')']=frac_gradient

            smoother=[]

            for n in range(1,(len(df))):
                smooth_temp=[df['Pore Pressure Resistividad (RES'+str(r)+')'][n],df['Profundidad'][n]]
                smoother.append(smooth_temp)
            
            a=np.array(smoother)
            x1, y1 = a.T
            t = np.linspace(0, 1, len(x1))
            t2 = np.linspace(0, 1, 100)

            x2 = np.interp(t2, t, x1)
            y2 = np.interp(t2, t, y1)
            sigma = 0.5
            x3 = gaussian_filter1d(x2, sigma)
            y3 = gaussian_filter1d(y2, sigma)

            x=list(x3)
            y=list(y3)
            axon.plot(x, y, label='Pore Pressure (RES'+str(r)+')')
            axon.legend()
            figu.canvas.draw()

            smoother=[]

            for n in range(1,(len(df))):
                smooth_temp=[df['Gradiente de Fractura (RES'+str(r)+')'][n],df['Profundidad'][n]]
                smoother.append(smooth_temp)
            
            a=np.array(smoother)
            x1, y1 = a.T
            t = np.linspace(0, 1, len(x1))
            t2 = np.linspace(0, 1, 100)

            x2 = np.interp(t2, t, x1)
            y2 = np.interp(t2, t, y1)
            sigma = 0.5
            x3 = gaussian_filter1d(x2, sigma)
            y3 = gaussian_filter1d(y2, sigma)

            x=list(x3)
            y=list(y3)

            axon.plot(x, y, label='Gradiente de Fractura (RES'+str(r)+')')
            axon.legend()
            figu.canvas.draw()
            top.destroy()

            df.drop(columns=['Trendline'])


    
        


        def module(x):
            global alfa, beta,line
            try:
                ax.lines[1].remove()
            except:
                'do nothing'
            line=[]
            alfa = float(alfa_slide.get())
            beta = float(beta_slide.get())
            for n in range(0,(len(df))):
                line_temp=beta-float(df["Dato"][n])*float(alfa)
                line.append(line_temp)
            df["Trendline"] = line
            ax.autoscale(enable=False,tight=None)
            
            ax.plot(list(df['Dato']),list(df['Trendline']),color='blue')
            fig.canvas.draw()
        
        calc_button_res=Button(top,text='Calcular',command=lambda:module(x),width = 30)
        aceptar_button=Button(top,text='Aceptar',command=lambda:a_resistividad(alfa,beta),width = 30)
        calc_button_res.grid(row=1,column=3)
        aceptar_button.grid(row=2,column=3)

        alfa_slide = DoubleVar()
        beta_slide = DoubleVar()
        output_message_text = StringVar()

        ds = Scale(top, variable = alfa_slide, from_ = alfa_min, to = alfa_max,length=600)
        ds.grid(column = 0, row = 0)

        o_s = Scale(top, variable = beta_slide, from_ = beta_min, to = beta_max,length=600)
        o_s.grid(column = 2, row = 0)
    
    elif modo=='Sonico': #se necesita mas informacion para poder corroborar la forma en la que se calcula la trendline

        top=Toplevel()
        top.title('Analisis Sonico')
        top.geometry('1300x1000')
        alfa_min = 1
        alfa_max = 20000
        beta_min = df["Profundidad"].max()
        beta_max = 20000
        fig, ax = plt.subplots(figsize=(7,9))
        x=list(df['Dato'])
        y=list(df['Profundidad'])
        ax.plot(x, y,color='red')

        ts = pd.Series(df['Dato'].values, index=df['Dato'])
        upper=ts.quantile(.9)
        lower=ts.quantile(.1)
        

        ax.set_xlim(-lower*2,upper*2)


        ax.set(xlabel='Delta tiempo', ylabel='Profundidad(ft)',
            title='Analisis Sonico')
        ax.grid()
        
        canvas = FigureCanvasTkAgg(fig, master=top)

        canvas.get_tk_widget().grid(column=1,row=0)

        def a_sonico(alfa,beta):

            Sonic_Trendline=[(-beta+df['Profundidad'][0])/-alfa]
            exp_Trendline=[np.exp((np.log(df['Profundidad'][0])-exported[1])/exported[0])]
            Sonic_result=[exp_Trendline[0]-(exp_Trendline[0]-8.6)*((Sonic_Trendline[0]/df['Dato'][0])**3)]


            for n in range(1,(len(df))):

                expo=np.exp((np.log(df['Profundidad'][n])-exported[1])/exported[0])
                exp_Trendline.append(expo)


            for n in range(1,(len(df))):

                sonic_tl=(-beta+df['Profundidad'][n])/(-alfa)
                Sonic_Trendline.append(sonic_tl)

            for n in range(1,(len(df))):

                Sonic=exp_Trendline[n]-(exp_Trendline[n]-8.6)*((Sonic_Trendline[n]/df['Dato'][n])**3)
                Sonic_result.append(Sonic)
            df['Pore Pressure Sonico']=Sonic_result


            x=list(df['Pore Pressure Sonico'])
            y=list(df['Profundidad'])
            axon.plot(x, y, label='Presion Poral (SON1)')
            figu.canvas.draw()
            axon.legend()
            top.destroy()
            df.drop(columns=['Trendline'])
    
        


        def module(x):
            global alfa, beta,line
            try:
                ax.lines[1].remove()
            except:
                'do nothing'
            line=[]
            alfa = float(alfa_slide.get())
            beta = float(beta_slide.get())
            for n in range(0,(len(df))):
                line_temp=beta-float(df["Dato"][n])*float(alfa)
                line.append(line_temp)
            df["Trendline"] = line
            ax.autoscale(enable=False,tight=None)
            
            ax.plot(list(df['Dato']),list(df['Trendline']),color='blue')
            fig.canvas.draw()
            
        aceptar_button=Button(top,text='Aceptar',command=lambda:a_sonico(alfa,beta),width = 30)
        aceptar_button.grid(row=1,column=3)

        alfa_slide = DoubleVar()
        beta_slide = DoubleVar()
        output_message_text = StringVar()

        ds = Scale(top, variable = alfa_slide, from_ = alfa_min, to = alfa_max,length=600)
        ds.grid(column = 0, row = 0)

        o_s = Scale(top, variable = beta_slide, from_ = beta_min, to = beta_max,length=600)
        o_s.grid(column = 2, row = 0)

    elif modo=='Sismica':

        x=list(df['Dato'])
        y=list(df['Profundidad'])
        exp_sism=np.polyfit(np.log(x), np.log(y), 1)

        Sism_Trendline=[np.exp((np.log(df['Profundidad'][0])-exp_sism[1])/exp_sism[0])]
        exp_Trendline=[np.exp((np.log(df['Profundidad'][0])-exported[1])/exported[0])]
        Sism_result=[exp_Trendline[0]-(exp_Trendline[0]-8.6)*((Sism_Trendline[0]/df['Dato'][0])**3)]

        for n in range(1,(len(df))):

            expo=np.exp((np.log(df['Profundidad'][n])-exported[1])/exported[0])
            exp_Trendline.append(expo)

        for n in range(1,(len(df))):

            sism_tl=np.exp((np.log(df['Profundidad'][n])-exp_sism[1])/exp_sism[0])
            Sism_Trendline.append(sism_tl)

        for n in range(1,(len(df))):

            Sismic=exp_Trendline[n]-(exp_Trendline[n]-8.6)*((Sism_Trendline[n]/df['Dato'][n])**3)
            Sism_result.append(Sismic)
        df['Pore Pressure Sismica']=Sism_result


        x=list(df['Pore Pressure Sismica'])
        y=list(df['Profundidad'])
        axon.plot(x, y, label='Presion Poral (SIS1)')
        axon.legend()
        figu.canvas.draw()

    elif modo=='Datos Puntuales':
        top=Toplevel()
        top.title('Datos Puntuales')
        top.geometry('1300x1000')
        frame_LOT=Frame(top, text='Leak-off Tests')
        frame_LOT.grid(column=0,row=0)
        L1=Label(frame_LOT, text='Profundidad').grid(column=0,row=0)
        L2=Label(frame_LOT, text='PPG').grid(column=1,row=0)
        entry_LOT_1=Entry(frame_LOT,width=20).grid(column=0,row=1)
        entry_LOT_2=Entry(frame_LOT,width=20).grid(column=1,row=1)

curvas=StringVar()
drop_curvas=OptionMenu(root,curvas,'Densidad (g/cc)','Sonico','Resistividad','Sismica','Datos Puntuales',command=lambda _:enabler_select())
drop_curvas.grid(row=1,column=0)
drop_curvas.config(width=16)
select_button=Button(root,text='Importar',command=importar,width = 20,state=DISABLED).grid(row=1,column=1)
calc_button=Button(root,text='Calcular',command=lambda:calcular(curvas.get()),width = 20,state=DISABLED).grid(row=1,column=2)
mainloop()