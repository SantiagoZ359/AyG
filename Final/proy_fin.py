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
    f) Usuarios conectados a una AP en un rango de fecha o fecha especifica
    g) Trafico de subida y bajada de un usuario
    h) Ordenamiento por trafico
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
    elif input_1 == 'g':
        conex_tot()
    elif input_1 == 'h':
        total_traf()
    elif input_1 == 'x':
        print("Saliendo del sistema...")
        exit()
    else:
        print("error")

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
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            Id_ses()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
    
    else:
        print("Nombre incorrecto, intentelo nuevamente...")
        time.sleep(1)
        Id_ses()

#2
def Inic_ses():
    nomb_usuario = input("Ingrese el nombre del usuario a analizar: ")
    print("A continuacion, ingrese el rango de fecha")
    print("El formato debe ser MM/DD/AAAA HH:MM (mes/dia/a??o hora:minuto)")
    time.sleep(2)
    #solicito la primer fecha
    fech1 = input("ingrese la fecha inicial: ")
    #solicito la segunda fecha
    fech2 = input("ingrese la fecha final: ")
    #verifico la existencia de los datos
    if nomb_usuario in df.values and fech1 < fech2:
        #"elimino" las categorias innecesarias
        sf2 = df.loc[: , ["Usuario","Inicio de Conexi??n"]]
        #busco el nombre del usuario
        sf3 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #busco entre las fechas especificas
        sf4 = sf3.loc[df["Inicio de Conexi??n"].between(fech1, fech2)]
        #exporto csv
        sf4.to_csv("inicios_sesion.csv")
        
        print("proceso realizado con exito, verificar archivo 'inicios_sesion.csv")
        time.sleep(1)
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            Inic_ses()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
    else:
        print("error dato incorrecto")
        print("Intentelo nuevamente")
        time.sleep(1)
        Inic_ses()

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
        
        time.sleep(1)
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            tiempo_total()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
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
        #Agrupo por tama??o y cambio la cat, incluyo el nombre del usuario
        sf3 = sf2.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Veces Utilizada')
        #Exporto como csv
        sf3.to_csv("mac_busqueda.csv")
        print("Exito, el archivo 'mac_busqueda' fue creado con exito")
        time.sleep(1)
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            mac_busqueda()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit

    else:
        print("Mac no identificada, regresando al menu...")
        time.sleep(1)

#5
def mac():
    #pido el nombre del usuario
    nomb_usuario = input("Ingrese el nombre de usuario a analizar: ")
    
    #corroboro que exista el nombre
    if nomb_usuario in df.values:
        #separo las categorias en ID y Usuario
        #loc "elimina" categorias
        sf2 = df.loc[: , ["MAC Cliente","Usuario"]]
        #isin busca dentro de la categoria
        #filtro las categorias por el nombre de usuario
        sf3 = sf2[sf2["Usuario"].isin([nomb_usuario])]
        #agrupo por tama??o, y creo una index
        sf4 = sf3.groupby(['MAC Cliente']).size().reset_index(name ='Veces Utilizada')
        #exporto como csv
        sf4.to_csv("mac_usuario.csv")
        print("Exito, archivo 'mac_usuario.csv' fue creado con exito")
        time.sleep(1)
        #menu para continuar
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            mac()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
    
    else:
        print("Nombre incorrecto, regresando al menu...")
        time.sleep(1)
        main()


