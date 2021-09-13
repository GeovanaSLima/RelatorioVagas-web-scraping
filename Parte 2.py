"""
Criando um Relatório automático de Vagas do Indeed com o Selenium + Python

Parte II

@2021 Created By Geovana Sousa - LearnData
"""

# $ python3 -m pip install reportlab

# Módulos do ReportLab
from reportlab.pdfgen.canvas import Canvas  #
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Módulos para envio de E-mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# PDF -----------------------------------------------------------------------------------
# Estrutura das Páginas
PAGE_HEIGHT = letter[1]  # Altura da Página
PAGE_WIDTH = letter[0]  # Largura da Página
styles = getSampleStyleSheet()  # Estilo da Página

image = "LearningData_dark.png"
my_canvas = Canvas("Vagas.pdf", pagesize=letter)
pageinfo = "LearningData"
title = "Vagas Indeed"


def first_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 20)
    canvas.drawCentredString(300, 720, title)
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(x=500, y=15, text="Página 1 / %s" % pageinfo)
    canvas.drawImage(image, x=20, y=750, width=110, height=22, mask='rgba(252, 92, 101, 0.5)')
    canvas.drawString(547, 28, date.today().strftime("%d/%m/%Y"))
    canvas.restoreState()


def later_pagers(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(x=500, y=15, text="Página %d / %s" % (doc.page, pageinfo))
    canvas.drawImage(image, x=20, y=750, width=110, height=22, mask='rgba(252, 92, 101, 0.5)')
    canvas.drawString(547, 28, date.today().strftime("%d/%m/%Y"))
    canvas.restoreState()


def pdf_file_generator():
    doc = SimpleDocTemplate("Vagas.pdf", pagesize=letter)
    story = [Spacer(1, 2)]
    style = styles["Normal"]
    style_h = styles["Heading3"]
    with open('vagas_ids.csv', 'r') as file:
        leitura_ids = csv.reader(file)
        titles = next(file)
        if titles is not None:
            for row in leitura_ids:
                vaga_title = (row[1])
                vaga_link = (row[2])
                p = Paragraph(vaga_title, style_h)
                p2 = Paragraph(vaga_link, style)
                story.append(p)
                story.append(Spacer(1, 2))
                story.append(p2)
                story.append(Spacer(1, 5))
            doc.build(story, onFirstPage=first_page, onLaterPages=later_pagers)


# Enviar por Email ---------------------------------------------------------------------

def enviar_email():
    corpo_email = """
Boa tarde! 

Segue em anexo o relatório de vagas dos últimos 3 dias.
    """

    mensagem = MIMEMultipart()
    # mensagem = email.message.Message()
    mensagem['Subject'] = 'Relatório de Vagas Indeed - Últimos 3 dias'
    mensagem['From'] = 'seu_email@xx.com'
    mensagem['To'] = 'email_que_vai_enviar@xx.com'
    password = 'sua_senha'
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.attach(MIMEText(corpo_email, 'plain'))

    filename = 'Vagas.pdf'
    anexo = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(anexo.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "anexo; filename=%s" % filename)

    mensagem.attach(part)
    anexo.close()

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais de Login para realizar o envio
    s.login(mensagem['From'], password)
    s.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string().encode('utf-8'))


# Rodando    ---------------------------------------------------------------------

# Definindo as Palavras-chaves para pesquisa
titulos = ['assistente administrativo', 'assistente financeiro']

# Extrair Vagas
for pesquisa in titulos:
    extrair_vagas(pesquisa)

# Encerrar o webdriver
driver.close()

# Gerar o PDF
pdf_file_generator()

# Enviar o E-mail
enviar_email()
