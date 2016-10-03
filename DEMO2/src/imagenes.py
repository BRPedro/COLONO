from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2

n=Tk()

class listaImagens:
    def __init__(self):

        self.lista=[ImageTk.PhotoImage(Image.open("null.jpg")),PhotoImage(file="logo.gif"),PhotoImage(file="logo.gif")]
        self.escaneo=[]
        self.proceso=[]
        #for i in range(28):
            #escaneo.append(mageTk.PhotoImage(Image.open("null.jpg")))
    n.destroy()

n.mainloop()
