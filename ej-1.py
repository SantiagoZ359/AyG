import re
import string
from wsgiref.validate import PartialIteratorWrapper

def contiene_s(cadena):
    patron = '[A-Z]'

    if re.search(patron, cadena[0]):
        print(f'La cadena "{cadena}" contiene una mayuscula del patron "{patron}"')
    else:
        print(f'La cadena "{cadena}" NO contiene una mayuscula del patron "{patron}"')


cadena_1 = 'Fernando'
cadena_2 = 'um'
cadena_3 = 'facultad'

contiene_s(cadena_1)
contiene_s(cadena_2)
contiene_s(cadena_3)