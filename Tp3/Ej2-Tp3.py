import time

def main():
    print("Ingrese cualquier tipo de cadena del formato: (aa|b)*(a|bb)*")
    string = str(input("Ingrese cadena: "))
    transition_process(string)

def transition_process(string):
    # inicializo el estado en 0
    state = 0
    print(f"Ha introducido: '{string}'")
    print("INICIANDO AUTOMATA...")
    # recorro la cadena de entrada con un for
    for i in range(len(string)):
        # igualo la cadena de la posicion actual a la transicion
        transition = string[i]
        #Para el Estado A
        if state == 0:       
       
            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue
            elif transition == 'b':
                print("ESTADO: ", state)
                state = 2
                time.sleep(1)
                continue
            else:
                print("ERROR")
                state=0
                return
                 
        #Para el Estado B
        if state == 1:   

            if transition == 'a':
                print("ESTADO: ", state)
                state = 3
                time.sleep(1)
                continue
            elif transition == 'b':
                print("ESTADO: ", state)
                state = 2                
                time.sleep(1)           
                continue
            else:
                print("ERROR")
                state=0
                return
        
        #Para el Estado C
        if state == 2:

            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue
            elif transition == 'b':
                print("ESTADO: ", state)
                state = 4
                time.sleep(1)              
                continue
            else:
                print("ERROR")
                state=0
                return

        #Para el Estado D
        if state == 3:

            if transition == 'a':
                print("ESTADO: ", state)
                state = 3
                time.sleep(1)
                continue
            elif transition == 'b':
                print("ESTADO: ", state)
                state = 2
                time.sleep(1)              
                continue
            else:
                print("ERROR")
                state=0
                return

        #Para el Estado E
        if state == 4:

            if transition == 'a':
                print("ESTADO: ", state)
                state = 1
                time.sleep(1)
                continue
            elif transition == 'b':
                print("ESTADO: ", state)
                state = 4
                time.sleep(1)              
                continue
            else:
                print("ERROR")
                state=0
                return
    if state == 0 or state == 1 or state == 2:
        print("Estado de aceptacion no alcanzado.",state)
    else:
        print("Estado de aceptacion alcanzado:", state)

if __name__ == '__main__':
    main()