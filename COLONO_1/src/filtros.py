# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import cv2
import numpy as np
from time import time

__author__ = "PBR"
__date__ = "$01/09/2016 11:13:37 AM$"


class Filtros:
    def __init__(self, imagen):
        self.imagen = cv2.imread(imagen)
        self.gris = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        self.data = np.array(self.imagen)

    def cierre(self):
        kernel9 = np.ones((9, 9), np.uint8)
        cierre = cv2.morphologyEx(self.gris, cv2.MORPH_CLOSE, kernel9)
        return cierre

    def apertura(self):
        kernel9 = np.ones((9, 9), np.uint8)
        apertura = cv2.morphologyEx(self.gris, cv2.MORPH_OPEN, kernel9)
        return apertura

    def erosion(self):
        kernel11 = np.ones((11, 11), np.uint8)
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
        cv2.imwrite('tem0.jpg', newData)
        tem = cv2.imread('tem0.jpg')
        return tem

    def grises(self):
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        return gris2


    def dos_grises(self):
        tiempo_inicial = time()
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        cv2.imwrite('gris1.jpg', gris2)
        print 'El tiempo de ejecucion de opencv fue:', tiempo_ejecucion  # En segundos

        tiempo_inicial = time()
        newData = self.data
        filas, columnas, tipo = self.imagen.shape
        for f in range(filas):
            for c in range(columnas):
                rojo, verde, azul = self.data[f][c]
                promedio = (rojo + verde + azul) // 3
                newData[f][c] = [promedio, promedio, promedio]
        cv2.imwrite('gris2.jpg', newData)
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        cv2.imwrite('gris2.jpg', gris2)
        print 'El tiempo de ejecucion de propio fue:', tiempo_ejecucion  # En segundos
        print "Hola Pedro"


    def top_Hat(self):
        # Cargar la mascara

        # Crear un kernel de '1' de 3x3
        kernel = np.ones((9, 9), np.uint8)

        # Se aplica la transformacion: Top Hat
        transformacion = cv2.morphologyEx(self.gris, cv2.MORPH_TOPHAT, kernel)
        return transformacion


    def black_Hat(self):
        # Cargar la mascara

        # Crear un kernel de '1' de 3x3
        kernel = np.ones((9, 9), np.uint8)

        # Se aplica la transformacion: Top Hat
        transformacion = cv2.morphologyEx(self.gris, cv2.MORPH_CROSS)
        return transformacion
