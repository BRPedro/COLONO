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
import conteoCombinado as CC

class Ventana:
    def __init__(self):
        self.inicio = Tk()
        self.imagelista = listaImagens()
        self.direccionString = ""
        self.listaL = ["", ""]

        self.filtro=2
        self.altura=15
        self.tipoBanda=0
        self.coodenadas=[0.0,0.0]
        self.fila=0
        self.columna=0
        self.tipo=0
        self.escala=0.25
        self.ajuste=20.0
        self.circulo=10

        self.contador=0

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
        self.bMyFiltro = Button(self.fBotones, text="Contar Plantas", command=lambda: self.contarPlantas(), bg="yellow green", width=18).grid( row=0, column=0)

        self.menu1 = Menu(self.inicio)
        self.inicio.config(menu=self.menu1)
        self.menu1_1 = Menu(self.menu1, tearoff=0)
        self.menu1.add_cascade(label="Archivo", menu=self.menu1_1)
        self.menu1_1.add_command(label="Cargar",command=lambda: self.mostrarOcultar(self.cargadoV,self.inicio))
        self.menu1_1.add_cascade(label="Guardar",command=lambda: self.mostrarOcultar(self.ajusteV,self.inicio))

        self.menu1_2 = Menu(self.menu1, tearoff=0)
        self.menu1.add_cascade(label="Ajustes",command=lambda: self.iniciarVentanaAjustes())


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

        self.lResoluccionCV=Label(self.framelabelCV,text="Resolucio:",bg='white',width=20).grid(row=0,column=0)
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

        self.textboxAlturaCV=StringVar()
        self.textboxAlturaCV.set(str(self.altura))
        self.lAlturaCV=Label(self.framelabelCV,text="Altura de vuelo:",bg='white',width=15).grid(row=4,column=0)
        self.eAlturaCV=Entry(self.framelabelCV,textvariable=self.textboxAlturaCV,bg='white').grid(row=4,column=1)


        self.lEscalCV=Label(self.framelabelCV,text="Escala pixeles:",width=15).grid(row=5,column=0)
        self.textboxEscalaCV=StringVar()
        self.textboxEscalaCV.set(str(self.escala))
        self.eEscalaCV=Entry(self.framelabelCV,textvariable=self.textboxEscalaCV, bg='white').grid(row=5,column=1)

        #---------------Frame de sector de Error---------------
        self.frameErrorCV=Frame(self.cargadoV, bg='white')
        self.frameErrorCV.grid(column=0, row=2 )

        self.textVariableErrorCV=StringVar()
        self.textVariableErrorCV.set("     ")
        self.errorAV=Label(self.frameErrorCV,textvariable=self.textVariableErrorCV,bg='white',width=35,  height=2 ).grid(row=0,column=0)

        #---------------Frame de sector de Botones---------------
        self.frameBoteonesCV=Frame(self.cargadoV, bg='white')
        self.frameBoteonesCV.grid(column=0, row=3 )

        self.bAceptarCV = Button(self.frameBoteonesCV, text="Aceptar", command=lambda: self.botonAceptar(0), bg="yellow green", width=18).grid( row=0, column=0)
        self.bCancelarCV = Button(self.frameBoteonesCV, text="Cancelar", command=lambda: self.botonCancelar(0), bg="yellow green", width=18).grid( row=0, column=1)

        #-----------------------------------------------------------

        """******************************Ventana de Ajuste******************************"""
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

        self.lAjusteAV=Label(self.framelabeAV,text="Ajuste de proximidad:",bg='white',width=20).grid(row=3,column=0)
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

        self.frameErrorAV=Frame(self.ajusteV, bg='white')
        self.frameErrorAV.grid(row=1,column=0)

        self.textVariableErrorAV=StringVar()
        self.textVariableErrorAV.set("     ")
        self.errorAV=Label(self.frameErrorAV,textvariable=self.textVariableErrorAV,bg='white',width=35,  height=2 ).grid(row=0,column=0)

        self.frameBoteonesAV=Frame(self.ajusteV, bg='white')
        self.frameBoteonesAV.grid(column=0, row=2)

        self.bAceptarCV = Button(self.frameBoteonesAV, text="Aceptar", command=lambda: self.botonAceptar(1), bg="yellow green", width=18).grid( row=0, column=0)
        self.bCancelarCV = Button(self.frameBoteonesAV, text="Cancelar", command=lambda: self.botonCancelar(1), bg="yellow green", width=18).grid( row=0, column=1)

        #-----------------------------------------------------------

        """******************************Ventana de Espera******************************"""

        self.procesoV=Toplevel(self.inicio)
        self.procesoV.title("Proceso")
        self.procesoV.configure(background='white')

        self.imagP = self.imagelista.escaneo[0]
        self.imagePV = Label(self.procesoV, image=self.imagP, bg='white')
        self.imagePV.config()
        self.imagePV.grid(row=0, column=0)

        self.textVariablePasoPV=StringVar()
        self.textVariablePasoPV.set("Paso: 1")
        self.labelTextPasoPV=Label(self.procesoV,textvariable=self.textVariablePasoPV,bg='white',width=10).grid(row=1,column=0)



        self.ajusteV.withdraw()
        self.cargadoV.withdraw()
        self.procesoV.withdraw()
        self.inicio.mainloop()

    def mostrarOcultar(self,ver,ocultar):#Mostrar ventana registro y ocultar la de inicio
        ocultar.withdraw()
        ver.deiconify()
        
    def ajustar(self):
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

    def ajustarConParametro(self,imagen):
        f,c,t=imagen.shape
        if f>400:
            porcen=(400.0*100.0/f)/100.0
            imag=cv2.resize(imagen, (int(c*porcen),int(f*porcen)), interpolation=cv2.INTER_CUBIC)
        f,c,t=imagen.shape
        if c>400:
            porcen=(400.0*100.0/c)/100.0
            imag=cv2.resize(imagen, (int(c*porcen),int(f*porcen)), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("imagenesInterfaz\\principal\\ajustar.jpg", imagen)
        return "imagenesInterfaz\\principal\\ajustar.jpg"

    def cargarImagen(self,dire):
        imagens = PhotoImage(file=dire)
        return imagens

    def seleccionarImagen(self):
        try:
            self.direccionString = askopenfilename()
            self.imagen=cv2.imread(self.direccionString)
            self.fila,self.columna,self.tipo =self.imagen.shape
            dirtem = self.ajustar()
            self.imagelista.lista[1] = ImageTk.PhotoImage(Image.open(dirtem))
            l = self.imagelista.lista[1]
            self.listaL[0].config(image=l)
            self.lCVimagen.config(image=l)
            self.textResolucionCV.set(str(self.fila)+" x "+str(self.columna))
            self.textTamnnoCV.set(str(self.fila*self.columna))

        except:
            self.direccionString=""
            t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"El archivo seleccionado\nno es valido",))
            t.start()

    def botonCancelar(self,opcion):
        if opcion==0:
            self.mostrarOcultar(self.inicio,self.cargadoV)
        elif opcion==1:
            self.mostrarOcultar(self.inicio,self.ajusteV)

    def botonAceptar(self,opcion):
        if opcion==0:
            self.combalidarCargado()
        elif opcion==1:
            self.combalidacionAjustes()

    def iniciarVentanaAjustes(self):
        self.textVariableAlturaAV.set(str(self.coodenadas[0]))
        self.textVariableLongitudAV.set(str(self.coodenadas[1]))
        self.textVariableAlturaAV.set(str(self.altura))
        self.textVariableEscalaAV.set(str(self.escala))
        self.textVariableFiltradoAV.set(str(self.filtro))
        self.textVariableAjusteAV.set(str(self.ajuste))
        self.textVariableCirculoAV.set(str(self.circulo))
        self.mostrarOcultar(self.ajusteV,self.inicio)

    def errorMesaje(self,textoError,mensaje):
        textoError.set(mensaje)
        time.sleep(5)
        textoError.set(" ")
        return

    def prueba(self):
        print "Hola Mundo"

    def combalidacionAjustes(self):
        estado=True

        altura=self.altura
        escala=self.escala
        filtro=self.filtro
        ajuste=self.ajuste
        circulo=self.circulo
        coordenadas=self.coodenadas
        try:
            print self.textVariableAlturaAV.get()
            altura=float(self.textVariableAlturaAV.get())
            if altura<=0.0:
                estado=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"El valor debe ser superior a 0.0\nen Altura de vuelo",))
                t.start()
            else:
                try:
                    escala=float(self.textVariableEscalaAV.get())
                    if estado<=0:
                        estado=False
                        t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"El valor debe ser superior a 0.0\nen Escala PxM",))
                        t.start()
                    else:
                        try:
                            filtro=int(self.textVariableFiltradoAV.get())
                            if filtro<=0:
                                estado=False
                                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"El valor debe ser superior a 0\nen Filtro de ruido",))
                                t.start()
                            else:
                                try:
                                    ajuste=float(self.textVariableAjusteAV.get())
                                    if ajuste<=0.0:
                                        estado=False
                                        t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"El valor debe ser superior a 0.0\nen Ajuste de proximidad",))
                                        t.start()
                                    else:
                                        try:
                                            circulo=int(self.textVariableCirculoAV.get())
                                            if circulo<=0:
                                                estado=False
                                                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"El valor debe ser superior a 0\nen Tamanno circulo",))
                                                t.start()
                                            else:
                                                try:
                                                    coordenadas[0]=float(self.textVariableLatitudAV.get())
                                                    coordenadas[1]=float(self.textVariableLongitudAV.get())
                                                except:
                                                    estado=False
                                                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en campo\nCoordenadas",))
                                                    t.start()
                                        except:
                                            estado=False
                                            t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en campo\nTamanno Circulo",))
                                            t.start()
                                except:
                                    estado=False
                                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en campo\nAjuste de proximidad",))
                                    t.start()
                        except:
                            estado=False
                            t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en campo\nFiltro de ruido",))
                            t.start()
                except:
                    estado=False
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en campo\nEscala PxM",))
                    t.start()
        except:
            estado=False
            t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorAV,"Solo numeros en campo\nAltura de vuelo",))
            t.start()

        if estado:
            self.altura=altura
            self.escala=escala
            self.filtro=filtro
            self.ajuste=ajuste
            self.circulo=circulo
            self.coodenadas=coordenadas
            self.mostrarOcultar(self.inicio,self.ajusteV)
        
    def combalidarCargado(self):
        coordenadas=self.coodenadas
        escala=self.escala
        altura=self.altura
        estado=True

        if self.direccionString=="":
            estado=False
            t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"Seleccione una\nImagen",))
            t.start()
        else:
            try:
                coordenadas[0]=float(self.textLatitudCV.get())
                coordenadas[1]=float(self.textLongitudCV.get())
                try:
                    altura=float(self.textboxAlturaCV.get())
                    if altura<=0.0:
                        estado=False
                        t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"El valor de altura de vuelo\ndebe ser mayor a 0.0",))
                        t.start()
                    else:
                        try:
                            escala=float(self.textboxEscalaCV.get())
                            if escala<=0.0:
                                estado=False
                                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"El valor de Escala de\n pixeles debe ser mayor a 0.0",))
                                t.start()
                        except:
                            estado=False
                            t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"El valor de Escala de pixeles\ndebe ser numerico",))
                            t.start()
                except:
                    estado=False
                    t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"El valor de altura de vuelo\ndebe ser numerico",))
                    t.start()

            except:
                estado=False
                t = threading.Thread(target=self.errorMesaje,args=(self.textVariableErrorCV,"El valor de cordenadas debe\nser numerico",))
                t.start()
        if estado:
            self.escala=escala
            self.altura=altura
            self.mostrarOcultar(self.inicio,self.cargadoV)

    def contarPlantas(self):
        print self.direccionString
        if self.direccionString=="":
            t = threading.Thread(target=self.errorMesaje,args=(self.j2,"Error de seleccion",))
            t.start()
        else:
            self.contador=CC.ConteoCombinado(self.direccionString)
            resultado=self.contador.mi_contadorAgrupado(self.filtro,self.ajuste,self.circulo)
            if len(resultado)>0:
                dirtem = self.ajustarConParametro(resultado[0])
                self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
                l = self.imagelista.lista[2]
                self.listaL[1].config(image=l)
                self.j2.set(str(resultado[1]))


