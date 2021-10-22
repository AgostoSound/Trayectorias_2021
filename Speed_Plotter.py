#_______________________________ LIBRERIAS ____________________________________
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

#_______________________________ HARD CODE ____________________________________
# hasta ahora no es necesaria desde este fragmento

#_______________________________ FUNCIONES ____________________________________
def es_divisible(largo):
    # esta funcion sirve para calcular un valor optimo para los intervalos
    # toma la longitud del arreglo y revisa si es divisible por algun entero del 1 al 300 y
    # luego de notificar las opciones procede a pedir el valor elegido

    print('\n - El largo del arreglo es de ' + str(largo) + ' ms - ')

    vec_divisores = []
    for i in range(1, 300):
        if largo % i == 0:
            vec_divisores.append(i)

    print('\nEs divisible por ' + str(vec_divisores))

    return int(input('Elija longitud del intervalo: '))

def calc_vel(mat, delta, long, op):
    # mat: matriz encolumnada tipo data frame
    # delta: longitud del intervalo
    # long: longitud del arreglo

    l = long
    s = 0 # start - punto de partida
    d = delta
    cant_inter = l // d # calcula total de intervalos
    # cant_inter = 150 # para pruebas
    vec_vel_x = []
    vec_vel_y = []

    for i in range(cant_inter): # itera por cantidad de intervalos
        # intervalo = 'Intervalo ' + str(i+1)
        # print('\n' + intervalo)

        mat_aux = mat[s:d] # matriz solo con elementos del intervalo actual
        # print(mat_aux)

        # extrae posiciones iniciales y finales en X e Y
        xi = int(mat_aux['X'][s])
        xf = int(mat_aux['X'][d-1])
        yi = int(mat_aux['Y'][s])
        yf = int(mat_aux['Y'][d-1])

        # calcula la distancia recorrida por cada eje
        # Condicion para convertir o no a valores absolutos
        if op == 1:
            dx = xf - xi
            dy = yf - yi
        elif op == 2:
            dx = abs(xf - xi)
            dy = abs(yf - yi)

        # calcula la velocidad como distancia recorrida (en pixeles)
        # dividido el tiempo empleado (largo del intervalo en milisegundos)
        vx = round(dx / delta, 3)
        vy = round(dy / delta, 3)
        # LA VELOCIDAD EN EL TRAMO NO REPRESENTA UN PROMEDIO NECESARIAMENTE FIEL
        # AL COMPORTAMIENTO DE LAS VARIACIONES DE VELOCIDAD INTERNAS AL INTERVALO

        # almacena en vectores todas las velocidades calculadas
        vec_vel_x.append(vx)
        vec_vel_y.append(vy)

        # aumenta el valor de los limites del intervalo para la proxima vuelta
        s += delta
        d += delta
        if d > long: # ante un valor de intervalo no divisible por el largo del arreglo de manera entera
            break    # se truncarán los samples que falten para completar dicho largo

    return vec_vel_x, vec_vel_y

def crea_mat_vel(vec_Vx, vec_Vy, delta, vec_time):
    # Genera una tabla de 3 columnas Tiempo - Vel X - Vel Y

    # bloque que genera vector de velocidades concatenando cada
    # tantos samples como indica el intervalo
    vx_dup, vy_dup = [], []
    for i in range(len(vec_Vx)):
        for j in range(delta):
            vx_dup.append(vec_Vx[i])
            vy_dup.append((vec_Vy[i]))

    # Genera tabla
    tope_sup = delta * len(vec_Vx)
    mat = pd.DataFrame({'Tiempo':vec_time[:tope_sup], # este index determina el tope a partir de cual
                   'Vel X':vx_dup,                   # se truncarán los samples
                   'Vel Y': vy_dup})

    return mat

def graficadora(mat_vel, delta, ruta, para_title):
    # convierte los vectores a tipo de dato numerico
    t, vx, vy = np.array(mat_vel['Tiempo']), np.array(mat_vel['Vel X']), np.array(mat_vel['Vel Y'])

    # Crea la figura y el subplot
    fig, ax = plt.subplots()
    ax.plot(t, vx, label='Suj X')
    ax.plot(t, vy, label='Suj Y')
    subtit = 'Intervalo de muestra cada ' + str(delta) + ' samples'
    ax.set(xlabel='Samples', ylabel='Vel (px/sample)',
           title=subtit)

    fig.suptitle('Velocidad entre sujetos - Ensayo: ' + para_title, fontsize=16)
    ax.legend()
    ax.grid()

    plt.savefig(ruta, dpi=199)
    # plt.show()

#____________________________  PRINCIPAL  _____________________________________
def speed_ploter(op1, vec_in, dir_input, subdir_comun, dir_out, delta_comun):

    # control de flujo para el uso o no de intervalo comun
    # si delta_comun ingresa como -1 significa que no desea un intervalo comun
    flag_delta = False
    if delta_comun != -1:
        flag_delta = True

    print('\n - Se están generando las gráficas, aguarde un momento... ')

    for ensayo in vec_in:  # iterador principal de carpetas 001 002 ...
        dir_rec = dir_input + '/' + ensayo + subdir_comun  # se posiciona dentro de la carpeta Recorridos de cada ensayo
        vec_rec = os.listdir(dir_rec)  # lista de pruebas de cada ensayo

        for rec in vec_rec:  # iterador secundario para cada prueba
            to_open = dir_rec + rec  # directorio util para abrir .csv
            arch_open = pd.read_csv(to_open, delimiter=';', decimal=',')  # abre el csv
            para_title = os.path.splitext(rec)[0]

            if op1 == 1:
                ruta_save = dir_out + '/' + ensayo + '/' + para_title + 'Signos.png'  # directorio de salida
            elif op1 == 2:
                ruta_save = dir_out + '/' + ensayo + '/' + para_title + 'Absolutos.png'

            df_format = pd.DataFrame(arch_open)  # convierte a data frame
            df_f2 = df_format.transpose()  # Matrix transpuesta (auxiliar)
            largo_set = len(df_format)  # Longitud del arreglo
            vec_time = df_format['Tmilisegundos']

            # si la bandera esta arriba setea el delta tal como ingresó
            if flag_delta:
                delta = delta_comun
            # si la bandera esta baja pide un intervalo por cada ensayo
            else:
                delta = es_divisible(largo_set)  # carga el valor del intervalo

            vec_Vx, vec_Vy = calc_vel(df_format, delta, largo_set, op1)  # crea vectores de velocidad
            mat_vel = crea_mat_vel(vec_Vx, vec_Vy, delta, vec_time)  # nueva matrix con velocidades
            graficadora(mat_vel, delta, ruta_save, para_title)

            # break
        # break