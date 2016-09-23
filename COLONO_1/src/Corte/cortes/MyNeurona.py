import numpy as np
import neurolab as nl
import cv2

min_value = 0
max_value = 255

listcarg=[]

for i in range(4,16):
    listatem=[]
    imagen=cv2.imread("corte"+str(i)+".jpg")
    data = np.array(imagen)

    filas, columnas, tipo = imagen.shape
    for f in range(filas):
        for c in range(columnas):
            rojo, verde, azul = data[f][c]
            promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
            listatem.append(promedio)
    listcarg.append(listatem)


listasalida=[[1]]*12
for t in listcarg:
    print len(t)
print  listasalida


net=nl.net.newff(([[min_value,max_value]]*1600), [10, 10, 1])


net.trainf = nl.train.train_gd



error = net.train(listcarg, listasalida, epochs=10000, show=1000, goal=0.0001)

listatem=[]
imagen=cv2.imread("corte1.jpg")
data = np.array(imagen)

filas, columnas, tipo = imagen.shape
for f in range(filas):
    for c in range(columnas):
        rojo, verde, azul = data[f][c]
        promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
        listatem.append(promedio)
listcarg.append(listatem)

predicted_output = net.sim([listatem])
print predicted_output

listatem=[]
imagen=cv2.imread("corte11.jpg")
data = np.array(imagen)

filas, columnas, tipo = imagen.shape
for f in range(filas):
    for c in range(columnas):
        rojo, verde, azul = data[f][c]
        promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
        listatem.append(promedio)
listcarg.append(listatem)

predicted_output = net.sim([listatem])
print predicted_output