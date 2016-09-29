from Tkinter import *
from tkFileDialog import *
from PIL import ImageTk, Image
import cv2
from imagenes import *
import filtros

# This creates the main window of an application
class Ventana:
    def __init__(self):
        self.inicio = Tk()
        self.imagelista = listaImagens()
        self.direccionString = ""
        self.listaL = ["", ""]
        
        self.inicio.title("Calculadora")
        self.inicio.geometry("1000x600")
        self.inicio.configure(background='white')


        # **************************Logo y titulo**********************************************
        self.fCabeza = Frame(self.inicio, bg='white')
        self.fCabeza.grid(column=0, row=0)
        self.logo = ImageTk.PhotoImage(Image.open("logo.gif"))
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

        self.fBotones = Frame(self.inicio)
        self.fBotones.grid(column=0, row=2)
        self.bCargar = Button(self.fBotones, text="Cargar", command=lambda: self.direccion(), bg="green", width=18).grid(row=0, column=0)

        self.bGradiente = Button(self.fBotones, text="Gradiente", command=lambda: self.filtro_gradiente(), bg="yellow green", width=18).grid(row=0, column=1)

        self.bMyFiltro = Button(self.fBotones, text="Verdes", command=lambda: self.filtro_MyFiltro(), bg="yellow green", width=18).grid( row=0, column=2)

        self.bMyFiltro = Button(self.fBotones, text="Cierre", command=lambda: self.filtro_cierre(), bg="yellow green", width=18).grid(row=0, column=3)

        self.bMyFiltro = Button(self.fBotones, text="Apertura", command=lambda: self.filtro_capertura(), bg="yellow green", width=18).grid( row=1, column=0)

        self.bMyFiltro = Button(self.fBotones, text="Erosion", command=lambda: self.filtro_erosion(), bg="yellow green", width=18).grid( row=1, column=1)

        self.bMyFiltro = Button(self.fBotones, text="Dilatacion", command=lambda: self.filtro_dilatacion(), bg="yellow green", width=18).grid( row=1, column=2)

        self.bMyFiltro = Button(self.fBotones, text="Gris", command=lambda: self.filtro_grises(), bg="yellow green", width=18).grid( row=1, column=3)

        self.bMyFiltro = Button(self.fBotones, text="Contar", command=lambda: self.filtro_Contar(), bg="yellow green", width=18).grid( row=1, column=4)

        self.bMyFiltro = Button(self.fBotones, text="fundir", command=lambda: self.filtro_fucion(), bg="yellow green", width=18).grid( row=0, column=4)

        self.inicio.mainloop()
        
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
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.apertura()
        cv2.imwrite("tem2cp.jpg", resultado)
        dirtem = self.ajustar("tem2cp.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_gradiente(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.gradiente()
        cv2.imwrite("tem2g.jpg", resultado)
        dirtem = self.ajustar("tem2g.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_MyFiltro(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.mi_filtro()
        cv2.imwrite("tem2m.jpg", resultado)
        dirtem = self.ajustar("tem2m.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_cierre(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.cierre()
        cv2.imwrite("tem2c.jpg", resultado)
        dirtem = self.ajustar("tem2c.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_erosion(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.erosion()
        cv2.imwrite("tem2e.jpg", resultado)
        dirtem = self.ajustar("tem2e.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_dilatacion(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.dilatacion()
        cv2.imwrite("tem2d.jpg", resultado)
        dirtem = self.ajustar("tem2d.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_grises(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.grises()
        cv2.imwrite("tem2gs.jpg", resultado)
        dirtem = self.ajustar("tem2gs.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)
        
    def filtro_Contar(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.contar()
        cv2.imwrite("tem2contar.jpg", resultado)
        dirtem = self.ajustar("tem2contar.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

    def filtro_fucion(self):
        filtro = filtros.Filtros(self.direccionString)
        resultado = filtro.fucion()
        cv2.imwrite("tem2fucion.jpg", resultado)
        dirtem = self.ajustar("tem2fucion.jpg", False)
        self.imagelista.lista[2] = ImageTk.PhotoImage(Image.open(dirtem))
        l = self.imagelista.lista[2]
        self.listaL[1].config(image=l)

