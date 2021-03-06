# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import cv2
import numpy as np

class ListaColor:
    def __init__(self, imagen):
        self.imagen = cv2.imread(imagen)
        self.data = np.array(self.imagen)
        #self.data = np.sort(self.data,axis=0)
        #cv2.imwrite('gg2.jpg', self.data)
        self.fila,self.columna,self.tipo=self.imagen.shape
        self.matrizColor = np.zeros(shape=(self.fila,self.columna))
        self.lista=[]
        
        
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
        cv2.imwrite('verde.jpg', newData)
        #tem = cv2.imread('verde.jpg')
        
    def acomodarColor(self):
        for f in range(self.fila):
            for c in range(self.columna):   
                self.lista.append(self.data[f][c])
                
                
        lista_nueva = []
        for i in self.lista:
            if self.buscarEnLista(lista_nueva,i)==False:
                lista_nueva.append(i)
        print len(self.lista),len(lista_nueva)       
    
    def buscarEnLista(self,lista,valor):
        for i in lista:
            if i[0]==valor[0] and i[1]==valor[1] and i[2]==valor[2]:
                return True
        return False
         
        
       
                
        
