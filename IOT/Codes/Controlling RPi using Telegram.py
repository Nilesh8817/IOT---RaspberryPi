import time,datetime 
import RPi.GPIO as GPIO 
import telepot 
from telepot.loop import MessageLoop 
 
led=6 
 
now=datetime.datetime.now() 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
 
GPIO.setup(led,GPIO.OUT) 
GPIO.output(led,0) 
 
def action(msg):     
  char_id=msg['chat']['id']    
  cmd=msg['text']     
  print('Received: %s' %cmd) 
 
    if 'on' in cmd:         
      message = "on "         
      message=message+"led"         
      GPIO.output(led,1)         
      message=message+"light" 
      
        telegram_bot.sendMessage(char_id,message) 
 
    if 'off' in cmd: 
      message = "off "         
      message=message+"led"         
      GPIO.output(led,0)         
      message=message+"light" 
        
        telegram_bot.sendMessage(char_id,message) 
 
telegram_bot=telepot.Bot(' *** ACCESS KEY TOKEN *** ') 
print(telegram_bot.getMe()) 
MessageLoop(telegram_bot,action).run_as_thread() 
print('Up and Running..') 
 
while 1: 
   time.sleep(10) 
