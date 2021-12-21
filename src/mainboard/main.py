# import AlarmController as ACt
import RPi.GPIO as GPIO
import AngleChecker as AgC
import MotorController as MC
import MailController as Mail
import DistanceChecker as DC
import MultiPeopleChecker as MP
import AlarmChecker as AC
import time
import web_parser as wp
import DisplayController as lcd
GPIO.setwarnings(False)

STOP  = 0
FORWARD = 1
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

def setMotor(speed, stat):
    #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
    setMotorContorl(pwmA, IN1, IN2, speed, stat)
    setMotorContorl(pwmB, IN3, IN4, speed, stat) # speed +30
    
    
def lose_rpm(speed, stat):   # 5초 이내에 감속하여 정지
    a = speed
    for i in range(5):
        speed -= a/5 #speed -= 20
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
        setMotorContorl(pwmB, IN3, IN4, speed, stat) #speed+30
        time.sleep(1)  #time.sleep(2)
            
        #if speed <= 25:
            #setMotor(0,STOP)
        
#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)


angle_time = 0
start = time.time()
end = time.time()
a = 0
b = 0

while (1):

    dist = DC.get_distance()
    pres = MP.count_pressure()
    angle = AgC.get_angle()
   
    if angle >45 :
        end = time.time()
        a = 1
        
    else:
        start = time.time()
        a = 0
    
    time_val = end - start
    
    if time_val >= 3.0 :
        angle_time = 1
        AC.sound_on()

        if time_val >= 8.0:
            Mail.send_mail()
            b = 0
    else:
        angle_time = 0

    if (wp.read_data() == 1 and a == 0 and 1 <= pres < 3):  
        if dist > 0.35:
            lcd.get_lcd(4) # OK (작동)
            setMotor(100,FORWARD)    
            b = 1   
		
    else:    
        AC.sound_off()
        if wp.read_data() == 0:
            lcd.get_lcd(1)  # Helmet Off  (헬멧 미 착용)

        elif wp.read_data() == 1 and pres < 1:
            lcd.get_lcd(2) # Helmet On (헬멧 착용, 주행자 미탑승)

        elif wp.read_data() == 1 and pres > 2:
            lcd.get_lcd(3) # Two People (헬멧 착용, 다중 탑승)
 
        if (a == 1 or b == 0):
            setMotor(0,STOP)
            
        elif (b == 1):
            lose_rpm(100,FORWARD)
  
    print(dist) 
 
    if (dist <= 0.75 or angle_time == 1):
        AC.sound_on()
        if (dist <= 0.35 and b == 1):
            setMotor(60,FORWARD)
    elif (dist >= 0.75 and angle_time == 0 and time_val < 3.0):
        AC.sound_off()
