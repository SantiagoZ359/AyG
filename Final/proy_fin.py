import pandas as pd
import numpy as np
import time 

#leo el csv
datos = pd.read_csv("Usuarios WiFi.csv")
df = pd.DataFrame(datos)

#creo el menu
def main():
    print('''
    OPCIONES:
    a) Lista de sesiones de usuario por ID
    b) Direccion URL
    c) Direccion IPV4
    d) Contraseña segura
    e) Salir
    ''')
    input_1 = input("Seleccione el dato a analizar: ")
    print("\n")
    if input_1 == 'a':
        Id_ses()
    #elif input_1 == 'b':
        #use_url()
    #elif input_1 == 'c':
        #use_ipv4()
    #elif input_1 == 'd':
        #use_password()
    elif input_1 == 'e':
        print("Saliendo del sistema...")
        exit()
    else:
        print("error")

#reemplazo los valores vacios por 0
#df.dropna(0)

#Filtro por la categoria usuario
def Id_ses():
    #nombre del usuario
    nomb_usuario = input("Ingrese el nombre de usuario a analizar: ")
    #corroboro que exista el nombre
    if nomb_usuario in df.values:
        #separo las categorias en ID y Usuario
        sf2 = df.loc[: , ["ID Conexion unico","Usuario"]]
        #filtro las categorias por el nombre de usuario
        sf3 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #exporto como csv
        sf3.to_csv("sesiones.csv")
        print("Exito, archivo 'sessiones.csv' fue creado con exito")
        time.sleep(1)
        print("regresando al menu")
        time.sleep(1)
        main()
    else:
        print("Nombre incorrecto, regresando al menu...")
        time.sleep(1)
        main()

if __name__ == '__main__':
    main()