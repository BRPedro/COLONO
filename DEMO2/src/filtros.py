# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import conteo
import cv2
import numpy as np
from time import time

__author__ = "PBR"
__date__ = "$01/09/2016 11:13:37 AM$"


class Filtros:
    def __init__(self, imagen):
        
        self.direccion = imagen
        self.imagen = cv2.imread(imagen)
        self.gris = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        self.data = np.array(self.imagen)

    def cierre(self):
        kernel9 = np.ones((9, 9), np.uint8)
        cierre = cv2.morphologyEx(self.gris, cv2.MORPH_CLOSE, kernel9)
        return cierre

    def apertura(self):
        kernel9 = np.ones((15, 15), np.uint8)
        apertura = cv2.morphologyEx(self.gris, cv2.MORPH_OPEN, kernel9)
        return apertura

    def erosion(self):
        kernel11 = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(self.gris, kernel11, iterations=1)
        return erosion

    def dilatacion(self):
        kernel11 = np.ones((11, 11), np.uint8)
        dilatacion = cv2.dilate(self.gris, kernel11, iterations=1)
        return dilatacion

    def gradiente(self):
        ee3 = np.ones((3, 3), np.uint8)
        gradiente = cv2.morphologyEx(self.gris, cv2.MORPH_GRADIENT, ee3)
        return gradiente

    def tophat1(self):
        ee5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (200, 200))
        tophat3 = cv2.morphologyEx(self.gray, cv2.MORPH_TOPHAT, ee5)
        return tophat3

    def mi_filtro(self):
        newData = self.data
        filas, columnas, tipo = self.imagen.shape
        for f in range(filas):
            for c in range(columnas):
                rojo, verde, azul = self.data[f][c]
                # promedio=(rojo+verde+azul)//3
                if (rojo < verde) and (azul < verde):
                    newData[f][c] = [0, 255, 0]
                else:
                    newData[f][c] = [255, 255, 255]
        cv2.imwrite('imagenProceso\\tem0.jpg', newData)
        tem = cv2.imread('imagenProceso\\tem0.jpg')
        return tem

    def grises(self):
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        return gris2

    def dos_grises(self):
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('imagenProceso\\gris1.jpg', gris2)

        tiempo_inicial = time()
        newData = self.data
        filas, columnas, tipo = self.imagen.shape
        for f in range(filas):
            for c in range(columnas):
                rojo, verde, azul = self.data[f][c]
                promedio = (rojo + verde + azul) // 3
                newData[f][c] = [promedio, promedio, promedio]
        cv2.imwrite('imagenProceso\\gris2.jpg', newData)
        cv2.imwrite('imagenProceso\\gris2.jpg', gris2)
 
    
    def contar(self):        
        return (conteo.Conteo(self.direccion)).mi_contador()
        #return  (conteo.Conteo(self.direccion)).listaErosion()
    
    def fucion(self):
        ima1 = self.erosion()
        ima2 = self.mi_filtro()
        tem = cv2.AddWeighted(ima1, 0.5, ima2, 0.3, 0) 
        cv2.imwrite('imagenProceso\\fucion.jpg', tem)
        return tem
    
    def detailEnhance (self):        
        dst = cv2.detailEnhance(self.imagen, sigma_s=10, sigma_r=0.15)
        return dst
    
    def combinacionFiltro1(self):
        
        edges = cv2.Canny(self.imagen, 100, 200)
        cv2.imwrite('imagenProceso\\combinacionFiltro1.jpg', edges)
        edges = cv2.Canny(self.imagen, 100, 200)
        #return cv2.imread('imagenProceso\\combinacionFiltro1.jpg')



