import time

from Task.buscar_pasta import buscar_pasta
from function.click_and_fill import click_and_fill
from function.logger import log


def etapa_processo(df):
    time.sleep(5)
    buscar_pasta(df["Nº"][0])
    for index, row in df.iterrows():
        log.info('cadastro do procon iniciado!')
        click_and_fill('fechar', 'fechar encontrado!', 'fechar não encontrado')
        log.info('Cadastro completo: ' + row['Autor'])