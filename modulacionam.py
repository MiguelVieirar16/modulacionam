from tkinter import*
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy import signal
import numpy as np


#fondo y Texto que va en las ventanas
root = tk.Tk()
root.geometry("1400x720+60+20")
root.title("GENERADOR DE SEÑALES :)")
root.resizable(False, False)
root.configure(bg='#003152')

#creacion de la ventana
texto = Label(root, text="GENERADOR DE SEÑALES Y MODULADOR", font=('Comic Sans Ms', 18, 'bold'), fg="white", bg="#003152") 
texto.place(x=280, y=20)

#cuadro donde se mostrara todo
datos = LabelFrame(root, width=1000, height=120, text="  DATOS"+"🗒️", font=('Comic Sans Ms', 14, 'bold'), fg="white", bg="#003152", border=5)
datos.place(x=100, y=80)

#zona donde seleccionamos el tipo de Onda (Señal portadora)
señal = Label(datos, text="Seleccione la señal portadora:", font=('Comic Sans Ms', 12), fg="white", bg="#003152")
señal.place(x=20, y=15)
combo = ttk.Combobox(datos, state="readonly", values=["SINUSOIDAL","CUADRADA","DIENTE DE SIERRA"], font=('Comic Sans Ms', 12), width=20, height=25)
combo.place(x=20, y=40)

#calidar la amplitud ingresada
def valida_amp(a_str):
    if a_str.isdigit() or a_str == "":
        return True
    else:
        return False

# Zona donde ingresaremos el valor de AMPLITUD.
amp0 = Label(datos, text="Ingrese la AMPLITUD:", font=('Comic Sans Ms', 12), fg="white", bg="#003152")
amp0.place(x=270, y=15)
amp = Entry(datos, width=10, validate="key", validatecommand=(datos.register(valida_amp), '%P'), font=('Comic Sans Ms', 12))
amp.place(x=270, y=40)
combo1 = ttk.Combobox(datos, state="readonly", values=["V"], font=('Comic Sans Ms', 12), width=5, height=25)
combo1.place(x=380, y=40)
combo1.current(0)

#validar la frecuencia ingresada
def valida_fre(frecuencia_str):
    if frecuencia_str.isdigit() or frecuencia_str == "":
        return True
    else: 
        return False

#zona donde ingresaremos el valor de FRECUENCIA
frc0 = Label(datos, text="Ingrese la FRECUENCIA:", font=('Comic Sans Ms', 12), fg="white", bg="#003152")
frc0.place(x=480, y=15)
frc = Entry(datos, width=10, validate="key", validatecommand=(datos.register(valida_fre), '%P'), font=('Comic Sans Ms', 12))
frc.place(x=480, y=40)
combo2 = ttk.Combobox(datos, state="readonly", values=["Hz"], font=('Comic Sans Ms', 12), width=5, height=25)
combo2.place(x=590, y=40)
combo2.current(0)

#zona donde seleccionamos el tipo de modulación
mod = Label(datos, text="Seleccione el tipo de modulación:", font=('Comic Sans Ms', 12), fg="white", bg="#003152")
mod.place(x=700, y=15)
combo3 = ttk.Combobox(datos, state="readonly", values=["AM"], font=('Comic Sans Ms', 12), width=22, height=25)
combo3.place(x=700, y=40)
combo3.current(0)

#variables a usar
A_sm = 5 #Amplitud de la moduladora
f_sm = 4000 #Frecuencia de la moduladora
t_s = np.linspace(0,1,1000) #Vector de tiempo
t= np.linspace(0,1,1000, endpoint=True) #Vector de tiempo
ka = 2 #Índice de modulación

#creamos un cuadro donde se colocara las gráficas (señal portadora, mensaje y modulacion)
grafica = LabelFrame(root, width=1140, height=490, text="  GRÁFICA"+"📉", font=('Comic Sans Ms', 14, 'bold'), fg="white", bg="#003152", border=5)
grafica.place(x=40, y=210)

