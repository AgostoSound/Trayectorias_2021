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

def plotea(ax, df):

    print('VAMOS A MORIR TODOS')

    posX, posY, vt = [], [], []

    for i in range(len(df['Estado'])):
        if df['Estado'][i] == 1:
            posX.append(df['X'][i])
            posY.append(df['Y'][i])
            vt.append(df['Tmilisegundos'][i])
        else:
            break
    ax.plot3D(posX, posY, vt, color='red', lw=1.5, label='')

def graficadora2(df):
    # Dibuja el desplazamiento
    ax = plt.axes(projection='3d')
    # ax.plot3D(posX, posY, vt, 'red', lw=1.5, label='Poner label')

    plotea(ax, df)

    # Seccion de labels y textos
    ax.set_xlabel('X (pixels)')
    ax.set_ylabel('Y (pixels)')
    ax.set_zlabel('Tiempo (ms)')

    # Delimita la zona a mostrar
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    # ax.set_zlim(0, 10)

    # Dibuja rectangulo en el suelo = total de pantalla de pruebas
    # p = Rectangle((0, 0), 900, 600, color='black', alpha=0.15, fc='yellow')
    # ax.add_patch(p)
    # art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    # Dibuja figura en el suelo

    # Genera nombre y guarda / muestra
    plt.show()

def graficadora(posX, posY, vt, e):
    # Dibuja el desplazamiento
    ax = plt.axes(projection='3d')
    # ax.plot3D(posX, posY, vt, 'red', lw=1.5, label='Poner label')

    plotea(ax, posX, posY, vt, e)

    # Seccion de labels y textos
    ax.set_xlabel('X (pixels)')
    ax.set_ylabel('Y (pixels)')
    ax.set_zlabel('Tiempo (ms)')

    # Delimita la zona a mostrar
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    # ax.set_zlim(0, 10)

    # Dibuja rectangulo en el suelo = total de pantalla de pruebas
    # p = Rectangle((0, 0), 900, 600, color='black', alpha=0.15, fc='yellow')
    # ax.add_patch(p)
    # art3d.pathpatch_2d_to_3d(p, z=0, zdir="z")

    #Dibuja figura en el suelo

    # Genera nombre y guarda / muestra
    plt.show()

def Cuadrado(ax):

    x1 = [-197, 180, 180, -197]
    y1 = [-164, -164, -164, -164]
    z1 = [0, 0, 40, 40]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

    x2 = [180, 180, 180, 180]
    y2 = [189, -164, -164, 189]
    z2 = [0, 0, 40, 40]
    vert_2 = [list(zip(x2, y2, z2))]
    ax.add_collection3d(Poly3DCollection(vert_2, color='m', linewidths=0.3, alpha=0.1))

    x3 = [-197, 180, 180, -197]
    y3 = [189, 189, 189, 189]
    z3 = [0, 0, 40, 40]
    vert_3 = [list(zip(x3, y3, z3))]
    ax.add_collection3d(Poly3DCollection(vert_3, color='m', linewidths=0.3, alpha=0.1))

    x4 = [-197, -197, -197, -197]
    y4 = [189, -164, -164, 189]
    z4 = [0, 0, 40, 40]
    vert_4 = [list(zip(x4, y4, z4))]
    ax.add_collection3d(Poly3DCollection(vert_4, color='m', linewidths=0.3, alpha=0.1))

def Triangulo(ax):
    x1 = [-269, 249, 249, -269]
    y1 = [-223, -223, -223, -223]
    z1 = [0, 0, 40, 40]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

    x2 = [-269, -10, -10, -269]
    y2 = [-223, 244, 244, -223]
    z2 = [0, 0, 40, 40]
    vert_2 = [list(zip(x2, y2, z2))]
    ax.add_collection3d(Poly3DCollection(vert_2, color='m', linewidths=0.3, alpha=0.1))

    x3 = [249, -10, -10, 249]
    y3 = [-223, 244, 244, -223]
    z3 = [0, 0, 40, 40]
    vert_3 = [list(zip(x3, y3, z3))]
    ax.add_collection3d(Poly3DCollection(vert_3, color='m', linewidths=0.3, alpha=0.1))


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

            graficadora2(df_format)
            # graficadora(posX, posY, vec_time, estado)
            break
        break

main(vec_in, subdir_comun, dir_out)