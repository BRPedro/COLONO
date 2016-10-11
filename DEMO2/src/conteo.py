# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import cv2
import numpy as np
import threading

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
        self.etapa = 0
        self.resultado = 0

        self.lista1=[]
        self.lista2=[]
        self.lista3=[]
        self.lista4=[]
        self.espera1=False
        self.espera2=False
        self.espera3=False
        self.espera4=False
        self.espera5=False
        self.espera6=False

        self.CuadradosC1 = [[[0,0]]*(self.columna)]*(self.fila)
        
    def getResultado(self):
        return self.resultado
    
    def setEtapa(self, etapa):
        self.etapa = etapa
        
    def getEtapa(self):
        return self.etapa

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
        self.etapa = 1            
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
            self.centroides.append([(((maxC-minC) / 2) + minC), (((maxF-minF) / 2) + minF)])
        tem = cv2.imread(self.dir)
        for i in self.centroides:
            cv2.circle(tem, (i[0], i[1]), 6, (0, 0, 255), 0)
        cv2.imwrite('contado.jpg', tem)
        self.resultad = tem
        self.etapa = 2
        self.listaErosion()
        return tem,len(self.centroides)
    
    def combinacionMetodos(self):
        kernel11 = np.ones((10, 10), np.uint8)
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        erosion = cv2.erode(gris2, kernel11, iterations=2)
        matrizEro = np.array(erosion)
        listaEro = []
        filas, columnas, tipo = self.imagen.shape
        for f in range(filas):
            for c in range(columnas):
                listaEro.append([[[f, c], matrizEro[f][c]]])
        while True:
            inicio, siguiente = 0, 1
            bandera = True
            while siguiente < len(listaEro):
                bandera2 = True
                for lis in listaEro[inicio]:
                    if self.busquedaConPeso(lis[0][0], lis[0][1],lis[1], listaEro[siguiente]):
                        bandera2 = False
                        bandera = False
                        listaEro[inicio] = listaEro[inicio] + listaEro[siguiente]
                        listaEro.pop(siguiente)
                        break
                if bandera2:
                    inicio += 1
                    siguiente += 1
            if bandera:
                break

        print listaEro
    
    def busquedaConPeso(self, f, c, peso, lista2):
        for i in lista2:
            if (peso==i[1] or peso-1==i[1] or peso-2==i[1] or peso+1==i[1] or peso+2==i[1]):
                if i[0][0] == f-1 and i[0][1] == c-1:
                    return True
                if i[0][0] == f-1 and i[0][1] == c:
                    return True
                if i[0][0] == f-1 and i[0][1] == c+1 :
                    return True
                if i[0][0] == f and i[0][1] == c+1:
                    return True
                if i[0][0] == f+1 and i[0][1] == c+1 :
                    return True
                if i[0][0] == f+1 and i[0][1] == c :
                    return True
                if i[0][0] == f+1 and i[0][1] == c-1 :
                    return True
                if i[0][0] == f and i[0][1] == c-1 :
                    return True
        return False


