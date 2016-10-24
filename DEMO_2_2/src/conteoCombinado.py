#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Pedro Barrantes R"
__date__ = "$11/10/2016 09:44:07 AM$"

import cv2
import numpy as np
from Tkinter import *
from imagenes import *
import threading
import time
"""
Clase encargada de realizar el conteo de pinnas en una plantacion
Su constructor recibe un string con la direccion de la imagen.
"""
class ConteoCombinado:
    def __init__(self, direccion):
        self.paso=0
        self.dir = direccion
        self.imagen = cv2.imread(direccion)
        self.matrizOrig = np.array(self.imagen)
        self.fila, self.columna, self.tipo = self.imagen.shape
        self.newData = np.zeros(shape=(self.fila, self.columna))
        self.centroides = []

    def getPaso(self):
        return self.paso
    def setPaso(self,paso):
        self.paso=paso
        
    """
    Metodo que busca los 8 vecinos mas cercanos de una coordenada (f,c)
    Recibe de parametros:
        f =  fila (int)
        c = columna (int)
        lista = lista de coordenadas ejemplo: [[2,3],[1,2], ...,[2,4]]
    Retorna True si tiene un vecino en la lista o Falso si no tiene vecino. 
    """
    def busqueda(self, f, c, lista):
        if lista.count([f-1, c-1]) > 0:
            return True
        if lista.count([f-1, c]) > 0:
            return True
        if lista.count([f-1, c + 1]) > 0:
            return True
        if lista.count([f, c + 1]) > 0:
            return True
        if lista.count([f + 1, c + 1]) > 0:
            return True
        if lista.count([f + 1, c]) > 0:
            return True
        if lista.count([f + 1, c-1]) > 0:
            return True
        if lista.count([f, c-1]) > 0:
            return True
        return False
    
    """
    Metodo de ordenamiento burbuja.
    Se toma el tamanno de la sublistas como condicion de ordenamiento
        Recibe un lista la cual ordena de menor a mayor
        Retorna la lista ordenada
    Ejemplo: 
        Lista entrada: [[[1,2]], [[0,1], [0,2], [0,3]], [[1,3], [1,4]]] 
        Resultado: [[[1,2]], [[1,3], [1,4]] , [[0,1], [0,2], [0,3]]]
    """
    def burbuja(self, lista):#Se puede modificar para mejorar el rendimiento o remplazarlo con un motodo mas eficiente.
        numero = len(lista)
        i = 0
        while (i < numero):
            j = i
            while (j < numero):
                if(len(lista[i]) > len(lista[j])):
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp
                j = j + 1
            i = i + 1
        return lista

    def contadorAgrupado(self, limitePatron,limiteCercania, circulo):
        try:
            self.paso+=1
            listapuntos = []
            for f in range(self.fila):
                for c in range(self.columna):
                    rojo, verde, azul = self.matrizOrig[f][c]
                    if (rojo < verde) and (azul < verde):
                        listapuntos.append([[f, c]])
                        self.newData[f][c] = 1
                    else:
                        self.newData[f][c] = 0
            self.paso+=1
            while True:
                inicio, siguiente = 0, 1
                bandera = True
                while siguiente < len(listapuntos):
                    bandera2 = True
                    for lis in listapuntos[inicio]:
                        if self.busqueda(lis[0], lis[1], listapuntos[siguiente]):
                            bandera2 = False
                            bandera = False
                            listapuntos[inicio] = listapuntos[inicio] + listapuntos[siguiente]
                            listapuntos.pop(siguiente)
                            break
                    if bandera2:
                        inicio += 1
                        siguiente += 1
                if bandera:
                    break

            self.paso+=1
            listapuntos=self.borrarXcantidadElemento(listapuntos,limitePatron)
            listapuntos=self.burbuja(listapuntos)
            self.paso+=1
            listapuntos=self.agrupamientoXproximidad(listapuntos,limiteCercania)
            self.paso+=1
            for i in listapuntos:#
                minF, minC = self.fila-1, self.columna-1
                maxF, maxC = 0, 0
                for ii in i:
                    if ii[0] < minF:
                        minF = ii[0]
                    if ii[0] > maxF:
                        maxF = ii[0]
                    if ii[1] < minC:
                        minC = ii[1]
                    if ii[1] > maxC:
                        maxC = ii[1]
                self.centroides.append([((maxC-minC) / 2) + minC,((maxF-minF) / 2) + minF])
                tem = cv2.imread(self.dir)
                for i in self.centroides:
                    cv2.circle(tem, (i[0], i[1]), circulo, (0, 0, 255), 0)
                cv2.imwrite('imagenProceso\\contado1.jpg', tem)
            self.paso+=1
            return [tem,len(self.centroides)]
        except:
            return []

    """
    Metodo que borra patrones que no cumplan el limite de elementos minimo
    Parametros:
            lista: Lista de coordenada int[][]
            limite: limite de coordenadas int
    Retorna: 
            Retorna: int[][]
    """
    def borrarXcantidadElemento(self, lista, limite):
        listaT = []
        for i in lista:
            if len(i) > limite:
                listaT.append(i)
        listaT = self.burbuja(listaT)
        return listaT
    
    """
    Metodo que calcula un punto central de un patron
    Parametros:
            lista: Lista de coordenada int[][]
    Retorna: 
            Retorna: coordenada central del patron; int[]
    """
    def puntoCentralGrupo(self, lista):
        maxF, maxC = 0, 0
        minF, minC = self.fila-1, self.columna-1
        for temp in lista:
            if temp[0] > maxF:
                maxF = temp[0]
            if temp[0] < minF:
                minF = temp[0]
            if temp[1] > maxC:
                maxC = temp[1]
            if temp[1] < minC:
                minC = temp[1]
        return [((maxF-minF) / 2) + minF, ((maxC-minC) / 2) + minC]   
   
    """
    Metodo para calcular la distancia de dos puntos (F, C)
    Parametros:
            coordenada1: lista de int ejemplo: [0, 0]
            coordenada2: lista de int ejemplo: [0, 1]
    Retorna: 
            Resultado: float
    """
    def distaciaEntrePuntos(self, coordenada1, coordenada2):
        resultado = (((coordenada2[0]-coordenada1[0]) ** 2) + ((coordenada2[1]-coordenada1[01]) ** 2)) ** 0.5
        if(resultado < 0):
            resultado *= -1
        return resultado
    
    """
    Metodo que verifica si dos patrones se encuentran cercanos
    Parametros:
            patron1 y patron2: lista de coordenadas int 
		Ejemplo: [[0,0], [0,1]]
            limite: distancia de cercanoa a comprobar
    Retorna: 
            Resultado: 
                False: si no estan cercanas.
                True: si estan cercanas.
    """
    def distaciaEntrePatrones(self, patron1, patron2, limite):
        resultado = self.distaciaEntrePuntos(self.puntoCentralGrupo(patron1), self.puntoCentralGrupo(patron2))
        if resultado <= float(limite):
            return True
        return False
    
    """
    Metodo que verifica los vecinos de los patrones y si existen patrones mas cercanos al limite minimo borra el patron con menor cantidad de coordenadas
    Parametros:
        listaGrupos: lista [][][]
        limite: int, limite de cercania
      Retorna: 
        Int[][][]
    """
    def agrupamientoXproximidad(self, listaGrupos, limite):#Este metodo se puede mejorar si se realiza un manejo mejor de los ciclos de busqueda en la lista.
        while True:
            bandera = True
            i1 = 0
            while i1 < len(listaGrupos)-1:
                i2 = i1 + 1
                bandera2 = True
                while i2 < len(listaGrupos):
                    if (self.distaciaEntrePatrones(listaGrupos[i1], listaGrupos[i2], limite)):
                        if len(listaGrupos[i1]) > len(listaGrupos[i2]):
                            listaGrupos.pop(i2)
                        else:
                            listaGrupos.pop(i1)
                        bandera2 = False
                        break

                    i2 += 1
                if  bandera2== False:
                    bandera = False
                    break
                i1 += 1
            if bandera:
                break
        return listaGrupos

    def inicioConteo(self,limitePatron,limiteCercania, circulo):
        return self.contadorAgrupado(limitePatron,limiteCercania,circulo)

#n = ConteoCombinado("C:\\Users\\PBR\\Documents\\NetBeansProjects\\COLONO\\COLONO\\DEMO2\\src\\corte.jpg")
#n.mi_contadorAgrupado(2,20,10)


