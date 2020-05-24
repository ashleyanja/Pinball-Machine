import RPi.GPIO as GPIO
import time

# Pins on the raspberry pi
PIN_DATA = [18,17,15,27,14,4,3,2]

def SendScoreToBasys(score_decimal):
	GPIO.setwarnings(False)

	GPIO.setmode(GPIO.BCM)

	for i in range(8):
		GPIO.setup(PIN_DATA[i], GPIO.OUT)

	binary_score = str(format(int(score_decimal), '#010b'))[2:]
	print("GPIO output: " + str(binary_score))

	for i in range(8):
		GPIO.output(PIN_DATA[i], int(binary_score[i]))
		
	time.sleep(3)
