from logging import exception
import pandas as pd
import pyperclip
from tkinter import filedialog
from function.logger import log


def ler_arquivo():
    return filedialog.askopenfilename(title="Selecione o arquivo BASE DE DEVEDORES",filetypes=[("Arquivos Excel", "*.xlsx *.xls")])


def copiar(valor: str, date: bool = False, time: bool = False):
    try:
        if date and not time:
            valor = pd.to_datetime(valor, format='%d/%m/%Y', errors='coerce')
            valor = valor.strftime('%d/%m/%Y')

        if time and not date:
            valor = pd.to_datetime(valor, format='%H:%M:%S', errors='coerce')
            valor = valor.strftime('%H:%M:%S')

        if pd.notnull(valor):
            valor_final = str(valor)
            pyperclip.copy(valor_final)
            log.success('Valor Copiado!')
            return valor_final

    except Exception as e:
        log.error(f"Erro ao copiar valor: {e}")
        return None

    except exception as e:
        log.success('Valor não copiado!')