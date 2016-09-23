# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2
from imagenes import *
import numpy as np

__author__ = "PBR"
__date__ = "$20/09/2016 01:49:01 PM$"

class Ventana:

    def __init__(self):
        self.f,self.c=0,0
        #self.ff,self.cc=20,20
        self.height, self.width=0,0

        self.contador=7
        self.imagen1=""
        self.imagen2=""
        self.imagen3=""
        self.inicio = Tk()
        self.imagelista = listaImagens()
        self.direccionString1 = ""
        self.direccionString2 = ""
        self.direccionString3 = ""
        self.listaL = ["", ""]

        self.inicio.title("Calculadora")
        self.inicio.geometry("1000x700")
        self.inicio.configure(background='white')
        self.dimencion=40
        self.velo = 5

        self.direccion()

        self.fImagenPrinc = Frame(self.inicio)
        self.fImagenPrinc.grid(row=0,column=0)

        self.fImagenCarg =Frame(self.fImagenPrinc)
        self.fImagenCarg.grid(row=0,column=0)


        self.bArriba = Button(self.fImagenCarg, text="Arriba", command=lambda: self.funcionBoton(0), bg="yellow green",
                                width=10).grid(row=0, column=1)

        self.bDerecha = Button(self.fImagenCarg, text="Derecha", command=lambda: self.funcionBoton(1), bg="yellow green",
                                width=10).grid(row=1, column=0)

        self.lImagenCarga = Label(self.fImagenCarg,  bg="light sea green")
        self.lImagenCarga.config()
        self.lImagenCarga.grid(row=1, column=1)

        self.bIzquierda = Button(self.fImagenCarg, text="Izquierda", command=lambda: self.funcionBoton(2), bg="yellow green",
                                 width=10).grid(row=1, column=2)

        self.bAbajo = Button(self.fImagenCarg, text="Abajo", command=lambda: self.funcionBoton(3), bg="yellow green",
                                 width=10).grid(row=2, column=1)


        self.fImagenCorte = Frame(self.fImagenPrinc)
        self.fImagenCorte.grid(row=0,column=1)

        self.bDerecha2 = Button(self.fImagenCorte, text="<-", command=lambda: self.funcionBoton(41),
                               bg="yellow green",
                               width=5).grid(row=0, column=0)

        self.lImagenCortes = Label(self.fImagenCorte, bg="light sea green")
        self.lImagenCortes.config()
        self.lImagenCortes.grid(row=0, column=1)

        self.bIzquierda = Button(self.fImagenCorte, text="->", command=lambda: self.funcionBoton(5),
                                bg="yellow green",
                                width=5).grid(row=0, column=2)

        self.bBorrar = Button(self.fImagenCorte, text="Borrar", command=lambda: self.funcionBoton(6),
                                bg="yellow green",
                                width=10).grid(row=1, column=1)

        self.fControl = Frame(self.inicio)
        self.fControl.grid(row=1, column=0)




        self.bCortar = Button(self.fControl, text="Cortar", command=lambda: self.funcionBoton(8),
                               bg="yellow green",
                               width=10).grid(row=0, column=0)


        self.inicio.mainloop()

    def mover(self,direccion):
        if(direccion==0):
            if(self.f-self.velo>=0):
                self.f-=self.velo
        elif(direccion==1):
            if self.c-self.velo>=0:
                self.c-=self.velo
        elif(direccion==2):
            if self.c+self.velo<=self.width:
                self.c+=self.velo
        elif(direccion==3):
            if self.f + self.velo <= self.height:
                self.f+=self.velo


        imag1 = cv2.imread("temp1.jpg")
        res1 = cv2.resize(imag1, (100, 100), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("temp1.jpg", res1)

        imag2 = cv2.imread("temp2.jpg")
        res2 = cv2.resize(imag2, (100, 100), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("temp2.jpg", res2)

        imag3 = cv2.imread("temp3.jpg")
        res3 = cv2.resize(imag3, (100, 100), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("temp3.jpg", res3)

        self.imagen1 = cv2.imread(self.direccionString1)
        crop_img1 = self.imagen1[self.f:self.f + self.dimencion, self.c:self.c + self.dimencion]
        cv2.imwrite("temp1.jpg", crop_img1)

        self.imagen2 = cv2.imread(self.direccionString2)
        crop_img2 = self.imagen2[self.f:self.f + self.dimencion, self.c:self.c + self.dimencion]
        cv2.imwrite("temp2.jpg", crop_img2)

        self.imagen3 = cv2.imread(self.direccionString3)
        crop_img3 = self.imagen3[self.f:self.f + self.dimencion, self.c:self.c + self.dimencion]
        cv2.imwrite("temp3.jpg", crop_img3)

        self.imagelista.lista[0] = ImageTk.PhotoImage(Image.open("temp1.jpg"))
        l = self.imagelista.lista[0]
        self.lImagenCarga.config(image=l)



    def funcionBoton(self,tipo):
        print tipo
        if(tipo==0):
            self.mover(0)
        elif(tipo==1):
            self.mover(1)
        elif(tipo==2):
            self.mover(2)
        elif(tipo==3):
            self.mover(3)
        elif(tipo==4):
            self.mover(3)
        elif(tipo==3):
            self.mover(3)
        elif(tipo==5):
            self.mover(3)
        elif(tipo==6):
            self.mover(3)
        elif(tipo==8):
            self.cortar()
        elif(tipo==9):
            self.direccion()


    def cortar(self):
        cor=cv2.imread("temp1.jpg")
        cv2.imwrite("cortes\\corte1_"+str(self.contador)+".jpg",cor)
        cor=cv2.imread("temp2.jpg")
        cv2.imwrite("cortes\\corte2_"+str(self.contador)+".jpg",cor)
        cor=cv2.imread("temp3.jpg")
        cv2.imwrite("cortes\\corte3_"+str(self.contador)+".jpg",cor)
        self.contador+=1


    def direccion(self):
        self.direccionString1 = "C:\\Users\PBR\\Documents\\NetBeansProjects\\COLONO\COLONO\\COLONO_1\\src\\Corte\\2.jpg"
        self.direccionString2 = "C:\\Users\PBR\\Documents\\NetBeansProjects\\COLONO\COLONO\\COLONO_1\\src\\Corte\\verde2.jpg"
        self.direccionString3 = "C:\\Users\PBR\\Documents\\NetBeansProjects\\COLONO\COLONO\\COLONO_1\\src\\Corte\\tem2th.jpg"
        self.imagen1=cv2.imread(self.direccionString1)
        self.imagen2=cv2.imread(self.direccionString2)
        self.imagen3=cv2.imread(self.direccionString3)
        crop_img1 =  self.imagen1[0:10, 0:10]
        crop_img2 =  self.imagen2[0:10, 0:10]
        crop_img3 =  self.imagen3[0:10, 0:10]
        cv2.imwrite("temp1.jpg",crop_img1)
        cv2.imwrite("temp2.jpg",crop_img2)
        cv2.imwrite("temp3.jpg",crop_img3)

        self.imagelista.lista[0] = ImageTk.PhotoImage(Image.open(self.direccionString1 ))
        l = self.imagelista.lista[0]
        #self.lImagenCarga.config(image=l)
        self.height, self.width = self.imagen1.shape[:2]
Ventana()