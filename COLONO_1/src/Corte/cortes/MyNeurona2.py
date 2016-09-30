import numpy as np
import neurolab as nl
import cv2

min_value = 0
max_value = 255

listcarg=[]

listasalida=[[1]]
for t in listcarg:
    print len(t)
print  listasalida


net=nl.net.newff(([[min_value,max_value]]*(1600*3)), [2, 2, 1])


net.trainf = nl.train.train_gd

for contar in range(1,10):
    listatem = []
    imagen = cv2.imread("corte1_" + str(contar) + ".jpg")
    data = np.array(imagen)
    filas, columnas, tipo = imagen.shape
    for f in range(filas):
        for c in range(columnas):
            rojo, verde, azul = data[f][c]
            promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
            listatem.append(promedio)

    imagen = cv2.imread("corte2_" + str(contar) + ".jpg")
    data = np.array(imagen)
    filas, columnas, tipo = imagen.shape
    for f in range(filas):
        for c in range(columnas):
            rojo, verde, azul = data[f][c]
            promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
            listatem.append(promedio)

    imagen = cv2.imread("corte3_" + str(contar) + ".jpg")
    data = np.array(imagen)
    filas, columnas, tipo = imagen.shape
    for f in range(filas):
        for c in range(columnas):
            rojo, verde, azul = data[f][c]
            promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
            listatem.append(promedio)

    listcarg.append(listatem)
    error = net.train(listcarg, listasalida, epochs=10, show=10, goal=0.01)
    listcarg=[]
    print contar



    def crearmMatrizImag(dir):
        matrizImg=[]
        imagen = cv2.imread(dir)
        data = np.array(imagen)
        filas, columnas, tipo = imagen.shape
        for f in range(filas):
            for c in range(columnas):
                rojo, verde, azul = data[f][c]
                promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
                matrizImg.append(promedio)
        return matrizImg

"""
listatem = []
imagen = cv2.imread("corte1_3.jpg")
data = np.array(imagen)
filas, columnas, tipo = imagen.shape
for f in range(filas):
    for c in range(columnas):
        rojo, verde, azul = data[f][c]
        promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
        listatem.append(promedio)

imagen = cv2.imread("corte2_3.jpg")
data = np.array(imagen)
filas, columnas, tipo = imagen.shape
for f in range(filas):
    for c in range(columnas):
        rojo, verde, azul = data[f][c]
        promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
        listatem.append(promedio)

imagen = cv2.imread("corte3_3.jpg")
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



listatem = []
imagen = cv2.imread("corte1_11.jpg")
data = np.array(imagen)
filas, columnas, tipo = imagen.shape
for f in range(filas):
    for c in range(columnas):
        rojo, verde, azul = data[f][c]
        promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
        listatem.append(promedio)

imagen = cv2.imread("corte2_11.jpg")
data = np.array(imagen)
filas, columnas, tipo = imagen.shape
for f in range(filas):
    for c in range(columnas):
        rojo, verde, azul = data[f][c]
        promedio = ((int(rojo) + int(verde) + int(azul)) // 3)
        listatem.append(promedio)

imagen = cv2.imread("corte3_11.jpg")
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
"""