#metodo donde se generara la grafica de la señal mensaje
def mensajee():
    mensaje = A_sm*np.cos(2*np.pi*f_sm*t_s)
    fig = Figure(figsize=(10,3.5))
    fig.add_subplot().plot(mensaje)
    grafica_mensaje = LabelFrame(grafica, width=1080, height=420, bg="white", border=5)
    grafica_mensaje.place(x=25, y=10)
    
    canvas = FigureCanvasTkAgg(fig, master=grafica_mensaje)
    canvas.draw()
    canvas.get_tk_widget().place(x=5, y=40)

    mensaje1 = Label(grafica_mensaje, text="SEÑAL MENSAJE O MODULADORA", font=('Comic Sans Ms', 14)).place(x=340,y=20)

def graficar_seno():
    frecuencia_str = frc.get()
    a_str = amp.get()
    
    if frecuencia_str == '' or a_str == '':
        tk.messagebox.showerror('Error', 'Para mostrar la onda, debe ingresar una frecuencia y una Amplitud')
        return
                   
    #frecuencia de la portadora (SINUSOIDAL)
    f_sp = float(frecuencia_str)
    
    #amplitud de la portadora (SINUSOIDAL)
    A_sp = float(a_str)

    portadora = A_sp*np.cos(2*np.pi*f_sp*t_s)                         
    fig = Figure(figsize=(10,3.5))
    fig.add_subplot(111).plot(portadora)
    grafica_señal1 = LabelFrame(grafica, width=1080, height=420, bg="white", border=5)
    grafica_señal1.place(x=25, y=10)

    canvas = FigureCanvasTkAgg(fig, master=grafica_señal1)
    canvas.draw()
    canvas.get_tk_widget().place(x=5, y=40)

    señal1 = Label(grafica_señal1, text=f"SEÑAL PORTADORA {combo.get()}", font=('Comic Sans Ms', 14)).place(x=340,y=20)

def graficar_cuadrada():
    frecuencia_str = frc.get()
    a_str = amp.get()

    if frecuencia_str == '' or a_str == '':
        tk.messagebox.showerror('Error', 'Para mostrar la onda, debe ingresar una frecuencia y una Amplitud')
        return
    
    #frecuencia de la portadora (CUADRADA)
    f_sc = float(frecuencia_str)
    
    #amplitud de la portadora (CUADRADA)
    A_sc = float(a_str)

    cuadrada = A_sc*signal.square(2 * np.pi * f_sc * t)
    fig = Figure(figsize=(10,3.5))
    fig.add_subplot(111).plot(cuadrada)
    grafica_cuadrada1 = LabelFrame(grafica, width=1080, height=420, bg="white", border=5)
    grafica_cuadrada1.place(x=25, y=10)

    canvas = FigureCanvasTkAgg(fig, master=grafica_cuadrada1)
    canvas.draw()
    canvas.get_tk_widget().place(x=5, y=40)

    señal2 = Label(grafica_cuadrada1, text=f"SEÑAL PORTADORA {combo.get()}", font=('Comic Sans Ms', 14)).place(x=340,y=20)

def graficar_sierra():
    frecuencia_str = frc.get()
    a_str = amp.get()

    if frecuencia_str == '' or a_str == '':
        tk.messagebox.showerror('Error', 'Para mostrar la onda, debe ingresar una frecuencia y una Amplitud')
        return
    
    #frecuencia de la portadora (DIENTE DE SIERRA)
    f_ds = float(frecuencia_str)

    #amplitud de la portadora (DIENTE DE SIERRA)
    A_ds = float(a_str)

    diente_sierra = A_ds*signal.sawtooth(2 * np.pi * f_ds * t)
    fig = Figure(figsize=(10,3.5))
    fig.add_subplot(111).plot(diente_sierra)
    grafica_ds1 = LabelFrame(grafica, width=1080, height=420, bg="white", border=5)
    grafica_ds1.place(x=25, y=10)

    canvas = FigureCanvasTkAgg(fig, master=grafica_ds1)
    canvas.draw()
    canvas.get_tk_widget().place(x=5, y=40)

    señal3 = Label(grafica_ds1, text=f"SEÑAL PORTADORA {combo.get()}", font=('Comic Sans Ms', 14)).place(x=340,y=20)


