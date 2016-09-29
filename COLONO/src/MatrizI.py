# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import nodo
import numpy as np

__author__ = "PBR"
__date__ = "$28/09/2016 01:57:20 PM$"

class Matriz:
    def __init__(self,imagenM):        
        self.matriz=[]
        self.filas=len(imagenM)
        self.columnas=len(imagenM[0])
        self.matriz=np.zeros(shape=(self.filas,self.columnas))
        self.centroides=[]
        self.vectore=[]
        for f in range(self.filas):
            for c in range(self.columnas):
                if imagenM[f][c]==1:
                    self.matriz[f][c]=nodo.Nodo(1,f,c)
                else:
                    self.matriz[f][c]=nodo.Nodo(0,f,c)
    
    def colocarVesinos(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if self.matriz[f][c].valor==1:
                    if f-1>=0 and c-1>=0:
                        if self.matriz[f-1][c-1].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f-1][c-1])
                        
                    if f-1>=0:
                        if self.matriz[f-1][c].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f-1][c])
                        
                    if f-1>=0 and c+1<self.columnas:
                        if self.matriz[f-1][c+1].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f-1][c+1])
                            
                    if c+1<self.columnas:
                        if self.matriz[f][c+1].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f][c+1])
                    
                    if f+1<self.filas and c+1<self.columnas:
                        if self.matriz[f+1][c+1].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f+1][c+1])
                            
                    if f+1<self.filas:
                        if self.matriz[f+1][c].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f+1][c])
                    
                    if f+1<self.filas and c-1>=0:
                        if self.matriz[f+1][c-1].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f+1][c-1])
                            
                    if c-1>=0:
                        if self.matriz[f][c-1].valor==1:
                            self.matriz[f][c].set_vesinos(self.matriz[f][c-1])
        