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
    b) Inicio de sesion de un user en una determinada fecha
    c) Tiempo total de la sesion de un usuario
    d) Busqueda de una MAC
    e) Lista de MAC de un usuario
    f) Usuarios conectados a una AP en un rango de fecha
    x) Salir
    ''')
    input_1 = input("Seleccione el dato a analizar: ")
    print("\n")
    if input_1 == 'a':
        Id_ses()
    elif input_1 == 'b':
        Inic_ses()
    elif input_1 == 'c':
        tiempo_total()
    elif input_1 == 'd':
        mac_busqueda()
    elif input_1 == 'e':
        mac()
    elif input_1 == 'f':
        Mac_conect_fecha()
    elif input_1 == 'x':
        print("Saliendo del sistema...")
        exit()
    else:
        print("error")

#reemplazo los valores vacios por 0
#df.dropna(0)

#1
def Id_ses():
    
    #nombre del usuario
    nomb_usuario = input("Ingrese el nombre de usuario a analizar: ")
    
    #corroboro que exista el nombre
    if nomb_usuario in df.values:
        #separo las categorias en ID y Usuario
        #loc "elimina" categorias
        sf2 = df.loc[: , ["ID Conexion unico","Usuario"]]
        #isin busca dentro de la categoria
        #filtro las categorias por el nombre de usuario
        sf3 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #exporto como csv
        sf3.to_csv("sesiones.csv")
        
        print("Exito, archivo 'sessiones.csv' fue creado con exito")
        time.sleep(1)
        
        print("regresando al menu")
        
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        main()
    
    else:
        print("Nombre incorrecto, regresando al menu...")
        time.sleep(1)
        main()

#2
def Inic_ses():
    nomb_usuario = input("Ingrese el nombre del usuario a analizar: ")
    print("A continuacion, ingrese el rango de fecha")
    print("El formato debe ser MM/DD/AAAA HH:MM (mes/dia/año hora:minuto)")
    time.sleep(2)
    #solicito la primer fecha
    fech1 = input("ingrese la fecha inicial: ")
    #solicito la segunda fecha
    fech2 = input("ingrese la fecha final: ")
    #verifico la existencia de los datos
    if fech1 in df.values and fech2 in df.values and nomb_usuario in df.values and fech1 < fech2:
        #"elimino" las categorias innecesarias
        sf2 = df.loc[: , ["Usuario","Inicio de Conexi¢n"]]
        #busco el nombre del usuario
        sf3 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #busco entre las fechas especificas
        sf4 = sf3.loc[df["Inicio de Conexi¢n"].between(fech1, fech2)]
        #exporto csv
        sf4.to_csv("inicios_sesion.csv")
        
        print("proceso realizado con exito, verificar archivo 'inicios_sesion.csv")
        print("Regresando al menu...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        main()
    else:
        print("error dato incorrecto")
        print("Volviendo al menu")
        time.sleep(1)
        main()

#3
def tiempo_total():

    nomb_usuario = input("Ingrese el nombre de usuario a analizar: ")
    if nomb_usuario in df.values:
        sf2 = df.loc[: , ["Usuario","Session Time"]]
        sf1 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #al pedir el total usamos .sum
        sf3 = sf1['Session Time'].sum()
        
        print("El total de segundos es",sf3)
        #lo defino por hora minuto y segundo
        horas = sf3 // 3600
        sobrante = sf3%3600
        minutos = sobrante//60
        sobrante2 = sobrante%60
        time.sleep(1)
        print("HORAS:")
        print(horas)
        print("MINUTOS:")
        print(minutos)
        print("SEGUNDOS:")
        print(sobrante2)
        
        time.sleep(5)
        
        print("Regresando al menu...")
        
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        main()
    else:
        print("error, usuario no encontrado")
        print("regresando al menu...")
        time.sleep(1)
        main()

#4
def mac_busqueda():
    #Busco la mac del user
    mac_usuario = input("Ingrese la direccion MAC a analizar: ")
    #Verifico existencia
    if mac_usuario in df.values:
        #"elimino" categorias innecesarias
        sf1 = df.loc[: , ["MAC Cliente","Usuario"]]
        #Busco la Mac
        sf2 = sf1[sf1["MAC Cliente"].isin([mac_usuario])]
        #Agrupo por tamaño y cambio la cat, incluyo el nombre del usuario
        sf3 = sf2.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Veces Utilizada')
        #Exporto como csv
        sf3.to_csv("mac_busqueda.csv")
        print("Exito, el archivo 'mac_busqueda' fue creado con exito")
        time.sleep(1)
        
        print("regresando al menu")
        
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        main()

    else:
        print("Mac no identificada, regresando al menu...")
        time.sleep(1)



#5
def mac():
    nomb_usuario = input("Ingrese el nombre de usuario a analizar: ")
    
    #corroboro que exista el nombre
    if nomb_usuario in df.values:
        #separo las categorias en ID y Usuario
        #loc "elimina" categorias
        sf2 = df.loc[: , ["MAC Cliente","Usuario"]]
        #isin busca dentro de la categoria
        #filtro las categorias por el nombre de usuario
        sf3 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #agrupo por tamaño, y creo una index
        sf4 = sf3.groupby(['MAC Cliente']).size().reset_index(name ='Veces Utilizada')
        #exporto como csv
        sf4.to_csv("mac_usuario.csv")
        print("Exito, archivo 'mac_usuario.csv' fue creado con exito")
        time.sleep(1)
        
        print("regresando al menu")
        
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        main()
    
    else:
        print("Nombre incorrecto, regresando al menu...")
        time.sleep(1)
        main()


#6
def Mac_conect_fecha():
    print("A continuacion, ingrese el rango de fecha")
    print("El formato debe ser MM/DD/AAAA HH:MM (mes/dia/año hora:minuto)")
    time.sleep(2)
    #solicito la primer fecha
    fech1 = input("ingrese la fecha inicial: ")
    #solicito la segunda fecha
    fech2 = input("ingrese la fecha final: ")
    #verifico la existencia de los datos y la concordancia en el rango
    if fech1 in df.values and fech2 in df.values and fech1 < fech2:
        #"elimino" las categorias innecesarias
        sf2 = df.loc[: , ["Usuario","MAC AP","Inicio de Conexi¢n"]]
        #busco el nombre del usuario
        #busco entre las fechas especificas
        sf3 = sf2.loc[df["Inicio de Conexi¢n"].between(fech1, fech2)]
        #exporto csv
        sf3.to_csv("users_conec_ap.csv")
        
        print("proceso realizado con exito, verificar archivo 'users_conec_ap.csv'")
        print("Regresando al menu...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        main()
    else:
        print("Error dato, incorrecto")
        print("Volviendo al menu")
        time.sleep(1)
        main()



#8/28/2019 10:06
#8/28/2019 10:07
#csegeview

if __name__ == '__main__':
    main()