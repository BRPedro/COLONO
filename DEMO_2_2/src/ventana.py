# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: cp1252 -*-
__author__ = "PBR"
__date__ = "$11/10/2016 09:37:00 AM$"

# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2
from imagenes import *

class Ventana:
    def __init__(self):
        self.contadorE,self.contadorP=0,0
        self.filtro=0
        self.inicio = Tk()
        self.imagelista = listaImagens()
        self.direccionString = ""
        self.listaL = ["", ""]

        self.altura=0
        self.tipoBanda=0
        self.coodenadas=[]
        self.tiempoV=0
        
        self.inicio.title("Calculadora")
        self.inicio.geometry("1000x700")
        self.inicio.configure(background='white')

        self.cargadoV=Toplevel(self.inicio)
        self.cargadoV.title("Cargado")
        self.cargadoV.withdraw()


        # **************************Logo y titulo**********************************************
        self.fCabeza = Frame(self.inicio, bg='white')
        self.fCabeza.grid(column=0, row=0)
        self.logo = ImageTk.PhotoImage(Image.open("imagenesInterfaz\\principal\\colonoImg.png"))
        self.lLogo = Label(self.fCabeza, image=self.logo, bg="light sea green").grid(row=0, column=0)
        self.lTitulo = Label(self.fCabeza, text="                                                        CALCULADORA", bg='white',
                        font=("Helvetica", 18)).grid(row=0, column=1)

        # **************************Logo y titulo**********************************************
        self.fImagen = Frame(self.inicio)
        self.fImagen.grid(column=0, row=1)
        self.cul = self.imagelista.lista[0]
        self.listaL[0] = Label(self.fImagen, image=self.cul, bg="light sea green")
        self.listaL[0].config()
        self.listaL[0].grid(row=0, column=0)

        self.listaL[1] = Label(self.fImagen, image=self.cul, bg="light sea green")
        self.listaL[1].config()
        self.listaL[1].grid(row=0, column=1)
        
        self.fResultado = Frame(self.inicio)
        self.fResultado.grid(column=0, row=2)
        self.jlabel1=Label(self.fResultado,text="Resultado:",width=22).grid(row=0,column=0)
        self.j2=StringVar()
        self.jlabel1=Label(self.fResultado,textvariable=self.j2,width=22).grid(row=0,column=1)
        
        

        self.fBotones = Frame(self.inicio)
        self.fBotones.grid(column=0, row=3)
        self.bCargar = Button(self.fBotones, text="Cargar", command=lambda: self.direccion(), bg="green", width=18).grid(row=0, column=0)
        self.bMyFiltro = Button(self.fBotones, text="Contar", command=lambda: self.filtro_Contar(), bg="yellow green", width=18).grid( row=0, column=1)

        self.menu1 = Menu(self.inicio)
        self.inicio.config(menu=self.menu1)
        self.menu1_1 = Menu(self.menu1, tearoff=0)
        self.menu1.add_cascade(label="Archivo", menu=self.menu1_1)
        self.menu1_1.add_command(label="Cargar",command=lambda: self.prueba())
        self.menu1_1.add_cascade(label="Guardar",command=lambda: self.prueba())

        self.menu1_2 = Menu(self.menu1, tearoff=0)
        self.menu1.add_cascade(label="Ajustes",command=lambda: self.prueba())


        """Ventana de Cragado"""


        self.inicio.mainloop()

    def mostrarOcultar(self,ver,ocultar):#Mostrar ventana registro y ocultar la de inicio
        ocultar.withdraw()
        ver.deiconify()
        
    def ajustar(self, dir, bandera):
        imag = cv2.imread(dir)
        nombre = ""
        if bandera:
            nombre = "tem1.jpg"
        else:
            nombre = "tem2.jpg"
        res = cv2.resize(imag, (500, 500), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(nombre, res)
        return nombre


    def cargarImagen(self,dire):
        imagens = PhotoImage(file=dire)
        return imagens


    def direccion(self):
        self.direccionString = askopenfilename()
        dirtem = self.ajustar(self.direccionString, True)

        self.imagelista.lista[1] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[1]
        self.listaL[0].config(image=l)


        
    def filtro_Contar(self):
        return

    def iniciarConteo(self):
        return

    def prueba(self):
        print "Hola Mundo"
        

        

