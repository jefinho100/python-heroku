import re
import smtplib
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
options = Options()
options.headless = True
servico = Service(ChromeDriverManager().install())
naveg1 = webdriver.Chrome(service=servico, options=options)
naveg1.get('https://www.tempo.com/itanhem.htm')
sleep(5)
buton = naveg1.find_element(By.XPATH, '//*[@id="sendOpGdpr"]').click()
sleep(3)
div_mae = naveg1.find_element(By.XPATH, '/html/body/main/span[4]/span/span/ul')
html_content = div_mae.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
dias = soup.find_all('li', attrs={'class': 'dia'})
for dia in dias:
    data = dia.find('span', attrs={'class': 'cuando'})
    if not data:
        continue
    max = dia.find('span', attrs={'class': 'temperatura'})
    if not max:
        continue
    provabilidade = dia.find('span', attrs={'class': 'probabilidad-lluvia'})
    if not provabilidade:
        continue
    milimetros = provabilidade.find('span', attrs={'class': 'changeUnitR'})
    milimetros1 = milimetros.text[0:2]
    mili = float(milimetros1)
    if provabilidade:
        print(data.text)
        print(mili)
        print(provabilidade.text)
        print(max.text)
        print('')
    else:
        print(data.text)
        print(max.text)
        print('')
    def enviar_email():
        corpo_email = """
        <p>ALERTA DE CHUVA FORTE NESTA SEMANA!</p>
        <p>https://www.tempo.com/itanhem.htm</p>
        """

        msg = email.message.Message()
        msg['Subject'] = "Alerta de Chuva forte na Semana!"
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

    if mili > 10:
        enviar_email()





    
























