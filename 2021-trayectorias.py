# LIBRERIAS
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# CARPETAS IN-OUT
dir_input = './Pruebas Piloto/025/Suj1/Recorridos'
vec_in = os.listdir(dir_input)
dir_out = './SALIDAS'

# FUNCIONES

def es_divisible(largo):
    # esta funcion sirve para calcular un valor optimo para los intervalos
    # toma la longitud del arreglo y revisa si es divisible por algun entero del 1 al 55 y
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
    s = 0 # punto de partida
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
        xi = mat_aux['X'][s]
        xf = mat_aux['X'][d-1]
        yi = mat_aux['Y'][s]
        yf = mat_aux['Y'][d-1]

        # calcula la distancia recorrida por cada eje
        # Condicion para convertir o no a valores absolutos
        if op == 1:
            dx = abs(xf - xi)
            dy = abs(yf - yi)
        else:
            dx = xf - xi
            dy = yf - yi

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
    mat = pd.DataFrame({'Tiempo':vec_time ,
                   'Vel X':vx_dup ,
                   'Vel Y': vy_dup})

    
    return mat

def graficadora(mat_vel, delta, ruta):
    # convierte los vectores a tipo de dato numerico
    t, vx, vy = np.array(mat_vel['Tiempo']), np.array(mat_vel['Vel X']), np.array(mat_vel['Vel Y'])

    # Crea la figura y el subplot
    fig, ax = plt.subplots()
    ax.plot(t, vx, label='Suj X')
    ax.plot(t, vy, label='Suj Y')
    subtit = 'Intervalo de muestra cada ' + str(delta) + ' milisegundos'
    ax.set(xlabel='Tiempo (ms)', ylabel='Vel (px/ms)',
           title=subtit)

    fig.suptitle('Variacion de velocidad entre sujetos', fontsize=16)
    ax.legend()
    ax.grid()

    plt.savefig(ruta, dpi=199)
    plt.show()

# LOGICA PRINCIPAL
op = int(input('\nConvertir a positivo: 0 No - 1 Si: '))
for rec in vec_in: # iterador principal
    to_open = dir_input + '/' + rec  # crea directorio util
    arch_open = pd.read_csv(to_open, delimiter=';') # abre el csv
    ruta_save = dir_out + '/' + os.path.splitext(rec)[0] + '.png'

    df_format = pd.DataFrame(arch_open) # convierte a data frame
    df_f2 = df_format.transpose() # Matrix transpuesta (auxiliar)
    largo_set = len(df_format) # Longitud del arreglo
    vec_time = df_format['Tmilisegundos']

    delta = es_divisible(largo_set) # carga el valor del intervalo
    vec_Vx, vec_Vy = calc_vel(df_format, delta, largo_set, op) # crea vectores de velocidad
    mat_vel = crea_mat_vel(vec_Vx, vec_Vy, delta, vec_time) # nueva matrix con velocidades
    graficadora(mat_vel, delta, ruta_save)
    # break