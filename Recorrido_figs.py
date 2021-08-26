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
# dir_input = './Pruebas Piloto' # carpeta de ENSAYOS
# vec_in = os.listdir(dir_input) # lista de subcarpetas de ensayos
# subdir_comun = '/Suj1/Recorridos/' # fragmento de direccion comun a todos
# dir_out = './SALIDAS'

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
            ax.plot3D(pX, pY, vT, color='lightgreen', lw=1.5, label='')

def graficadora(df, para_title, ruta_save, figura):

    # Dibuja el desplazamiento

    fig = plt.figure(figsize=(8,8)) # tamaño de la figura
    # ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(projection='3d')

    # graficador simple
    # ax.plot3D(posX, posY, vt, 'darkblue', lw=1.5, label='Poner label')

    # FUNCION MAGICA - plotea de distinto color segun está dentro o fuera de la figura
    plotea(ax, df)

    # Seccion de labels y textos
    fig.suptitle('Trayectoria - Ensayo: ' + para_title, fontsize=16)
    ax.set_xlabel('X (pixels)')
    ax.set_ylabel('Y (pixels)')
    ax.set_zlabel('Tiempo (ms)')

    # Delimita la zona a mostrar
    ax.set_xlim(0, 900)
    ax.set_ylim(0, 600)
    # ax.set_zlim(0, 10)

    # colocar aqui una condicion para elegir la figura del suelo
    if figura == 0:
        Figura_1(ax)
    elif figura == 1:
        Figura_2(ax)
    elif figura == 2:
        Figura_3(ax)
    # elif figura == 3: # a la espera de nuevos datos
    #     Figura_3(ax)

    ax.invert_xaxis()
    ax.set_ylim(0, 600)

    ax.view_init(None, 120) #controla el angulo de vision inicial (elevacion, azimuth)

    # Genera nombre y guarda / muestra
    plt.savefig(ruta_save)
    # plt.show()

def Figura_0(ax): # TRIANGULO DE FAMILIARIZACION
    # Puntos en (x y z) que forman el polígono
    x1 = [185, 630, 630, 330, 330, 560, 560, 330, 330]
    y1 = [530, 85, 530, 530, 460, 460, 230, 460, 530]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

def Figura_1(ax): # PARECE UN ENTER, PONELE
    # Puntos en (x y z) que forman el polígono
    x1 = [220, 680, 680, 430, 430, 220, 220, 290, 290, 500, 500, 610, 610, 220]
    y1 = [80, 80, 530, 530, 340, 340, 150, 150, 270, 270, 460, 460, 150, 150]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

def Figura_2(ax): # FLECHA APUNTANDO ABAJO A LA IZQUIERDA
    # Puntos en (x y z) que forman el polígono
    x1 = [200, 200, 480, 480, 700, 430, 270, 270, 410, 550, 410, 410, 270, 270]
    y1 = [550, 320, 50, 270, 270, 550, 550, 480, 480, 340, 340, 200, 340, 550]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

def Figura_3(ax): # NI PABLO PICASSO SE ATREVIÓ A TANTO
    # Puntos en (x y z) que forman el polígono
    x1 = [480, 180, 295, 450, 760, 635, 480, 480, 590, 660, 450, 340, 270, 480]
    y1 = [450, 565, 125, 260, 145, 585, 450, 380, 480, 240, 330, 230, 470, 380]
    z1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vert_1 = [list(zip(x1, y1, z1))]
    ax.add_collection3d(Poly3DCollection(vert_1, color='m', linewidths=0.3, alpha=0.1))

#____________________________  PRINCIPAL  _____________________________________
def main_rf(vec_in, subdir_comun, dir_out, dir_input):

    for ensayo in vec_in:  # iterador principal de carpetas 001 002 ...
        dir_rec = dir_input + '/' + ensayo + subdir_comun  # se posiciona dentro de la carpeta Recorridos de cada ensayo
        vec_rec = os.listdir(dir_rec)  # lista de pruebas de cada ensayo

        dir_metadata = dir_input + '/' + ensayo + '/Suj1/' + ensayo + '_1.csv' #ruta de metadata
        metadata = pd.read_csv(dir_metadata, delimiter=';', decimal=',') # abre metadata en una matriz
        df_metadata = pd.DataFrame(metadata) # convierte a DataFrame

        for rec in vec_rec:  # iterador secundario para cada prueba
            to_open = dir_rec + rec  # directorio util para abrir .csv

            # CON ESTA LINEA SE LEVANTA UN ARCHIVO CONCRETO
            # Si se va a usar hay que encender los break de abajo
            # to_open = './Pruebas Piloto/025/Suj1/Recorridos/025_1_01.csv'

            arch_open = pd.read_csv(to_open, delimiter=';', decimal=',')  # abre el csv

            para_title = os.path.splitext(rec)[0]
            ruta_save = dir_out + '/' + ensayo + '/' + para_title + '_t3D.png'  # directorio de salida

            df_format = pd.DataFrame(arch_open)  # convierte a data frame

            num_rec = int(rec[7]) - 1
            fig = int(df_metadata['FiguraExplorada'][num_rec])

            # posX, posY, vec_time, estado = df_format['X'], df_format['Y'], df_format['Tmilisegundos'], df_format['Estado']

            graficadora(df_format, para_title, ruta_save, fig)

            # break
        # break

# main_rf(vec_in, subdir_comun, dir_out, dir_input)