#metodo donde se generara la grafica de la señal portadora
def graficaa():
    comb = combo.get()
    comb1 = combo1.get()
    comb2 = combo2.get()

    if (comb == "SINUSOIDAL") or (comb == "CUADRADA") or (comb == "DIENTE DE SIERRA"):
       
        #se escogio la señal sinusoidal
        if (comb == "SINUSOIDAL"):
            if (comb1 == "V"):
                if (comb2 == "Hz"):
                    graficar_seno()
                else:
                    messagebox.showinfo(message= "Por favor, ingrese ingrese una frecuencia :)", title="Aviso")
            else:
                messagebox.showinfo(message= "Por favor, ingrese una amplitud :)", title="Aviso")

        #se escogio la señal cuadrada
        if (comb == "CUADRADA"):
            if (comb1 == "V"):
                if (comb2 == "Hz"):
                    graficar_cuadrada()
                else:
                    messagebox.showinfo(message= "Por favor, ingrese una frecuencia :)", title="Aviso")
            else:
                messagebox.showinfo(message= "Por favor, ingrese una amplitud :)", title="Aviso")

        #se escogio la señal diente de sierra
        if (comb == "DIENTE DE SIERRA"):
            if (comb1 == "V"):
                if (comb2 == "Hz"):
                    graficar_sierra()
                else:
                    messagebox.showinfo(message= "Por favor, ingrese una frecuencia", title="Aviso")
            else:
                messagebox.showinfo(message= "Por favor, ingrese una amplitud", title="Aviso")
    else: 
        messagebox.showinfo(message= "Por favor, ingrese el tipo de señal portadora", title="Aviso")

#metodo donde se generara la grafica de la modulacion AM

def modulacion():
    comb3 = combo3.get()
    comb1 = combo1.get()
    comb2 = combo2.get()
    if (comb3 == "AM"): 
            if (comb1 == "V"):
                if (comb2 == "Hz"):
                    frecuencia_str = frc.get()
                    a_str = amp.get()

                    if frecuencia_str == '' or a_str == '':
                        tk.messagebox.showerror('Error', 'Para mostrar la onda, debe ingresar una frecuencia y una Amplitud')
                        return
                    
                    # Frecuencia de la portadora.
                    f_sp = float(frecuencia_str)

                    # Amplitud de la portadora.
                    A_sp = float(a_str)

                    if A_sp == 0:
                        tk.messagebox.showerror('Error', 'La amplitud debe ser mayor que 0')
                        return
                    
                    modulacion_AM = (1+(A_sm/A_sp)*np.cos(2*np.cos(2*np.pi*f_sm*t_s)))*A_sp*np.cos(2*np.pi*f_sp*t_s)
                    fig = Figure(figsize=(10.5,3.5))
                    fig.add_subplot().plot(modulacion_AM)
                    grafica_modulacion = LabelFrame(grafica, width=1080, height=420, bg="white", border=5)
                    grafica_modulacion.place(x=25, y=10)
                                
                    canvas = FigureCanvasTkAgg(fig, master=grafica_modulacion)
                    canvas.draw()
                    canvas.get_tk_widget().place(x=2,y=40)

                    mod1= Label(grafica_modulacion, text=f"MODULACIÓN {combo3.get()}", font=('Comic Sans Ms', 14)).place(x=440,y=20)
                else:
                    messagebox.showinfo(message= "Por favor, ingrese una frecuencia :)", title="Aviso")
            else:
                messagebox.showinfo(message= "Por favor, ingrese una Amplitud :)", title="Aviso")
    else:
        messagebox.showinfo(message= "Por favor, ingrese el tipo de modulación :)", title="Aviso")