#6
def Mac_conect_fecha():

    #consulto si es en una fecha determinada o en un rango
    print("Desea que la busqueda sea en un rango de fecha o en una fecha especifica")
    selecc = input("Ingrese 1 si desea en rango, ingrese 2 si desea en fecha determinada: ")
    if selecc == '1':
        print("A continuacion, ingrese el rango de fecha")
        print("El formato debe ser MM/DD/AAAA (mes/dia/a??o), puede incluir hora HH:MM (hora:minuto")
        time.sleep(2)
        #solicito la primer fecha
        fech1 = input("ingrese la fecha inicial: ")
        #solicito la segunda fecha
        fech2 = input("ingrese la fecha final: ")
        #solicito la mac ap
        macap = input("Ingrese la mac ap a analizar: ")
        #verifico la existencia de los datos y la concordancia en el rango
        if fech1 < fech2 and macap in df.values:
            #"elimino" las categorias innecesarias
            sf2 = df.loc[: , ["Usuario","MAC AP","Inicio de Conexi??n"]]
            #busco entre las fechas especificas
            sf3 = sf2[sf2["MAC AP"].isin([macap])]
            sf4 = sf3.loc[df["Inicio de Conexi??n"].between(fech1, fech2)]
            #exporto csv
            sf4.to_csv("users_conec_ap.csv")
        
            print("proceso realizado con exito, verificar archivo 'users_conec_ap.csv'")
            time.sleep(1)
            #menu para continuar
            menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
            if menu == '1':
                print("Regresando al menu...")
                time.sleep(1)
                main()
            elif menu == '2':
                Mac_conect_fecha()
            elif menu == '3':
                print("Saliendo...")
                time.sleep(1)
                exit
        else:
            print("Error dato, incorrecto")
            print("Volviendo al inicio")
            time.sleep(1)
            Mac_conect_fecha()
    elif selecc == '2':
        print("Correcto")
        #solicito la fecha y la mac ap
        print("A continuacion, ingrese la fecha especifica")
        print("El formato debe ser MM/DD/AAAA (mes/dia/a??o)")
        time.sleep(2)
        #pido la fecha
        fechespec = input("Ingrese la fecha: ")
        #creo la fecha final que es el mismo dia hasta las 23:59
        fechespecfin = fechespec + ' 23:59'
        #pido la mac
        macap2 = input("Ingrese la mac ap a analizar: ")
        if macap2 in df.values:
            sf2 = df.loc[: , ["Usuario","MAC AP","Inicio de Conexi??n"]]
            #busco entre las fechas especificas
            sf3 = sf2[sf2["MAC AP"].isin([macap2])]
            sf4 = sf3.loc[df["Inicio de Conexi??n"].between(fechespec, fechespecfin)]
            #exporto csv
            sf4.to_csv("users_conec_ap_fech.csv")
        
            print("proceso realizado con exito, verificar archivo 'users_conec_ap_fech.csv'")
            time.sleep(1)
            #menu para continuar
            menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
            if menu == '1':
                print("Regresando al menu...")
                time.sleep(1)
                main()
            elif menu == '2':
                Mac_conect_fecha()
            elif menu == '3':
                print("Saliendo...")
                time.sleep(1)
                exit
        else:
            print("Error, dato incorrecto")
            print("Volviendo al inicio")
            time.sleep(1)
            Mac_conect_fecha()
    
    else:
        print("Error, dato incorrecto")
        print("Volviendo al inicio")
        time.sleep(1)
        Mac_conect_fecha()

#7
def conex_tot():
    #pido el usuario
    nomb_usuario = input("Ingrese el nombre de usuario a analizar: ")
    #verifico la existencia del usuario
    if nomb_usuario in df.values:
        #selecciono las columnas a utilizar
        sf1 = df.loc[: , ["Usuario","Input Octects","Output Octects"]]
        #busco el usuario
        sf2 = sf1[sf1["Usuario"].isin([nomb_usuario])]
        #sumo y divido para obtener los valores
        sf3 = sf2['Input Octects'].sum()
        MB1 = sf3 // 1048576
        sf4 = sf2['Output Octects'].sum()
        MB2 = sf4 // 1048576

        print(MB1, "MB de bajada")
        print(MB2, "MB de subida")
        time.sleep(5)

        #menu para continuar
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            conex_tot()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
    else:
        print("error, usuario no encontrado")
        print("intentelo nuevamente...")
        time.sleep(1)
        conex_tot()


#8
def total_traf():
    selec = input("Ingrese 1 para ordenar por bajada, ingrese 2 para ordenar por subida: ")
    if selec == '1':
        #definimos las columnas a utilizar
        sf1 = df.loc[: , ["MAC AP","Input Octects"]]
        #agrupo las macs sumando sus valores de octetos de bajada
        sf2 = sf1.groupby('MAC AP').sum()
        #ordeno de forma descendente
        sf3 = sf2.sort_values(by = ['Input Octects'],ascending = False)
        #exporto como csv
        sf3.to_csv("sort_bajada.csv")
        time.sleep(1)
        print("Proceso realizado con exito, verifique el archivo 'sort_bajada.csv'.")
        time.sleep(1)
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            total_traf()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
    elif selec == '2':
        #definimos las columnas a utilizar
        sf1 = df.loc[: , ["MAC AP","Output Octects"]]
        #agrupo las macs sumando sus valores de octetos de bajada
        sf2 = sf1.groupby('MAC AP').sum()
        #ordeno de forma descendente
        sf3 = sf2.sort_values(by = ['Output Octects'],ascending = False)
        #exporto como csv
        sf3.to_csv("sort_subida.csv")
        print("Proceso realizado con exito, verifique el archivo 'sort_subida.csv'.")
        time.sleep(1)
        menu = input("Para volver al menu ingrese 1, para volver a intentarlo ingrese 2, para salir 3: ")
        if menu == '1':
            print("Regresando al menu...")
            time.sleep(1)
            main()
        elif menu == '2':
            total_traf()
        elif menu == '3':
            print("Saliendo...")
            time.sleep(1)
            exit
    else:
        print("Intentelo de nuevo")
        total_traf()

#8/28/2019 10:06
#8/28/2019 10:07
#csegeview
#04-18-D6-22-94-E7:UM

if __name__ == '__main__':
    main()