import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText

def send_mail():    # sendmail() --> send_mail()
    smtp = smtplib.SMTP('smtp.gmail.com',587)
    smtp.starttls()
    smtp.login('seongsabgim@gmail.com', 'ggmzyrdpzjlkqpow')
    msg=MIMEText('무성이가 위험합니다')
    msg['Subject'] = '무성이를 도와주세요!'
    msg['To'] = 'lss980301@naver.com'
    smtp.sendmail('seongsabgim@gmail.com', 'lss980301@naver.com', msg.as_string())
    smtp.quit()
