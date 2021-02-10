#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
import smtplib
from bs4 import BeautifulSoup
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}
url = "https://www.amazon.fr/Xiaomi-Redmi-Smartphone-Display-5020mAh/dp/B089WCC775/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=xiaomi&qid=1612958660&sr=8-2"




def send_emails():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls
    server.ehlo()
    server.login('Email Address','Password')
    subject = 'price fell down!'
    body = 'Check the amazon link   https://www.amazon.fr/Xiaomi-Redmi-Smartphone-Display-5020mAh/dp/B089WCC775/ref=sr_1_2?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=xiaomi&qid=1612958660&sr=8-2'
    msg = f"Subject: {subject}\n\n {body}"
    server.sendmail('Email adress','Email adress',msg)
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()

reponse = requests.get(url,headers=headers)
soup = BeautifulSoup(reponse.content, 'html.parser')
titre = soup.find(id="productTitle").get_text()  
price = soup.find(id="priceblock_ourprice").get_text()
Convertedprice = float(price[0:4].replace(',', ''))
print(Convertedprice)
if Convertedprice < 140:
    send_emails()
else:
    print("Pas encore")
