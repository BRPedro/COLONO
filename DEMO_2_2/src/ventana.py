# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
__author__ = "PBR"
__date__ = "$11/10/2016 09:37:00 AM$"

# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2
from imagenes import *
import threading
import time

class Ventana:
    def __init__(self):
        self.contadorE,self.contadorP=0,0
        self.filtro=0
        self.inicio = Tk()
        self.imagelista = listaImagens()
        self.direccionString = ""
        self.listaL = ["", ""]
        self.imagenReal=0

        self.altura=0
        self.tipoBanda=0
        self.coodenadas=[0.0,0.0]
        self.tiempoV=0
        self.fila=0
        self.columna=0
        self.tipo=0
        self.escala=0.0
        self.ajuste=0.0
        self.circulo=0
        
        self.inicio.title("Calculadora")
        self.inicio.geometry("1000x700")
        self.inicio.configure(background='white')

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
        self.listaL[0] = Label(self.fImagen, image=self.cul, bg='white')
        self.listaL[0].config()
        self.listaL[0].grid(row=0, column=0)

        self.listaL[1] = Label(self.fImagen, image=self.cul, bg='white')
        self.listaL[1].config()
        self.listaL[1].grid(row=0, column=1)
        
        self.fResultado = Frame(self.inicio)
        self.fResultado.grid(column=0, row=2)
        self.jlabel1=Label(self.fResultado,text="Resultado:",bg='white',width=22).grid(row=0,column=0)
        self.j2=StringVar()
        self.jlabel1=Label(self.fResultado,textvariable=self.j2,bg='white',width=22).grid(row=0,column=1)
        
        

        self.fBotones = Frame(self.inicio)
        self.fBotones.grid(column=0, row=3)
        self.bCargar = Button(self.fBotones, text="Cargar", command=lambda: self.direccion(), bg="green", width=18).grid(row=0, column=0)
        self.bMyFiltro = Button(self.fBotones, text="Contar", command=lambda: self.filtro_Contar(), bg="yellow green", width=18).grid( row=0, column=1)

        self.menu1 = Menu(self.inicio)
        self.inicio.config(menu=self.menu1)
        self.menu1_1 = Menu(self.menu1, tearoff=0)
        self.menu1.add_cascade(label="Archivo", menu=self.menu1_1)
        self.menu1_1.add_command(label="Cargar",command=lambda: self.mostrarOcultar(self.cargadoV,self.inicio))
        self.menu1_1.add_cascade(label="Guardar",command=lambda: self.mostrarOcultar(self.ajusteV,self.inicio))

        self.menu1_2 = Menu(self.menu1, tearoff=0)
        self.menu1.add_cascade(label="Ajustes",command=lambda: self.mostrarOcultar(self.ajusteV,self.inicio))


        """******************************Ventana de Cargado******************************"""
        self.cargadoV=Toplevel(self.inicio)
        self.cargadoV.title("Cargado")
        self.cargadoV.configure(background='white')

        #---------------Frame de sector de imagen---------------
        self.frameImgCargadoCV=Frame(self.cargadoV, bg='white')
        self.frameImgCargadoCV.grid(column=0, row=0)

        self.imagCargado = self.imagelista.lista[1]
        self.lCVimagen = Label(self.frameImgCargadoCV, image=self.imagCargado, bg='white')
        self.lCVimagen.config()
        self.lCVimagen.grid(row=0, column=0)
        self.bCVcargado = Button(self.frameImgCargadoCV, text="Seleccionar", command=lambda: self.seleccionarImagen(), bg="yellow green", width=18).grid( row=1, column=0)

        #---------------Frame de sector de Labels---------------
        self.framelabelCV=Frame(self.cargadoV, bg='white')
        self.framelabelCV.grid(column=0, row=1)

        self.lResoluccionCV=Label(self.framelabelCV,text="Resolucio:",bg='white',width=10).grid(row=0,column=0)
        self.textResolucionCV=StringVar()
        self.textResolucionCV.set(str(self.fila)+" x "+str(self.columna))
        self.textBoxResolucionCV=Label(self.framelabelCV,textvariable=self.textResolucionCV,bg='white',width=20).grid(row=0,column=1)

        self.lTamannoCV=Label(self.framelabelCV,text="Tamanno:",bg='white',width=10).grid(row=1,column=0)
        self.textTamnnoCV=StringVar()
        self.textTamnnoCV.set(str(self.fila*self.columna))
        self.textBoxTamnnoCV=Label(self.framelabelCV,textvariable=self.textTamnnoCV,bg='white',width=20).grid(row=1,column=1)

        self.lCoordenadasCV=Label(self.framelabelCV,text="Coordenadas:",bg='white',width=10).grid(row=2,column=0)
        self.textLatitudCV=StringVar()
        self.textLongitudCV=StringVar()
        self.textLatitudCV.set(str(self.coodenadas[0]))
        self.textLongitudCV.set(str(self.coodenadas[1]))
        self.frameCoordenadasCV=Frame(self.framelabelCV, bg='white')
        self.frameCoordenadasCV.grid(row=2,column=1)
        self.textBoxTamnnoCV=Entry(self.frameCoordenadasCV,textvariable=self.textLatitudCV,bg='white',width=5).grid(row=0,column=0)
        self.textBoxTamnnoCV=Entry(self.frameCoordenadasCV,textvariable=self.textLongitudCV,bg='white',width=5).grid(row=0,column=1)

        self.lTipoCV=Label(self.framelabelCV,text="Tipo:",bg='white',width=10).grid(row=3,column=0)
        self.textboxTipoCV = StringVar()
        self.comboboxTipoCV = ttk.Combobox(self.framelabelCV, textvariable=self.textboxTipoCV,
                                state='readonly')
        self.comboboxTipoCV['values'] = ('RGB', '###', '###')
        self.comboboxTipoCV.current(0)
        self.comboboxTipoCV.grid(row=3,column=1)

        self.lAlturaCV=Label(self.framelabelCV,text="Altura de vuelo:",bg='white',width=15).grid(row=4,column=0)
        self.eAlturaCV=Entry(self.framelabelCV,text="15",font=("Helvetica", 13),fg="black", bg='white').grid(row=4,column=1)


        self.lEscalCV=Label(self.framelabelCV,text="Escala pixeles:",width=15).grid(row=5,column=0)
        self.eEscalaCV=Entry(self.framelabelCV,text="1",font=("Helvetica", 13),fg="black", bg='white').grid(row=5,column=1)


        #---------------Frame de sector de Botones---------------
        self.frameBoteonesCV=Frame(self.cargadoV, bg='white')
        self.frameBoteonesCV.grid(column=0, row=2 )

        self.bAceptarCV = Button(self.frameBoteonesCV, text="Aceptar", command=lambda: self.botonAceptar(0), bg="yellow green", width=18).grid( row=0, column=0)
        self.bCancelarCV = Button(self.frameBoteonesCV, text="Cancelar", command=lambda: self.botonCancelar(0), bg="yellow green", width=18).grid( row=0, column=1)

        #-----------------------------------------------------------

        """******************************Ventana de Cargado******************************"""
        self.ajusteV=Toplevel(self.inicio)
        self.ajusteV.title("Ajuste")
        self.ajusteV.configure(background='white')

        self.framelabeAV=Frame(self.ajusteV, bg='white')
        self.framelabeAV.grid(column=0, row=0)

        self.lAlturaAV=Label(self.framelabeAV,text="Altura de vuelo:",bg='white',width=15).grid(row=0,column=0)
        self.textVariableAlturaAV=StringVar()
        self.textVariableAlturaAV.set(str(self.altura))
        self.textBoxAlturaAV=Entry(self.framelabeAV,textvariable=self.textVariableAlturaAV,bg='white',width=5).grid(row=0,column=1)

        self.lEscalaAV=Label(self.framelabeAV,text="Escala pxm:",bg='white',width=15).grid(row=1,column=0)
        self.textVariableEscalaAV=StringVar()
        self.textVariableEscalaAV.set(str(self.escala))
        self.textBoxAlturaAV=Entry(self.framelabeAV,textvariable=self.textVariableEscalaAV,bg='white',width=5).grid(row=1,column=1)

        self.lFiltradoAV=Label(self.framelabeAV,text="Filtrado de ruido:",bg='white',width=15).grid(row=2,column=0)
        self.textVariableFiltradoAV=StringVar()
        self.textVariableFiltradoAV.set(str(self.filtro))
        self.textBoxAlturaAV=Entry(self.framelabeAV,textvariable=self.textVariableFiltradoAV,bg='white',width=5).grid(row=2,column=1)

        self.lAjusteAV=Label(self.framelabeAV,text="Ajuste de proximidad:",bg='white',width=15).grid(row=3,column=0)
        self.textVariableAjusteAV=StringVar()
        self.textVariableAjusteAV.set(str(self.ajuste))
        self.textBoxAlturaAV=Entry(self.framelabeAV,textvariable=self.textVariableAjusteAV,bg='white',width=5).grid(row=3,column=1)

        self.lcirculoAV=Label(self.framelabeAV,text="Tamanno Circulo:",bg='white',width=15).grid(row=4,column=0)
        self.textVariableCirculoAV=StringVar()
        self.textVariableCirculoAV.set(str(self.circulo))
        self.textBoxCirculoAV=Entry(self.framelabeAV,textvariable=self.textVariableCirculoAV,bg='white',width=5).grid(row=4,column=1)

        self.lCoordenadasAV=Label(self.framelabeAV,text="Coordenadas:",bg='white',width=10).grid(row=5,column=0)
        self.textVariableLatitudAV=StringVar()
        self.textVariableLongitudAV=StringVar()
        self.textVariableLatitudAV.set(str(self.coodenadas[0]))
        self.textVariableLongitudAV.set(str(self.coodenadas[1]))
        self.frameCoordenadasAV=Frame(self.framelabeAV, bg='white')
        self.frameCoordenadasAV.grid(row=5,column=1)
        self.textBoxTamnnoCV=Entry(self.frameCoordenadasAV,textvariable=self.textVariableLatitudAV,bg='white',width=5).grid(row=0,column=0)
        self.textBoxTamnnoCV=Entry(self.frameCoordenadasAV,textvariable=self.textVariableLongitudAV,bg='white',width=5).grid(row=0,column=1)

        self.textVariableErrorAV=StringVar()
        self.textVariableErrorAV.set("     ")
        self.errorAV=Label(self.framelabeAV,textvariable=self.textVariableErrorAV,bg='white',width=10, ).grid(row=6,column=0)

        self.frameBoteonesAV=Frame(self.ajusteV, bg='white')
        self.frameBoteonesAV.grid(column=0, row=1)

        self.bAceptarCV = Button(self.frameBoteonesAV, text="Aceptar", command=lambda: self.botonAceptar(1), bg="yellow green", width=18).grid( row=0, column=0)
        self.bCancelarCV = Button(self.frameBoteonesAV, text="Cancelar", command=lambda: self.botonCancelar(1), bg="yellow green", width=18).grid( row=0, column=1)

        #-----------------------------------------------------------
        self.ajusteV.withdraw()
        self.cargadoV.withdraw()
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

    def ajustar2(self):
        f,c,t=self.imagen.shape
        imag=self.imagen
        if f>400:
            porcen=(400.0*100.0/f)/100.0
            imag=cv2.resize(imag, (int(c*porcen),int(f*porcen)), interpolation=cv2.INTER_CUBIC)
        f,c,t=imag.shape
        if c>400:
            porcen=(400.0*100.0/c)/100.0
            imag=cv2.resize(imag, (int(c*porcen),int(f*porcen)), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("imagenesInterfaz\\principal\\ajustar.jpg", imag)
        return "imagenesInterfaz\\principal\\ajustar.jpg"



    def cargarImagen(self,dire):
        imagens = PhotoImage(file=dire)
        return imagens


    def direccion(self):
        self.direccionString = askopenfilename()
        dirtem = self.ajustar(self.direccionString, True)

        self.imagelista.lista[1] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[1]
        self.listaL[0].config(image=l)

    def seleccionarImagen(self):
        self.direccionString = askopenfilename()

        self.imagen=cv2.imread(self.direccionString)
        self.fila,self.columna,self.tipo =self.imagen.shape
        dirtem = self.ajustar2()
        self.imagelista.lista[1] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[1]
        self.listaL[0].config(image=l)
        self.lCVimagen.config(image=l)
        self.textResolucionCV.set(str(self.fila)+" x "+str(self.columna))
        self.textTamnnoCV.set(str(self.fila*self.columna))




    def botonCancelar(self,opcion):
        if opcion==0:
            self.mostrarOcultar(self.inicio,self.cargadoV)
        elif opcion==1:
            self.mostrarOcultar(self.inicio,self.ajusteV)

    def botonAceptar(self,opcion):
        if opcion==0:
            self.mostrarOcultar(self.inicio,self.cargadoV)
        elif opcion==1:
            paso=True
            try:
                altura=float(self.textVariableAlturaAV.get())
                if altura<=0.0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Altura no valida",))
                    t.start()
                    paso=False
                else:
                    self.altura=altura
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en Altura",))
                t.start()
            try:
                escala=float(self.textVariableEscalaAV.get())
                if escala<=0.0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Escala no valida",))
                    t.start()
                    paso=False
                else:
                    self.escala=escala
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en Escala",))
                t.start()
            try:
                filtro=int(self.textVariableFiltradoAV.get())
                if filtro<=0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Filtro no valida",))
                    t.start()
                    paso=False
                else:
                    self.filtro=filtro
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en filtro",))
                t.start()
            try:
                ajuste=float(self.textVariableAjusteAV.get())
                if ajuste<=0.0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Ajuste no valida",))
                    t.start()
                    paso=False
                else:
                    self.ajuste=ajuste
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en ajuste",))
                t.start()
            try:
                circulo=int(self.textVariableCirculoAV.get())
                if circulo<=0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Circulo no valida",))
                    t.start()
                    paso=False
                else:
                    self.circulo=circulo
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en circulo",))
                t.start()
            try:
                latitud=float(self.textVariableLatitudAV.get())
                if latitud<=0.0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Latitud no valida",))
                    t.start()
                    paso=False
                else:
                    self.coodenadas[0]=latitud
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en Latitud",))
                t.start()
            try:
                longitud=float(self.textVariableLongitudAV.get())
                if longitud<=0.0:
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Longitud no valida",))
                    t.start()
                    paso=False
                else:
                    self.coodenadas[1]=latitud
            finally:
                paso=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en Longitud",))
                t.start()


            if paso:
                self.mostrarOcultar(self.inicio,self.ajusteV)

    def errorMesaje(self,textoError,mensaje):
        textoError.set(mensaje)
        time.sleep(5)
        textoError.set(" ")
        return


    def prueba(self):
        print "Hola Mundo"

    def prueba2(self):
        print self.textboxTipoCV.get()
        

        

