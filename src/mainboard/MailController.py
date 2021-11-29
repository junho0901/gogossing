# devide "import time,smtplib" into two sentences shown line4, and line5
import json
import requests
import smtplib
from email.mime.text import MIMEText


def send_mail():  # sendmail() --> send_mail()
    url = 'http://ip-api.com/json'
    data = requests.get(url)
    res = data.json()
    text = "위도: " + str(res.get('lat')) + "\n" +  "경도: " + str(res.get('lon'))

    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login('seongsabgim@gmail.com', 'ggmzyrdpzjlkqpow')
    msg=MIMEText(text)
    msg['Subject'] = '[고고씽 with safety] 킥보드 사용자가 위험합니다.'
    msg['To'] = 'lss980301@naver.com'
    smtp.sendmail('seongsabgim@gmail.com', 'lss980301@naver.com', msg.as_string())
    smtp.quit()