#metodo donde se generara la grafica de la comparacion
def comparar():
    comb = combo.get()
    comb1 = combo1.get()
    comb2 = combo2.get()
    comb3 = combo3.get()

    if (comb == "SINUSOIDAL") or (comb == "CUADRADA") or (comb == "DIENTE DE SIERRA"):
            if (comb1 == "V"):
                if (comb2 == "Hz"):
                    if (comb3 == "AM"):
                        frecuencia_str = frc.get()
                        a_str = amp.get()

                        #frecuencia de la portadora (SINUSOIDAL)
                        f_sp = float(frecuencia_str) 

                        #amplitud de la portadora (SINUSOIDAL)
                        A_sp = float(a_str) 

                        #señal mensaje o moduladora
                        mensaje = A_sm*np.cos(2*np.pi*f_sm*t_s) 

                        #señal portadora (Sinusoidal, Cuadrada y Diente de sierra)
                        portadora = A_sp*np.cos(2*np.pi*f_sp*t_s)
                        cuadrada = A_sp*signal.square(2 * np.pi * f_sp * t)
                        diente_sierra = A_sp*signal.sawtooth(2 * np.pi * f_sp * t)

                        #modulacion AM 
                        modulacion_AM = A_sp*(1+ka*np.cos(2*np.cos(2*np.pi*f_sm*t_s))*np.cos(2*np.pi*f_sp*t_s))    

                        plt.clf()
                        
                        #imprimimos en pantalla la señal mensaje o moduladora
                        plt.subplot(5,1,1)
                        plt.title('Señal de Mensaje o Moduladora')
                        plt.plot(mensaje,'b')
                        plt.ylabel('Amplitud')

                        #imprimimos en pantalla la señal portadora (SINUSOIDAL)
                        plt.subplot(5,1,2)
                        plt.title('Señal de Portadora (Sinusoidal)')
                        plt.plot(portadora,'r')
                        plt.ylabel('Amplitud')

                        #imprimimos en pantalla la señal portadora (CUADRADA)
                        plt.subplot(5,1,3)
                        plt.title('Señal de Portadora (Cuadrada)')
                        plt.plot(cuadrada,'k')
                        plt.ylabel('Amplitud')

                        #imprimimos en pantalla la señal portadora (DIENTE DE SIERRA)
                        plt.subplot(5,1,4)
                        plt.title('Señal de Portadora (Diente de sierra)')
                        plt.plot(diente_sierra,'g')
                        plt.ylabel('Amplitud')
                    
                        #imprimimos en pantalla la modulacion AM.
                        plt.subplot(5,1,5)
                        plt.title('Modulacion AM')
                        plt.plot(modulacion_AM, color="purple")
                        plt.ylabel('Amplitud')

                        plt.show()
                    else:
                        messagebox.showinfo(message= "Por favor, ingrese el tipo de modulación", title="Aviso")
                else:
                    messagebox.showinfo(message= "Por favor, ingrese la frecuencia", title="Aviso")
            else:
                messagebox.showinfo(message= "Por favor, ingrese la amplitud", title="Aviso")
    else:
        messagebox.showinfo(message= "Por favor, ingrese el tipo de señal portadora", title="Aviso")

#botones para graficar la señal deseada con los datos ingresados y realizar la comparacion
button0 = tk.Button(root, text="Mensaje", font=('Comic Sans Ms', 12), fg="#151E3D", bg="#87CDEE", width=10, height=2, command=mensajee)
button0.place(x=1220, y=280)
button1 = tk.Button(root, text="Graficar", font=('Comic Sans Ms', 12), fg="#151E3D", bg="#57A0D3", width=10, height=2, command=graficaa)
button1.place(x=1220, y=380)
button2 = tk.Button(root, text="Modulación", font=('Comic Sans Ms', 12), fg="#151E3D", bg="#3E8EDE", width=10, height=2, command=modulacion)
button2.place(x=1220, y=480)
button3 = tk.Button(root, text="Comparar", font=('Comic Sans Ms', 12), fg="#151E3D", bg="#0073CF", width=10, height=2, command=comparar)
button3.place(x=1220, y=580)


root.mainloop()