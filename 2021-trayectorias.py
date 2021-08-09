#_______________________________ LIBRERIAS ____________________________________
import os
import Speed_Plotter as sp

#_______________________________ HARD CODE ____________________________________
dir_input = './Pruebas Piloto' # carpeta de ENSAYOS
vec_in = os.listdir(dir_input) # lista de subcarpetas de ensayos
subdir_comun = '/Suj1/Recorridos/' # fragmento de direccion comun a todos
dir_out = './SALIDAS'

#_______________________________ FUNCIONES ____________________________________

def imprime_menu(): # MENU PRINCIPAL
    print('')
    print('-----------------------------------------------------------------')
    print('             - ANALISIS DE TRAYECTORIAS 2021 - ')
    print('-----------------------------------------------------------------')
    print('')
    print(' 1 - Generar gráficas de velocidad')
    print(' 2 - Generar gráficas 3D de trayectorias')
    print(' 0 - Finalizar')

def imprime_op1():
    print('')
    print('--------------------------------------------------------------')
    print('             - GRAFICADORA DE VELOCIDADES - ')
    print('--------------------------------------------------------------')
    print('')
    print(' 1 - Utilizar valores con signo')
    print(' 2 - Convertir a valores absolutos')
    print(' 0 - Volver')

def valida_op(): # valida los ingresos por teclado para opciones entre 1 o 2
    nums = '120'
    op = input('\n -Ingrese opcion deseada: ')
    while op not in nums or len(op) != 1: #si el ingreso no esta en nums o tiene largo distinto de 1 entra en el bucle
        op = input(' -Error, ingrese una opcion valida: ')
    return int(op)

#____________________________  PRINCIPAL  _____________________________________
def main():
    op = -1  # inicia opcion en -1 para forzar el bucle
    while op != 0:  # ciclo que controla el menu principal
        imprime_menu()
        op = valida_op()  # carga opcion principal

        # GRAFICADORA DE VELOCIDADES
        if op == 1:
            op1 = -1  # inicia opcion en -1 para forzar el bucle
            while op1 != 0:  # ciclo que controla menu secundario
                imprime_op1()
                op1 = valida_op()  # elección de valores abs o no
                if op1 == 0:  # excepción para retroceder al menu principal sin
                    continue  # hacer nada más luego de ingresado un cero

                # Aqui ejecuta toda la rama del speed plotter desde el otro scipt
                sp.speed_ploter(op1, vec_in, dir_input, subdir_comun, dir_out)

        # GRAFICADORA DE TRAYECTORIAS
        elif op == 2:
            pass  # AQUI VA LA GRAFICADORA 3D
        else:
            print('\n--------------------------------')
            print(' - El programa ha finalizado -')
            print('--------------------------------')

main()

