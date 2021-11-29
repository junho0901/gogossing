# -*- coding: utf-8 -*-
# 라즈베리파이 GPIO 패키지 

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWORD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 23  #37 pin
ENB = 13  #27 pin

#GPIO PIN
IN1 = 25  #37 pin
IN2 = 24  #35 pin
IN3 = 19 #31 pin
IN4 = 26  #29 pin

# GPIO 모드 설정 
GPIO.setmode(GPIO.BCM)

# 핀 설정 함수
def setPinConfig(EN, INA, INB):  
    GPIO.setwarnings(False)      
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz 로 PWM 동작 시킴
    pwm = GPIO.PWM(EN, 100)
     
    # 우선 PWM 멈춤.   
    pwm.start(0) 
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)
    
    #앞으로
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
        
    #뒤로
    elif stat == BACKWORD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

        
# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def set_rpm1(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
        
def set_rpm2(ch, speed, stat):
    if ch == CH2:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)

def lose_rpm1(ch, speed, stat):  # 5초 이내에 감속하여 정지
    if ch == CH1:
        for i in range(50):
            speed = speed - 2
            setMotorContorl(pwmB, IN3, IN4, speed, stat)
            sleep(0.1)
            
            if speed == 0:
                GPIO.output(INA, LOW)
                GPIO.output(INB, LOW)

def lose_rpm2(ch, speed, stat):   # 5초 이내에 감속하여 정지
    if ch == CH2:
        for i in range(50):
            speed = speed - 2
            setMotorContorl(pwmB, IN3, IN4, speed, stat)
            sleep(0.1)
            
            if speed == 0:
                GPIO.output(INA, LOW)
                GPIO.output(INB, LOW)
             
#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴
def motor_pinset():   
    pwmA = setPinConfig(ENA, IN1, IN2)
    pwmB = setPinConfig(ENB, IN3, IN4)


# 종료
GPIO.cleanup()
