import time

import pyautogui

from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage
from function.read_dataframe import copiar


def adicionar_cadastro():
    time.sleep(3)
    searchimage('Adicionar', 'Adicionar Encontrado!', 'Adicionar não encontrado!')
    time.sleep(2)