#*********************** hilos metodo****************************

    def listaErosion(self):

        kernel11 = np.ones((10, 10), np.uint8)
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        erosion = cv2.erode(gris2, kernel11, iterations=2)
        matrizEro = np.array(erosion)
        self.espera5=False
        t0=threading.Thread(target=self.matrizVerde)
        t0.start()

        listaEro = []
        filas, columnas, tipo = self.imagen.shape
        for f in range(filas):
            for c in range(columnas):
                listaEro.append([[[f, c], matrizEro[f][c]]])
        largo=len(listaEro)//4
        print "Paso1"
        self.seteo()
        print len(listaEro)
        t1=threading.Thread(target=self.metodoHilosAgrupar,args=(listaEro[0:largo],1,))
        t2=threading.Thread(target=self.metodoHilosAgrupar,args=(listaEro[largo:(largo*2)],2,))
        t3=threading.Thread(target=self.metodoHilosAgrupar ,args= (listaEro[(largo*2):(largo*3)],3,))
        t4=threading.Thread(target=self.metodoHilosAgrupar,args= (listaEro[(largo*3):len(listaEro)],4,))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        while True:
            if self.espera1 and self.espera2 and self.espera3 and self.espera4:
                break

        lista1=self.lista1+self.lista2
        lista2=self.lista3+self.lista4
        self.seteo()
        print "Paso2"
        t5=threading.Thread(target=self.metodoHilosAgrupar, args=(lista1,1,))
        t6=threading.Thread(target=self.metodoHilosAgrupar, args=(lista2,2,))
        t5.start()
        t6.start()

        while True:
            if self.espera1 and self.espera2:
                break

        print "Paso3"
        lista1=self.lista1+self.lista2
        self.seteo()
        t7=threading.Thread(target=self.metodoHilosAgrupar, args=(lista1,1,))
        t7.start()
        while True:
            if self.espera1:
                break
        for i in self.lista1:
            self.centroideCuadrado(i)
        print len(self.lista1)
        self.dibujarCentroErosion(erosion,self.lista1)
        print self.CuadradosC1
        print "fin"

        while True:
            if self.espera5:
                break
        listaC=self.combinar()
        tem = cv2.imread(self.dir)
        for i in listaC:
            cv2.circle(tem, (i[0], i[1]), 6, (0, 0, 255), 0)
        cv2.imwrite('contado.jpg', tem)
        self.resultad = tem
        return tem,len(listaC)



    def metodoHilosAgrupar(self,listaD,numLista):
        while True:
            inicio, siguiente = 0, 1
            bandera = True
            while siguiente < len(listaD):
                bandera2 = True
                for lis in listaD[inicio]:
                    if self.busquedaConPeso(lis[0][0], lis[0][1],lis[1], listaD[siguiente]):
                        bandera2 = False
                        bandera = False
                        listaD[inicio] = listaD[inicio] + listaD[siguiente]
                        listaD.pop(siguiente)
                        break
                if bandera2:
                    inicio += 1
                    siguiente += 1
            if bandera:
                break
        if(numLista==1):
            self.lista1=listaD
            self.espera1=True
        elif numLista==2:
            self.lista2=listaD
            self.espera2 = True
        elif numLista==3:
            self.lista3=listaD
            self.espera3 = True
        elif numLista==4:
            self.lista4=listaD
            self.espera4 = True
        else:
            self.espera1=True
            self.espera2=True
            self.espera3=True
            self.espera4=True

    def seteo(self):
        self.espera1=False
        self.espera2=False
        self.espera3=False
        self.espera4=False
        self.lista1=[]
        self.lista2=[]
        self.lista3=[]
        self.lista4=[]

    def centroideCuadrado(self,lista):
        maxF,maxC=0,0
        minF,minC=self.fila-1,self.columna-1
        for temp in lista:
            if temp[0][0]>maxF: maxF=temp[0][0]
            elif temp[0][0]<minF: minF=temp[0][0]
            if temp[0][1]>maxC: maxC=temp[0][1]
            elif temp[0][1]<minC:minC=temp[0][1]
        for temp in lista:
            self.CuadradosC1[temp[0][0]][temp[0][1]]=[(((maxC-minC) / 2) + minC), (((maxF-minF) / 2) + minF)]

    def matrizVerde(self):
        self.espera5=False
        for f in range(self.fila):
            for c in range(self.columna):
                rojo, verde, azul = self.matrizOrig[f][c]
                if (rojo < verde) and (azul < verde):
                    self.newData[f][c] = 1
                else:
                    self.newData[f][c] = 0
        self.espera5=True

    def combinar(self):
        listaT=[]
        for f in range(self.fila):
            for c in range(self.columna):
                if self.newData[f][c]==1:
                    if listaT.count(self.CuadradosC1[f][c])==0:
                        listaT.append(self.CuadradosC1[f][c])
        return listaT

    def dibujarCentroErosion(self,imagen,lista):
        listas=[]
        for f in range(self.fila):
            for c in range(self.columna):
               if listas.count(self.CuadradosC1[f][c])==0:
                   listas.append(self.CuadradosC1[f][c])
        for i in listas:
            cv2.circle(imagen, (i[0], i[1]), 6, (0, 0, 255), 0)
        cv2.imwrite('centroErosion.jpg', imagen)
