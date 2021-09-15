# Relatorio de Vagas do Indeed com Python + Selenium

Projeto criado para o estudo das ferramentas de *Web Scraping* e geração de relatórios

Acesse o post da Parte I no Blog [aqui](https://learningdata.dev/tutorial-relatórios-de-vagas-parte-1).

Acesse o post da Parte II no Blog [aqui](https://learningdata.dev/tutorial-relatórios-de-vagas-parte-2).

<p align="center"><img src="https://github.com/GeovanaSLima/RelatorioVagas-web-scraping/blob/main/Relatorio_1.png" width=50%></p>

## Apresentando o *Case*

Imagine que você tenha um amigo que está desempregado e procurando vagas em diversas plataformas, mas nunca parece achar as vagas que vão de cordo com seu perfil. Então, você decide que vai ajudá-lo criando um script em python para encontrar algumas vagas.
Para dar início você pergunta qual o tipo de vaga que está procurando, e ele lhe responde com as seguintes especificações:

* Vagas de Assistente Administrativo ou Financeiro, que não exija ensino superior.

Para fazer isso, você acredita que poderia usar o Indeed para encontrar as vagas, e ainda achar algumas que ele consiga se candidatar diretamente pela plataforma, sem precisar de um redirecionamento. 


## 🗂️ Divisão do Projeto

### [Parte I](https://github.com/GeovanaSLima/RelatorioVagas-web-scraping/blob/main/Parte%201.py)

* Interação com o WebDriver utilizando o Selenium
* Exportação da Lista de Vagas de acordo com as especificação
* Criação do Arquivo CSV


### [Parte II](https://github.com/GeovanaSLima/RelatorioVagas-web-scraping/blob/main/Parte%202.py)

* Criação do Relatório com *ReportLab*
* Criar e enviar a mensagem por e-mail com o Relatório em anexo

<br>

### [Código Completo](https://github.com/GeovanaSLima/RelatorioVagas-web-scraping/blob/main/Completo.py)
<br>

## Selenium

O pacote *selenium* é utilizado para automatizar interações de web browsers com Python.
 
> **Home:**  https://selenium.dev
> 
> **Docs:**  [selenium package API](https://seleniumhq.github.io/selenium/docs/api/py/api.html)
>   
> **Dev:**  https://github.com/SeleniumHQ/Selenium
>   
> **PyPI:**  https://pypi.org/project/selenium/
> 
>**IRC**  **#selenium** channel on freenode

### Versões do Python Suportadas
* Python 3.7+

### Instalação

Se você já tem o **pip** instalado no seu sistema, pode simplesmente rodar a linha abaixo:

```pip install -U selenium```

Como segunda opção, você pode fazer o download pela fonte de distribuição [PyPI](https://pypi.org/project/selenium/#files), extrair o arquivo e rodar:

```python setup.py install```

### Drivers

O Selenium exige um *driver* para interagir com o browser escolhido. Os *drivers* disponíveis estão relacionados abaixo, lembrando que eles devem estar no ddiretório de instalação original do python.

**Chrome:** | **Edge:** | **Firefox:** | **Safari:**
----------- | ----------- | ----------- | ----------- |
[Driver](https://chromedriver.chromium.org/downloads) | [Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) | [Driver](https://github.com/mozilla/geckodriver/releases) | [Driver](	https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

---

## ReportLab

ReportLab é uma biblioteca do python para criar documentos em Portable Document Format (PDF), podendo criar gráficos em vários bitmaps e formatos de vetores. A biblioteca permite qye você crie documentos com comandos gráficos, sem a necessidade de passos intervencionais. Sendo assim, suas aplicaçõs conseguem gerar relatórios de forma rápida com pouquíssimas restrições para sua utilização. As principais aplicações do RepostLab são:

* Geração de PDFs dinâmicos a partir da Web
* Relatórios corporativos a partir de grandes banco de dados
* Criar um sistema de construção para relatórios gerenciais, contábeis e estatísticos complexos com gráficos, imagens, tabelas e texto 
* Transformar XML em PDF
* Transformar CSV/XLSX em PDF

> [Documentações](https://www.reportlab.com/dev/docs/)
>
> [User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)

### Versões do Python Suportadas
* Python  2.7 e 3.6+

### Instalação

```python3 -m pip install reportlab```

---
