# ultrasonic orignal code
# https://pimylifeup.com/raspberry-pi-distance-sensor/
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
timeout = time.time() + 60*5   # 5 minutes from now
while True:
	test = 0
	if test == 5 or time.time() > timeout:
		brake
	test = test -1
	try:
		GPIO.setmode(GPIO.BOARD)
		PIN_TRIGGER = 7
		PIN_ECHO = 11
		GPIO.setup(PIN_TRIGGER, GPIO.OUT)
		GPIO.setup(PIN_ECHO, GPIO.IN)
		GPIO.output(PIN_TRIGGER, GPIO.LOW)
		print "Waiting for sensor to settle"
		time.sleep(2)
		print "Calculating distance"
		GPIO.output(PIN_TRIGGER, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(PIN_TRIGGER, GPIO.LOW)
		while GPIO.input(PIN_ECHO)==0:
				pulse_start_time = time.time()
		while GPIO.input(PIN_ECHO)==1:
				pulse_end_time = time.time()
		pulse_duration = pulse_end_time - pulse_start_time
		distance = round(pulse_duration * 17150, 2)
		print "Distance:",distance,"cm"

finally:
      GPIO.cleanup()

