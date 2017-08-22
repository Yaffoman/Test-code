import time
import RPi.GPIO as GPIO
trig = 13
echo = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(trig, GPIO.OUT)
GPIO.output(trig, False)

time.sleep(.5)
print ("Starting...")
GPIO.output(trig, True)
time.sleep(.00001)
GPIO.output(trig, False)
print ('triggered')
start = time.time()

while GPIO.input(echo) == 0:
    start = time.time()

while GPIO.input(echo) == 1:
    stop = time.time()

elapsed = stop - start
distance = elapsed * 34300 / 2
print ("Distance : %.1f" % distance)
GPIO.cleanup()
