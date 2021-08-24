"""
Criando um Relatório automático de Vagas do Indeed com o Selenium + Python

Parte I

@2021 Created By Geovana Sousa - LearnData
"""

# $ python3 -m pip install Selenium

# Módulos Gerais e do Selenium
import os  # Módulo que permite a interação com o Sistema Operacional
from datetime import date  # Importando o Módulo para trabalhar com Datas
from time import sleep  # Permite adicionar tempos de espera dentro do código
from selenium import webdriver  # Disponibiliza as implementações Web do Selenium
from selenium.webdriver.common.keys import Keys  # Importa o Módulo para envio de Inputs
import csv  # Módulo para manipular arquivos CSV


# ---------------------------------------------------------------------------------------
os.chdir("C:\\Users\\geova\\OneDrive\\Área de Trabalho\\Python\\Indeed")  # Muda o diretório Atual

# ---------------------------------------------------------------------------------------
# Abre o Arquivo CSV Criado para
writer = csv.writer(open('vagas_ids.csv', 'w', encoding='utf-8', newline=''))
header = ['ID', 'TITULO', 'LINK']
writer.writerow(header)

# ---------------------------------------------------------------------------------------
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:\\Users\\geova\\anaconda3\\chromedriver.exe", options=options)


def extrair_vagas(palavra_chave):
    # Pesquisar cargos
    driver.get('https://br.indeed.com/')  # método utilizado para fazer uma requisição de url
    cargo_input = driver.find_element_by_name('q')  # Encontra o campo "O quê", Name = 'q'
    cargo_input.clear()  # Limpa o campo
    cargo_input.send_keys(palavra_chave)  # Envia a palavra-chave para o campo
    cargo_input.send_keys(Keys.RETURN)  # Simulação da tecla Enter

    # Ir para Busca Avançada
    driver.find_element_by_xpath('//a[text()="Busca Avançada de Vagas"]').click()

    # Selecionar Tipos de Vaga - Efetivo/CLT
    driver.find_element_by_xpath('//select[@id="jt"]//option[@value="fulltime"]').click()

    # Ir para o final da página
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Selecionar a opção "Omitir agências de emprego"
    driver.find_element_by_xpath('//input[@id="norecruiters"]').click()

    # Definir o Local
    local = driver.find_element_by_xpath('//input[@id="where"]')
    local.clear()
    local.send_keys('São Paulo, SP')

    # Selecionar a opção - Data: Últimos 3 Dias
    driver.find_element_by_xpath('//select[@id="fromage"]//option[@value="3"]').click()

    # Mostrar 50 vagas e classificar por data
    driver.find_element_by_xpath('//select[@id="limit"]//option[@value="50"]').click()
    driver.find_element_by_xpath('//select[@id="sort"]//option[@value="date"]').click()

    # Aceitar Cookies
    sleep(2)
    try:
        driver.find_element_by_xpath('//button[@id="onetrust-accept-btn-handler"]').click()
    except:
        pass

    # Selecionar o Botão de Pesquisa
    driver.find_element_by_xpath('//button[@id="fj"]').click()
    sleep(3)

    # Fechar Popup Window
    try:
        driver.find_element_by_xpath('//div[@id="popover-x"]').click()
    except:
        pass

    # Criar lista de vagas da página
    lista_vagas = (driver.find_elements_by_xpath('//div[@id="mosaic-provider-jobcards"]/a'))
    lista_ids = [vaga.get_attribute('id') for vaga in lista_vagas]
    lista_ids = list(set(lista_ids))
    lista_vagas = [vaga.get_attribute('href') for vaga in lista_vagas]

    # Salvar vagas no CSV
    for vaga in lista_vagas:
        driver.get(vaga)  # Ir para a página da vaga
        button = driver.find_elements_by_xpath('//button[@id="indeedApplyButton"]')  # Verificar se a candidatura é pelo Indeed
        titulo = driver.find_element_by_css_selector('h1').text  # Guardar o Título da vaga
        id_vaga = lista_ids[lista_vagas.index(vaga)]  # Encontrar o ID dentro da Lista
        if id_vaga is None:  # Checar se o id está na lista
            pass
        else:
            if len(button) > 0:
                if check_titulo(vaga):  # Verifica se o título se encaixa na especificação da vaga
                    if check_superior(vaga):  # Verifica se é exigido ensino superior
                        pass
                    else:
                        titulo = titulo
                        link = vaga
                        id_v = id_vaga

                        writer = csv.writer(open('vagas_ids.csv', 'a', encoding='utf-8', newline=''))
                        writer.writerow([id_v, titulo, link])
                else:
                    pass
            else:
                pass


# Definindo as Opções de Títulos
title_options = ["Financeiro", "financeiro", "Administrativo", "administrativo"]
exclusor = ["Superior", "superior", "cursando", "Cursando", "formado",
            "Formado", "Estágio", "Estagiário", "Bilíngue", "estágio",
            "estagiário", "PCD"]


def check_titulo(vaga):
    if any(titulo in vaga for titulo in title_options):
        result = True
    else:
        result = False
    return result


def check_superior(vaga):
    if any(titulo in vaga for titulo in exclusor):
        result = True
    else:
        result = False
    return result
