import time 
import AngleChecker as AC
import AlarmChecker as AmC
start = time.time()
end = time.time()

while True:
	if AC.get_angle() > 50:	
		end = time.time()
		print(end - start)
	
	elif AC.get_angle() < 50:
		start = time.time()
	
	time_val = end - start
		
	if time_val > 5.0:
		AmC.sound_on()
	
	elif time_val < 5.0:
		AmC.sound_off()
