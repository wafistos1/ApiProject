from .base import *
from .pro import *
try:
    from .dev import *
    print('Je suis sur le dev')
    
except :
    print('Pas de fichier dev.py')