# Ejercicio 2 - TP3 - Automata: (a|b)*(a|b|e)
import time

def main():
    print("Ingrese cualquier tipo de cadena del formato: (aa|b)*(a|bb)*")
    # ingreso una cadena compatible con el automata
    string = str(input("Ingrese cadena: "))
    # llamo a la funcion para que haga la transicion de estados
    transition_process(string)
def transition_process(string):
    # inicializo el estado
    state = 0
    print(f"Ha introducido: '{string}'")
    print("INICIANDO AUTOMATA...")
    print("ESTADO INICIAL: ", state)
    # analizo con un for las transiciones de estado, recorriendo la cadena de entrada
    for i in range(len(string)):
        # igualo la posicion de la cadena en la que estoy a la transicion actual
        transition = string[i]
        # analizo con un if cada estado importante
        # itero con el estado 0
        if state == 0:
            plus = 1
            next = find_next_value(string, i, plus)
            # analizo la transicion a
            if transition == 'a':
                # si el siguiente tambien es un a, entonces cambia a estado 1
                if next == 'a':
                    state = 2
                    print("ESTADO: ", state)
                    time.sleep(1)
                    state = 1
                    print("ESTADO: ", state)
                    time.sleep(1)
                    state = 3
                    print("ESTADO: ", state)
                # si el siguiente no es un a, hace la transicion de 1 a 3 a 4
                else:
                    state = 2
                    print("ESTADO: ", state)
                    state = 3
                    print("ESTADO: ", state)
                    state = 4
                    print("ESTADO: ", state)
            # analizo la transicion b
            elif transition == 'b':
                # si el siguiente tambien es un b, entonces hace la transicion de 1 a 3 a 4
                if next == 'b':
                    state = 1
                    print("ESTADO: ", state)
                    state = 3
                    print("ESTADO: ", state)
                    time.sleep(1)
                    state = 4
                    print("ESTADO: ", state)
                    continue
                # si el siguiente tambien es un a, entonces cambia a estado 1
                elif next == 'a':
                    state = 1
                    print("ESTADO: ", state)
                # si no es ninguno de los dos, error
                else:
                    state = "error"
                    print("ESTADO: ", state)
                    continue

# defino una funcion que analiza los elementos siguientes de la cadena
def find_next_value(string, i, plus):
    try:
        return string[i + plus]
    except:
        return 0
# defino el constructor, para ejecutar el main()
if __name__ == '__main__':
    main()