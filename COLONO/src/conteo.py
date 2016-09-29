# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cv2
import filtros as fil
import numpy as np

__author__ = "PBR"
__date__ = "$28/09/2016 08:32:41 AM$"

class Conteo:
    def __init__(self, direccion):
        self.dir = direccion
        self.imagen = cv2.imread(direccion)
        self.matrizOrig = np.array(self.imagen)
        self.centroides = []
        self.vectores = []
        
        self.fila, self.columna, self.tipo = self.imagen.shape
        self.newData = np.zeros(shape=(self.fila, self.columna))
        
        
        
        
    def contar2(self):
        filas, columnas, tipo = self.matrizOrig.shape
        for f in range(filas):
            for c in range(columnas):
                if (self.matrizOrig[f][c][0] != 255)or(self.matrizOrig[f][c][1] != 255)or (self.matrizOrig[f][c][2] != 255):
                    self.verVecinoInicio(f, c, filas, columnas)
                
        
        tem = cv2.imread(self.dir)
        for i in self.centroides:
            cv2.circle(tem, (i[0], i[1]), 63, (0, 0, 255), -1)
        cv2.imwrite('contado.jpg', tem)
        return tem
    
    
    
    def mi_filtro(self):
        for f in range(self.fila):
            for c in range(self.columna):
                rojo, verde, azul = self.matrizOrig[f][c]
                if (rojo < verde) and (azul < verde):
                    self.newData[f][c] = 1
                else:
                    self.newData[f][c] = 0
                    
    def contar(self):
        self.mi_filtro()
        for f in range(self.fila):
            for c in range(self.columna):
                if self.newData[f][c] == 1:
                    self.verVecinoInicio(f, c, self.fila, self.columna)
                
        
        tem = cv2.imread(self.dir)
        for i in self.centroides:
            cv2.circle(tem, (i[0], i[1]), 63, (0, 0, 255), -1)
        cv2.imwrite('contado.jpg', tem)
        return tem
        
    def verVecinoInicio(self, f, c, maxF, maxC):
        self.newData[f][c] = 0
        self.vectores = [[f, c]]
        if(f > 0 and c > 0):
            self.verVecino(f-1, c-1, maxF, maxC)
        if(f > 0):
            self.verVecino(f-1, c, maxF, maxC)
        if(f > 0 and c < maxC-1):
            self.verVecino(f-1, c + 1, maxF, maxC)
        if(c < maxC-1):
            self.verVecino(f, c + 1, maxF, maxC)
        if(f < maxF-1  and c < maxC-1):
            self.verVecino(f + 1, c + 1, maxF, maxC)
        if(f < maxF-1):
            self.verVecino(f + 1, c, maxF, maxC)
        if(f < maxF-1  and c > 0):
            self.verVecino(f + 1, c-1, maxF, maxC)
        if(c > 0):
            self.verVecino(f, c-1, maxF, maxC)
        minF, minC = 0, 0
        maxF, maxC = maxF-1, maxC-1
        for i in self.vectores:
            if i[0] < minF:
                minF = i[0]
            if i[0] > maxF:
                maxF = i[0]
            if i[1] < minC:
                minC = i[1]
            if i[1] > maxC:
                maxC = i[1]
        if(len(self.vectores) > 5):
            self.centroides.append([(((maxF-minF) / 2) + minF), (((maxC-minC) / 2) + minC)])
        return
        
    def verVecino(self, f, c, maxF, maxC):
        if (self.newData[f][c] == 1):
            self.vectores.append([f, c])
            self.newData[f][c] = 0
            if(f > 0 and c > 0):
                self.verVecino(f-1, c-1, maxF, maxC)
            if(f > 0):
                self.verVecino(f-1, c, maxF, maxC)
            if(f > 0 and c < maxC-1):
                self.verVecino(f-1, c + 1, maxF, maxC)
            if(c < maxC-1):
                self.verVecino(f, c + 1, maxF, maxC)
            if(f < maxF-1  and c < maxC-1):
                self.verVecino(f + 1, c + 1, maxF, maxC)
            if(f < maxF-1):
                self.verVecino(f + 1, c, maxF, maxC)
            if(f < maxF-1  and c > 0):
                self.verVecino(f + 1, c-1, maxF, maxC)
            if(c > 0):
                self.verVecino(f, c-1, maxF, maxC)
            return
        
    def busqueda(self, f, c, lista2):
        if lista2.count([f-1, c-1]) > 0: 
            return True
        if lista2.count([f-1, c]) > 0:
            return True
        if lista2.count([f-1, c + 1]) > 0:
            return True
        if lista2.count([f, c + 1]) > 0:
            return True
        if lista2.count([f + 1, c + 1]) > 0:
            return True
        if lista2.count([f + 1, c]) > 0:
            return True
        if lista2.count([f + 1, c-1]) > 0:
            return True
        if lista2.count([f, c-1]) > 0:
            return True
        return False
    
    def mi_contador(self):
        listapuntos = []
        for f in range(self.fila):
            for c in range(self.columna):
                rojo, verde, azul = self.matrizOrig[f][c]
                if (rojo < verde) and (azul < verde):
                    listapuntos.append([[f, c]])
                    self.newData[f][c] = 1
                else:
                    self.newData[f][c] = 0
                    
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
        for i in listapuntos:
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
            self.centroides.append([(((maxC-minC) / 2) + minC),(((maxF-minF) / 2) + minF)])
        tem = cv2.imread(self.dir)
        for i in self.centroides:
            cv2.circle(tem, (i[0], i[1]), 10, (0, 0, 255), 0)
        cv2.imwrite('contado.jpg', tem)
        return tem
    
    
    
    
        
        