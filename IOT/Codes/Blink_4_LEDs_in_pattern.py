import RPi.GPIO as GPIO 
import time 
 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(11,GPIO.OUT) 
GPIO.setup(12,GPIO.OUT) 
GPIO.setup(15,GPIO.OUT) 
GPIO.setup(16,GPIO.OUT) 
 
for i in range(5):     
  GPIO.output(11,True) 
  GPIO.output(12,False) 
  GPIO.output(15,False)     
  GPIO.output(16,False) 
  time.sleep(0.5) 
 
  GPIO.output(11,False) 
  GPIO.output(12,True) 
  GPIO.output(15,False)     
  GPIO.output(16,False) 
  time.sleep(0.5) 
 
  GPIO.output(11,False) 
  GPIO.output(12,False) 
  GPIO.output(15,True)     
  GPIO.output(16,False) 
  time.sleep(0.5) 
 
  GPIO.output(11,False) 
  GPIO.output(12,False) 
  GPIO.output(15,False)     
  GPIO.output(16,True) 
  time.sleep(0.5) 
 
GPIO.cleanup() 

