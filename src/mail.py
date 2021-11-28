import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MINEText
#GPIO.setmode(GPIO.BCM)
#CHECK_ON=1
#GPIO.setup(
smtp=smtplib.SMTP('smtp.gmail.com',587)
smtp.starttls()
smtp.login('seongsabgim@gmail.com', 'taeyeon31$2!')
msg=MINEText('mumu is jonjal')
msg['Subject']='mumu is sexy'
msg['To']='lss980301@naver.com'
smtp.sendmail('seongsabgim@gmail.com', 'lss980301@naver.com', msg.as_string())
smtp.quit()
