
  
import re
import string
from wsgiref.validate import PartialIteratorWrapper

def contiene_s(cadena):
    patron = '#'

    if re.search(patron, cadena[0]):
        print(f'La cadena "{cadena}" si es valido en python "{patron}"')
    else:
        print(f'La cadena "{cadena}" NO es valido en python "{patron}"')


cadena_1 = '#Fernand0'
cadena_2 = 'um'
cadena_3 = 'facultad'

contiene_s(cadena_1)
contiene_s(cadena_2)
contiene_s(cadena_3)