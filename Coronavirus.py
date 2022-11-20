import re
import smtplib
import requests
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def enviar_email():
    corpo_email = """
    <p>ALERTA, OS CASOS DE COVID AUMENTARAM NA BAHIA!</p>
    <p>https://infovis.sei.ba.gov.br/covid19/</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "ALERTA DE AUMENTO DE CASOS DE COVID 19 NA BAHIA!"
    msg['From'] = 'jefinhosena2@gmail.com'
    msg['To'] = 'jefinhosena2@gmail.com'
    password = 'yztbheyuzkaggylc'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

options = Options()
options.headless = True
servico = Service(ChromeDriverManager().install())
naveg = webdriver.Chrome(service=servico, options=options)
naveg.get('https://infovis.sei.ba.gov.br/covid19/')
sleep(4)
site = naveg.find_element(By.XPATH, '//*[@id="shiny-tab-aba1"]/div[1]')
page_content = naveg.page_source
soup = BeautifulSoup(page_content, 'html.parser')
#print(soup.prettify())
casos = soup.find_all('div', attrs={'class': 'shiny-html-output col-sm-3 shiny-bound-output'})
num = soup.find('div', attrs={'id': 'casos_atv'})
num1 = num.find('h3')
num2 = float(num1.text)
for caso in casos:
    titulo = caso.find('p')
    numero = caso.find('h3')

    #if titulo:
        #num = numero[3]
        #num1 = float(num)
        #print(titulo.text)
        #print(numero.text)
        #print(num2)
        #print('')
if num2 > 4.999:
    enviar_email()













