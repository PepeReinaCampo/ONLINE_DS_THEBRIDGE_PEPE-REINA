import numpy as np
import time

def selector_tamaño():
    while True:
        x = input("¿DE QUÉ TAMAÑO DESEA SU TABLERO? El tablero será cuadrado. ") 
        if not x.isdigit():
            print("INGRESE SOLO VALORES NUMÉRICOS POSITIVOS")
        else:
            x = int(x)

            if x == 0:
                print("JO JO JO... MUY GRACIOSO")
            elif x < 7:
                print("EL TAMAÑO DEL TABLERO DEBE SER COMO MÍNIMO DE 7") 
            elif x < 25:
                print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                return x          
            elif x == 25:
                print("WOW... TE GUSTA EL JUEGO")
                print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                return x
            else:
                print(x, "ES DEMASIADO, POSIBLEMENTE SE DESBORDE EL MAR...")
                while True:
                    xx = input("¿QUIERE CORRER EL RIESGO? SI/NO ")
                    if xx.lower() in ["si", "sí", "yes", "ja", "jaa", "n"]:
                        print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                        return x
                    elif xx.lower() in ["no", "n", "nein", "nope"]:
                        print("SU TABLERO SERÁ DE 25 FILAS Y 25 COLUMNAS")
                        x= 25
                        print("SU TABLERO DE ", x, "FILAS Y ", x, "COLUMNAS SE ESTÁ CREANDO.\n")
                        return x
                    else:
                        print("POR FAVOR, INGRESE 'SI' O 'NO'.")

           
def tablero(Tm):
    tu_ta = np.array([["  ","B", "L", "A", "S", "  ", "D", "E", " ", "L", "E", "Z", "O"]])
    su_ta = np.array([["V","E","R","N","O","N"]])
    nosotros = np.full((Tm, Tm), "🟦")
    ordenador = np.full((Tm, Tm), "🟦")
    separador = np.full((Tm+1, 2), "🟫")  
    numeros_de_columnas = []  # Para las fila con los números que indican las columnas necesitamos crear una lista vacia
    for i in range(1, Tm + 1):  #vamos recorriendo el rango (empezando en 1, no en 0, y terminando en Tm(o sea, uno más))
        if i < 10:  
            numeros_de_columnas.append(" "+str(i))  #A los número de un digito le añado un espacio para que queden bien y no se amontonen.
        else:
            numeros_de_columnas.append(str(i))   
    nosotros_columna= np.vstack((nosotros, numeros_de_columnas))
    ordenador_columna= np.vstack((ordenador, numeros_de_columnas))
    pantallas= np.hstack((nosotros_columna, separador,ordenador_columna))
    espacio_vacio= np.array([[" "]]) #para que pueda unir matrices con distinta dimension necesito añadir espacios vacios
    columnasletras = np.array([chr((i % 26) + 65) if i < 26 else chr((i % 26) + 97) for i in range(Tm)]).reshape(-1, 1)#esta linea es bastante complicada, lo hice con gpt.
    columna_de_letras =np.vstack((columnasletras, espacio_vacio))
    columna_de_filas_vacias = np.array([[" "]]*(Tm+1)) #para que la columna de letras que indican los nombres de las filas no se amontonen (en la pantalla derecha) usamos una columna vacia.
    pantallas_con_filas = np.hstack((columna_de_letras, pantallas,columna_de_filas_vacias, columna_de_letras))
 
    #con esto creamos el cabecero, donde irán los nombres, para su longitud se depende del tamalo del tablero
    nombres_jugadores= np.hstack((tu_ta,su_ta))
    tamaño_nombres=nombres_jugadores.shape[1]
    tamaño_tablero= pantallas_con_filas.shape[1]
    espacios_necesarios= tamaño_tablero - tamaño_nombres
    espacio_repetido = np.tile(espacio_vacio, (1, espacios_necesarios))
    cabecero= np.hstack((tu_ta,espacio_repetido, su_ta))
    pantallas_con_filas_y_cabero= np.vstack((cabecero,pantallas_con_filas)) #con esto unimos todo.
    return pantallas_con_filas_y_cabero

#con esto llamamos las funciones
tamaño_tablero = selector_tamaño()
tablero_resultante = tablero(tamaño_tablero)
#con esto la impimimos bonitas:
for fila in tablero_resultante:
    print("".join(fila))