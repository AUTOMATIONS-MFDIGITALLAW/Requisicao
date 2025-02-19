import os
import sys


def get_resource_path(relative_path):
   try:
      base_path = sys._MEIPASS
   except Exception:
      base_path = os.path.abspath(".")
   return os.path.join(base_path, relative_path)

IMG = {
    'cookie': get_resource_path('img/cookie.png'),
    'Abrir_Requisicao': get_resource_path('img/Abrir_Requisicao.png'),
    'Requisicao': get_resource_path('img/Requisicao.png'),
}

POSITION = {
    'cookie': (1767, 972)
}
