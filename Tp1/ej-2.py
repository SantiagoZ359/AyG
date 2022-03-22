import re
import string
from wsgiref.validate import PartialIteratorWrapper

def contiene_s(cadena):
    patron = '[0-9]'

    if re.search(patron, cadena):
        print(f'La cadena "{cadena}" contiene un numero "{patron}"')
    else:
        print(f'La cadena "{cadena}" NO contiene un numero "{patron}"')


cadena_1 = 'Fernand0'
cadena_2 = 'um'
cadena_3 = 'facultad'

contiene_s(cadena_1)
contiene_s(cadena_2)
contiene_s(cadena_3)