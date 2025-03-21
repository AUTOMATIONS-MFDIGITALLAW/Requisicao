import time

import pyautogui
import pyperclip

from function.click_and_fill import click_and_fill
from function.imgfuction import searchimage
from function.read_dataframe import copiar, copiar2


def cadastrar(row):
    time.sleep(5)
    copiar(row["PASTA"])
    searchimage('Pasta', 'Pasta Encontrado!', 'Pasta não encontrado!')
    pyautogui.write('1')
    pyautogui.press("backspace", presses=13)
    time.sleep(2)
    click_and_fill('clique2', 'clique2 encontrado', 'clique2 nao encontrado')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(3)
    searchimage('Adverso', 'Adverso Encontrado!', 'Adverso não encontrado!')
    time.sleep(1)
    click_and_fill('clique2', 'clique2 encontrado', 'clique2 nao encontrado')
    searchimage('Adverso', 'Adverso Encontrado!', 'Adverso não encontrado!')
    time.sleep(1)
    copiar(row["PARTES"])
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    click_and_fill('clique', 'clique encontrado', 'clique não encontrada')
    time.sleep(1)
    searchimage('TipoHonorario', 'TipoHonorario Encontrado!', 'TipoHonorario não encontrado!')
    copiar(row["ATO"])
    time.sleep(4)
    time.sleep(4)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(10)
    searchimage('Parcela', 'Parcela Encontrado!', 'Parcela não encontrado!')
    time.sleep(1)
    pyautogui.write('1')
    time.sleep(1)
    searchimage('ValorEspecie', 'ValorEspecie specie Encontrado!', 'ValorEspecie specie não encontrado!')
    copiar(row["VALOR"])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    searchimage('DataVencimento', 'DataVencimento specie Encontrado!', 'DataVencimento specie não encontrado!')
    copiar2(row["DATA"])
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    searchimage('Nota', 'Nota specie Encontrado!', 'Nota specie não encontrado!')
    copiar(row["OBS"])
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    searchimage('Salvar', 'Salvar specie Encontrado!', 'Salvar specie não encontrado!')



