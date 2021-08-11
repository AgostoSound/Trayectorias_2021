#_______________________________ LIBRERIAS ____________________________________
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits import mplot3d
from matplotlib.patches import Rectangle
import mpl_toolkits.mplot3d.art3d as art3d

#___________________________ BORRAR HARD CODE__________________________________
dir_input = './Pruebas Piloto' # carpeta de ENSAYOS
vec_in = os.listdir(dir_input) # lista de subcarpetas de ensayos
subdir_comun = '/Suj1/Recorridos/' # fragmento de direccion comun a todos
dir_out = './SALIDAS'

#_______________________________ FUNCIONES ____________________________________

def plotea(ax, df_gordo):

    vec_changes = [] # vector que almacena los index de cambios
    flag = False # banderita traviesa
    estado_anterior = -1 #hace que siempre agregue el 0 como primer elemento del vec de cambios

    # recorre hasta el penultimo index del DF
    for i in range(len(df_gordo['X'])-1):
        elem = df_gordo[:][i:i+1] # levanta una sola fila
        estado_actual = int(elem['Estado']) # guarda el valor del casillero "e" y lo vuelve entero

        # tal como está, siempre da TRUE en la primera vuelta
        if estado_actual != estado_anterior:
            vec_changes.append(i)
        estado_anterior = estado_actual

    # recorre el vector de cambios - setea limites inf. y sup.
    for j in range(len(vec_changes)-1):
        l_inf, l_sup = vec_changes[j], vec_changes[j+1]
        df_pedazo = df_gordo[:][l_inf:l_sup] # dataFrame cortado

        # vectores parciales para ir a cada color
        pX, pY, vT, vE = df_pedazo['X'], df_pedazo['Y'], df_pedazo['Tmilisegundos'], df_pedazo['Estado']

        # condicion de ploteado
        if int(vE[l_inf]) == 0:
            ax.plot3D(pX, pY, vT, color='red', lw=1.5, label='')
        elif int(vE[l_inf]) == 1:
            ax.plot3D(pX, pY, vT, color='orange', lw=1.5, label='')

def graficadora(df):
    # Dibuja el desplazamiento

    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(projection='3d')

    # graficador simple
    # ax.plot3D(posX, posY, vt, 'darkblue', lw=1.5, label='Poner label')

    # FUNCION MAGICA - plotea de distinto color segun está dentro o fuera de la figura
    plotea(ax, df)

    # Seccion de labels y textos
    ax.set_xlabel('X (pixels)')
    ax.set_ylabel('Y (pixels)')
    ax.set_zlabel('Tiempo (ms)')

    # Delimita la zona a mostrar
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    # ax.set_zlim(0, 10)

    Figura_1(ax)

    # ax.invert_yaxis()
    ax.invert_xaxis()

    ax.set_ylim(0, 600)

    # Genera nombre y guarda / muestra

    plt.show()

def Figura_1(ax):
    # Puntos en (x y z) que forman el polígono
    x1 = [150, 150, 490, 490, 740, 420, 230, 230, 400, 580, 410, 410, 230, 230]
    y1 = [600, 310, 0, 260, 260, 600, 600, 520, 520, 340, 340, 170, 350, 600]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

def Figura_2(ax):
    # Puntos en (x y z) que forman el polígono
    x1 = [480, 20, 280, 450, 890, 670, 480, 480, 640, 770, 450, 300, 150, 480]
    y1 = [450, 600, 130, 260, 20, 580, 450, 380, 490, 160, 330, 230, 490, 380]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

def Figura_3(ax):
    # Puntos en (x y z) que forman el polígono
    x1 = [200, 700, 700, 410, 410, 200, 200, 280, 280, 490, 490, 620, 620, 200]
    y1 = [60, 60, 550, 550, 340, 340, 140, 140, 260, 260, 470, 470, 140, 140]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

#____________________________  PRINCIPAL  _____________________________________
def main(vec_in, subdir_comun, dir_out):

    for ensayo in vec_in:  # iterador principal de carpetas 001 002 ...
        dir_rec = dir_input + '/' + ensayo + subdir_comun  # se posiciona dentro de la carpeta Recorridos de cada ensayo
        vec_rec = os.listdir(dir_rec)  # lista de pruebas de cada ensayo

        for rec in vec_rec:  # iterador secundario para cada prueba
            to_open = dir_rec + rec  # directorio util para abrir .csv

            # AUXILIAR, BORRAR
            to_open = './Pruebas Piloto/025/Suj1/Recorridos/025_1_01.csv'

            arch_open = pd.read_csv(to_open, delimiter=';', decimal=',')  # abre el csv
            para_title = os.path.splitext(rec)[0]
            ruta_save = dir_out + '/3D_' + para_title + '.png'  # directorio de salida

            df_format = pd.DataFrame(arch_open)  # convierte a data frame

            # posX, posY, vec_time, estado = df_format['X'], df_format['Y'], df_format['Tmilisegundos'], df_format['Estado']

            graficadora(df_format)
            break
        break

main(vec_in, subdir_comun, dir_out)