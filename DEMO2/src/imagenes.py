from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2

n=Tk()

class listaImagens:
    def __init__(self):

        self.lista=[ImageTk.PhotoImage(Image.open("imagenesInterfaz\\principal\\null.jpg")),PhotoImage(file="imagenesInterfaz\\principal\\logo.gif"),PhotoImage(file="imagenesInterfaz\\principal\\logo.gif")]
        self.escaneo=[]
        self.proceso=[]
        for i in range(26):
            self.escaneo.append(ImageTk.PhotoImage(Image.open("imagenesInterfaz\\cargado\\escaneo\\"+str(i)+".jpg")))
        for i in range(8):
            self.proceso.append(ImageTk.PhotoImage(Image.open("imagenesInterfaz\\cargado\\proceso\\"+str(i)+".jpg")))
    n.destroy()

n.mainloop()
