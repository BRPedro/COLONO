import cv2
import numpy as np
import threading

class ConteoCombinado:
    def __init__(self, direccion):
        print "hola"
        self.dir = direccion
        self.imagen = cv2.imread(direccion)
        self.matrizOrig = np.array(self.imagen)
        self.fila, self.columna, self.tipo = self.imagen.shape
        self.newData = np.zeros(shape=(self.fila, self.columna))
        self.centroides=[]

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

        self.centroides=[]

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

    #Comprueba que uno de los 8 vecinos cercanos tenga un color similar, si lo tiene retorna True y sino False
    def busquedaConPeso(self, f, c, peso, lista):
        for i in lista:
            if (peso==i[1] or peso-1==i[1]  or peso+1==i[1] ):# or peso+2==i[1] or peso-2==i[1]):
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

    # Agrupa valores vecinos y que tenga un peso similar
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


    def listaErosion(self):

        kernel11 = np.ones((4, 4), np.uint8)
        gris2 = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("gris.jpg",gris2)
        erosion = cv2.erode(gris2, kernel11, iterations=1)
        matrizEro = np.array(gris2)

        listaEro = []
        filas, columnas, tipo = self.imagen.shape
        print "hola2"
        for f in range(filas):
            for c in range(columnas):
                listaEro.append([[[f, c], matrizEro[f][c]]])
        print "hola3"

        self.metodoHilosAgrupar(listaEro,1)
        print "hola4"

        for i in self.lista1:
            self.centroideCuadrado(i)
        print "hola5"

        for i in self.centroides:
            cv2.circle(self.imagen, (i[0], i[1]), 1, (255, 0, 0), 0)
        cv2.imwrite('contadoeee.jpg', self.imagen)



    def centroideCuadrado(self,lista):
        maxF,maxC=0,0
        minF,minC=self.fila-1,self.columna-1
        for temp in lista:
            if temp[0][0]>maxF: maxF=temp[0][0]
            elif temp[0][0]<minF: minF=temp[0][0]
            if temp[0][1]>maxC: maxC=temp[0][1]
            elif temp[0][1]<minC:minC=temp[0][1]

        self.centroides.append([(((maxC-minC) / 2) + minC), (((maxF-minF) / 2) + minF)])

    def contarEscala(self):
        imagen=cv2.imread(self.dir)
        matriz = np.array(imagen)
        f,c,t=imagen.shape

        lista=[]
        for ff in range(f):
            for cc in range(c):
                rojo, verde, azul = matriz[ff][cc]
                if(lista.count([rojo,verde,azul])==0):
                    lista.append([rojo,verde,azul])
        print len(lista)




    def burbuja(self,lista):
        numero = len(lista)
        i= 0
        while (i < numero):
            j = i
            while (j < numero):
                if(len(lista[i]) > len(lista[j])):
                    temp = lista[i]
                    lista[i] = lista[j]
                    lista[j] = temp
                j= j+1
            i=i+1
        return lista

    def mi_contadorAgrupado(self):
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
        print len(listapuntos)
        listapuntos=self.borrarXcantidadElemento(listapuntos,2)
        print len(listapuntos)
        listapuntos=self.burbuja(listapuntos)
        print len(listapuntos)
        listapuntos=self.agrupamientoXproximidad2(listapuntos,20)
        print len(listapuntos)
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
            self.centroides.append([((maxC-minC) / 2) + minC,((maxF-minF) / 2) + minF])
            tem = cv2.imread(self.dir)
            for i in self.centroides:
                cv2.circle(tem, (i[0], i[1]), 6, (0, 0, 255), 0)
            cv2.imwrite('contado1.jpg', tem)

    def borrarXcantidadElemento(self,lista,limite):
        listaT=[]
        for i in lista:
            if len(i)>limite:
                listaT.append(i)
        listaT=self.burbuja(listaT)
        return listaT

    def puntoCentralGrupo(self,lista):
        maxF,maxC=0,0
        minF,minC=self.fila-1,self.columna-1
        for temp in lista:
            if temp[0]>maxF: maxF=temp[0]
            if temp[0]<minF: minF=temp[0]
            if temp[1]>maxC: maxC=temp[1]
            if temp[1]<minC:minC=temp[1]
        return [((maxF-minF) / 2) + minF,((maxC-minC) / 2) + minC]
        #return [(((maxC-minC) / 2) + minC), (((maxF-minF) / 2) + minF)]

    def distaciaEntrePuntos(self,coordenada1, coordenada2):
        res=(((coordenada2[0]-coordenada1[0])**2)+((coordenada2[1]-coordenada1[01])**2))**0.5
        if(res<0):res*=-1
        return res

    def distaciaEntrePatrones(self,patron1,patron2,limite):
        resultado=self.distaciaEntrePuntos(self.puntoCentralGrupo(patron1),self.puntoCentralGrupo(patron2))

        if resultado<=float(limite):return True
        return False

    def agrupamientoXproximidad(self, listaGrupos,limite):
        i=0
        while i<len(listaGrupos)-1:
            largo=len(listaGrupos)
            indice=i+1
            while indice<largo:
                if (self.distaciaEntrePatrones(listaGrupos[i],listaGrupos[indice],limite)):
                    if len(listaGrupos[indice])>len(listaGrupos[i]):
                        listaGrupos.pop(i)
                    else:
                        listaGrupos.pop(indice)
                        indice+=1
                    largo=len(listaGrupos)
                else:
                    indice+=1

        return listaGrupos

    def agrupamientoXproximidad2(self, listaGrupos,limite):###########
        print "agrupamientoXproximidad2"

        while True:
            bandera=True
            i1=0
            while i1<len(listaGrupos)-1:
                i2=i1+1
                bandera2=True
                while i2<len(listaGrupos):
                    if (self.distaciaEntrePatrones(listaGrupos[i1],listaGrupos[i2],limite)):
                        if len(listaGrupos[i1])>len(listaGrupos[i2]):
                            listaGrupos.pop(i2)
                        else:
                            listaGrupos.pop(i1)
                        bandera2=False
                        break

                    i2+=1
                if bandera2==False:
                    bandera=False
                    break
                i1+=1
            if bandera:
                break
        return listaGrupos


n=ConteoCombinado("C:\\Users\\PBR\\Documents\\NetBeansProjects\\COLONO\\COLONO\\DEMO2\\src\\corte.jpg")
n.mi_contadorAgrupado()
#n.listaErosion()
