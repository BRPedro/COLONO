# -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2
from imagenes import *
import filtros
import conteo
import threading
import time

# This creates the main window of an application
class Ventana:
    def __init__(self):
        self.contadorE,self.contadorP=0,0
        self.filtro=0
        self.inicio = Tk()
        self.imagelista = listaImagens()
        self.direccionString = ""
        self.listaL = ["", ""]
        
        self.inicio.title("Calculadora")
        self.inicio.geometry("1000x700")
        self.inicio.configure(background='white')


        # **************************Logo y titulo**********************************************
        self.fCabeza = Frame(self.inicio, bg='white')
        self.fCabeza.grid(column=0, row=0)
        self.logo = ImageTk.PhotoImage(Image.open("imagenesInterfaz\\principal\\logo.gif"))
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

        self.bGradiente = Button(self.fBotones, text="Gradiente", command=lambda: self.filtro_gradiente(), bg="yellow green", width=18).grid(row=0, column=1)

        self.bMyFiltro = Button(self.fBotones, text="Verdes", command=lambda: self.filtro_MyFiltro(), bg="yellow green", width=18).grid( row=0, column=2)

        self.bMyFiltro = Button(self.fBotones, text="Cierre", command=lambda: self.filtro_cierre(), bg="yellow green", width=18).grid(row=0, column=3)

        self.bMyFiltro = Button(self.fBotones, text="Apertura", command=lambda: self.filtro_capertura(), bg="yellow green", width=18).grid( row=1, column=0)

        self.bMyFiltro = Button(self.fBotones, text="Erosion", command=lambda: self.filtro_erosion(), bg="yellow green", width=18).grid( row=1, column=1)

        self.bMyFiltro = Button(self.fBotones, text="Dilatacion", command=lambda: self.filtro_dilatacion(), bg="yellow green", width=18).grid( row=1, column=2)

        self.bMyFiltro = Button(self.fBotones, text="Gris", command=lambda: self.filtro_grises(), bg="yellow green", width=18).grid( row=1, column=3)

        self.bMyFiltro = Button(self.fBotones, text="Contar", command=lambda: self.filtro_Contar(), bg="yellow green", width=18).grid( row=1, column=4)

        self.bMyFiltro = Button(self.fBotones, text="detailEnhance ", command=lambda: self.filtro_detailEnhance (), bg="yellow green", width=18).grid( row=0, column=4)

        """***************Ventana de procesamiento***************"""
        
        self.proceso=Toplevel(self.inicio)#Ventana �hija�
        self.proceso.protocol("WM_DELETE_WINDOW", "onexit")
        self.proceso.title("Procesando Imagen")
        self.proceso.config(bg="light sea green")
        l = self.imagelista.escaneo[0]
        self.cargado2 = Label(self.proceso, image=l, bg="light sea green")
        self.proceso.withdraw()


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

    def filtro_capertura(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.apertura()
        cv2.imwrite("imagenProceso\\tem2cp.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2cp.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_gradiente(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.gradiente()
        cv2.imwrite("imagenProceso\\tem2g.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2g.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_MyFiltro(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.mi_filtro()
        cv2.imwrite("imagenProceso\\tem2m.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2m.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_cierre(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.cierre()
        cv2.imwrite("imagenProceso\\tem2c.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2c.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_erosion(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.erosion()
        cv2.imwrite("imagenProceso\\tem2e.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2e.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_dilatacion(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.dilatacion()
        cv2.imwrite("imagenProceso\\tem2d.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2d.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_grises(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.grises()
        cv2.imwrite("imagenProceso\\tem2gs.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2gs.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)
        
    def filtro_Contar(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado,contador = self.filtro.contar()
        self.j2.set(str(contador))
        cv2.imwrite("imagenProceso\\tem2contar.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2contar.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_fucion(self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.fucion()
        cv2.imwrite("imagenProceso\\tem2fucion.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2fucion.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)
        
    def iniciarConteo(self):    

        self.filtro.mi_contador()
        
               
    def nuevoConteo(self):
        print "hola1"
        self.filtro=conteo.Conteo(self.direccionString)
        self.proceso.deiconify()     
        self.inicio.withdraw()     
        print self.direccionString   
        t = threading.Thread(target= self.filtro.mi_contador())
        t.start()        
        t2 = threading.Thread(target=self.animacion())
        t2.start()
        print "hola11"
        
    def animacion(self):
        print "hola3"

        while True:
            print 12
            if(self.filtro.getEtapa==0):
                l = self.imagelista.escaneo[self.contadorE]
                self.cargado2.config(image=l)
                if(self.contadorE<24):
                    self.contadorE+=1
                else:
                    self.contadorE=0
            elif(self.filtro.getEtapa==1):
                l = self.imagelista.proceso[self.contadorP]
                self.cargado2.config(image=l)
                if(self.contadorP<6):
                    self.contadorP+=1
                else:
                    self.contadorP=0
            else:
                break
            time.sleep(3)
        cv2.imwrite("imagenProceso\\tem2contar.jpg", self.filtro.getResultado())
        dirtem = self.ajustar("imagenProceso\\tem2contar.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)
        self.proceso.withdraw()      
        self.inicio.deiconify()
        
        
    def filtro_detailEnhance (self):
        self.filtro = filtros.Filtros(self.direccionString)
        resultado = self.filtro.combinacionFiltro1 ()
        cv2.imwrite("imagenProceso\\tem2sty.jpg", resultado)
        dirtem = self.ajustar("imagenProceso\\tem2sty.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)
        
