### suv modeli
linkler=["https://www.arabam.com/ikinci-el/arazi-suv-pick-up/renault"]
###SON
from bs4 import BeautifulSoup
import requests
import time
import numpy as np
import pandas as pd

liste1 = []
l=0
while l < len(linkler):
    # her bir linke ulasma
    ll = linkler[l]
    k=1
    while k<=50:
        # tüm arabaların linklerinin alınması ve liste 1 e at
        link = f"{ll}?sort=year.desc&page={k}"    
        r = requests.get(link, headers = {'User-agent': 'your bot 0.1'})
        soup = BeautifulSoup(r.content,"lxml")
        list = soup.find_all("tr",attrs={"class":"listing-list-item pr should-hover bg-white"})
        for i in list:
            link = i.find("td",attrs={"class":"listing-modelname pr"}).a.get("href")
            link = f"https://www.arabam.com{link}"
            liste1.append(link)
        k+=1
    l+=1
data=pd.read_DataFrame()
data["linkler"] = liste1
data.to_csv("data.csv")
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
email_sender="oguztizlak@gmail.com"
email_password="fsveigynlbjzljub"
email_recevier="oguztizlak@gmail.com"
subject="deneme"
body="""
deneme mail gonderme
"""
em=EmailMessage()
em["from"]=email_sender
em["to"]=email_recevier
em["subject"]=subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
  smtp.login(email_sender,email_password)
  smtp.sendmail(email_sender,email_recevier,em.as_string())
  msg=MIMEMultipart()
  msg["from"]=email_sender
  msg["to"]=email_recevier
  msg["subject"]=subject
  msg.attach(MIMEText(body,"plain"))
  filename="data.csv"
  attachment = open(filename,"rb")
  attachment_package = MIMEBase("application","octet-stream")
  attachment_package.set_payload((attachment).read())
  encoders.encode_base64(attachment_package)
  attachment_package.add_header('Content-Disposition',"attachment ; filename= "+filename)
  msg.attach(attachment_package)
  text = msg.as_string()
  smtp.sendmail(email_sender,email_recevier,text)
