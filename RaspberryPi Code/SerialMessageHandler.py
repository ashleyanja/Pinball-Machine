'''
Useful links:
https://www.elinux.org/Serial_port_programming
https://www.elinux.org/RPi_Serial_Connection#Preventing_Linux_using_the_serial_port
https://github.com/wimvanderbauwhede/limited-systems/wiki/First-steps-to-running-a-web-service-on-a-Raspberry-Pi
https://pyserial.readthedocs.io/en/latest/pyserial_api.html
'''

import serial
import requests
import GPIOHandler as GPIOH

def main():
    '''
    The first argument is port to open, if it does not work replace with: "/dev/ttyAMA0"
    Second argument is the baudrate, should not have to edit
    Third argument is the timeout, basically how many seconds can pass before it returns the information.
    Lower timeout means more realtime info, while a longer timeout is more efficient but not real time
    '''
    port = serial.Serial("/dev/ttyUSB1", baudrate=9600)

    # Send previous score to Basys3 via GPIO
    with open("prevscore.txt") as f:
        prevScore = f.readline().strip()
	print("Previous Score: " + str(prevScore))
        GPIOH.SendScoreToBasys(prevScore)

    while True:
	
        updatePoints(port)



def updatePoints(ser):
    data = readFromSerial(ser)

    # If Reset score
    if (data == "0"):
        
        # Send previous score to Basys3
	with open("/var/www/html/score.txt") as f:
		score = f.readline().strip()
		GPIOH.SendScoreToBasys(score)

	# Save previous score
	prevScoreFile = open("prevscore.txt", "w")
	print("Final Score: " + score)
	print >> prevScoreFile,score
	prevScoreFile.close()

    # Write score to file
    outFile = open("/var/www/html/score.txt","w")

    print("Score : " + data)
    print >> outFile,data

    outFile.close()



def readFromSerial(ser):
    #read in the data from the serial port
    data = ser.readline()
    #remove the last character to avoid new line
    return data[:-1]

main()
