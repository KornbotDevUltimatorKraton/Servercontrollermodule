from flask import Flask,render_template, request # import flask for the web application deployment function 
import pyfirmata # Hardware control function 
import RPi.GPIO as GPIO  # Setting the raspberry pi zero w to activate the GPIO 
import Adafruit_DHT # DHT22 sensor temperature measurement 
import sys 
import numpy as np # Numpy for the machine learning function 
import math # Import math for some mathermaticfunction calculation 
import time # Timer for the on off push switch function 
#from sklearn.model_selection import train_test_split # Model train test selection 
#from sklearn.linear_model import LinearRegression  # Linear regression  
#from matplotlib import style 
app = Flask(__name__) #build web app temperature
GPIO.setmode(GPIO.BCM) # Setting the GPIO Channel
GPIO.setwarnings(False)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      # Feedback from the sensor digital feed back 
feed1 = 10
feed2 = 9
feed3 = 11
feed4 = 25
feed5 = 8
feed6 = 7
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  #Pins for the reset computer 
r1 = 13 
r2 = 19 
r3 = 26
r4 = 16 
r5 = 20 
r6 = 21     
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
       #Feed back GPIO sensor feed back on active device 
GPIO.setup(feed1, GPIO.OUT)
GPIO.setup(feed2, GPIO.OUT)
GPIO.setup(feed3, GPIO.OUT)
GPIO.setup(feed4, GPIO.OUT)
GPIO.setup(feed5, GPIO.OUT)
GPIO.setup(feed6, GPIO.OUT) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
      # Reset pin function for the  relay control 
GPIO.setup(r1, GPIO.OUT)
GPIO.setup(r2, GPIO.OUT)
GPIO.setup(r3, GPIO.OUT)
GPIO.setup(r4, GPIO.OUT)
GPIO.setup(r5, GPIO.OUT)
GPIO.setup(r6, GPIO.OUT)

# Handleling the first hardware connection support 
try: 
   hardware = pyfirmata.ArduinoMega("/dev/ttyUSB0") #USB serial connection hardware 
   print("Successfully connect hardware 1")
   # Initial setting logic low 
   FanT1 = hardware.get_pin('d:2:p')
   p1 = hardware.get_pin('d:3:p') 
   p2 = hardware.get_pin('d:4:p')
   p3 = hardware.get_pin('d:9:p')
   p4 = 5 
   p5 = 6 
   GPIO.setup(p4, GPIO.OUT) # Setting the GPIO pin 5  out 
   GPIO.setup(p5, GPIO.OUT) # Setting the GPIO pins 6  out
   p6 = hardware.get_pin('d:12:p')
   FanT1.write(0)
   p1.write(0)
   p2.write(0) 
   p3.write(0) 
   GPIO.output(p4,GPIO.LOW) 
   GPIO.output(p5,GPIO.LOW)  
   p6.write(0)
   # Reset pins 
   GPIO.setup(r1, GPIO.LOW)
   GPIO.setup(r2, GPIO.LOW)
   GPIO.setup(r3, GPIO.LOW)
   GPIO.setup(r4, GPIO.LOW)
   GPIO.setup(r5, GPIO.LOW)      
   GPIO.setup(r6, GPIO.LOW)
except: 
   print("Searching hardware........")
   try:
      hardware = pyfirmata.ArduinoMega("/dev/ttyUSB1")
      print("Connection second option function now online!")
      FanT1 = hardware.get_pin('d:2:p')
      p1 = hardware.get_pin('d:3:p')
      p2 = hardware.get_pin('d:4:p')
      p3 = hardware.get_pin('d:9:p')
      p4 = 5
      p5 = 6
      GPIO.setup(p4, GPIO.OUT) # Setting the GPIO pin 5  out
      GPIO.setup(p5, GPIO.OUT) # Setting the GPIO pins 6  out
      p6 = hardware.get_pin('d:12:p')
      FanT1.write(0)
      p1.write(0)
      p2.write(0)
      p3.write(0)
      GPIO.output(p4,GPIO.LOW)
      GPIO.output(p5,GPIO.LOW)    
      p6.write(0)
         #Reset pins 
      GPIO.setup(r1, GPIO.LOW)
      GPIO.setup(r2, GPIO.LOW)
      GPIO.setup(r3, GPIO.LOW)
      GPIO.setup(r4, GPIO.LOW)
      GPIO.setup(r5, GPIO.LOW)
      GPIO.setup(r6, GPIO.LOW)
   except:
       print("Fail to connect second option please checking your physical hardware !")
# Handleing the second hardware connection support 
#try: 
#   hardware1  = pyfirmata.ArduinoMega("/dev/ttyUSB1")
#   print("Successfully connected hardware 2")
#except: 
#   print("Faile to connect the hardware 2")
#   try:
#     hardware = firmata.ArduinoMega("/dev/ttyUSB2")
#     print("Second hardwae connection successfully") 
#   except: 
#     print("Fail to connect the second option 2 hardware please checking your phtsical hardware !") 
#humidity = 0 
#temperature = 0 
#humidity,temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4) # Access pin 4 for the first temperature sensor 
#Temperature and humidity sensor and analog gpio read control funtion
   # Feed back logic from the computer to tell that computer turn on or turn off 
lp1 = 0  # computer 1 
lp2 = 0  # Computer 2 
lp3 = 0  # Computer 3 
lp4 = 0  # Computer 4 
lp5 = 0  # Computer 5 
lp6 = 0  # Computer 6 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Sensor pins activity define 
Sensor1 = 0
Sensor2 = 1
Sensor3 = 2
Sensor4 = 3
Sensor5 = 4
Sensor6 = 5
# List running pins 
Liston = [3,4,9,12,2]
Listdict = [5,6]
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@app.route("/")
def index2(): 
     #Reading the activity if the temperature humidty and gpio control 
     humidity = 0
     temperature = 0
     #Sensor preset define
     Sensor1 = 0 
     Sensor2 = 1
     Sensor3 = 2
     Sensor4 = 3
     Sensor5 = 4 
     Sensor6 = 5
     #Enable the actuators
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     #FanT1 = hardware.get_pin('d:2:p')   #Fan control 
     #PowerR1 = hardware.get_pin('d:4:p') #Power control relay
     #ResetR2 = hardware.get_pin('d:3:p') #Reset control relay 
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     #Enable sensor iterator 
     it = pyfirmata.util.Iterator(hardware) 
     it.start() 
     hardware.analog[Sensor1].enable_reporting() 
     hardware.analog[Sensor2].enable_reporting() 
     hardware.analog[Sensor3].enable_reporting() 
     hardware.analog[Sensor4].enable_reporting()
     hardware.analog[Sensor5].enable_reporting() 
     hardware.analog[Sensor6].enable_reporting()  
     #Sensor setting for reading function 
     Comps1 = hardware.analog[Sensor1].read() 
     Comps2 = hardware.analog[Sensor2].read() 
     Comps3 = hardware.analog[Sensor3].read() 
     Comps4 = hardware.analog[Sensor4].read() 
     Comps5 = hardware.analog[Sensor5].read() 
     Comps6 = hardware.analog[Sensor6].read()
     # Feed back logic response
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
     lp1 = GPIO.input(feed1)
     lp2 = GPIO.input(feed2)
     lp3 = GPIO.input(feed3)
     lp4 = GPIO.input(feed4)
     lp5 = GPIO.input(feed5)
     lp6 = GPIO.input(feed6) 
     #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     humidity,temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
     # Activity details reading here  
     FanT1.write(1)
     templateData = {
     'title' : 'Server activity and status',
     'Header1': 'Server temperature and humidity',
     'Temperature': str(temperature),
     'Humidity': str(humidity),   
     'Header2': 'Server status',
     'Comp1':  str(Comps1),
     'Comp2':  str(Comps2),
     'Comp3':  str(Comps3),
     'Comp4':  str(Comps4),
     'Comp5':  str(Comps5), 
     'Comp6':  str(Comps6),
     'Header22':'Active feedback online', 
     'lps1': str(lp1), 
     'lps2': str(lp2), 
     'lps3': str(lp3), 
     'lps4': str(lp4), 
     'lps5': str(lp5), 
     'lps6': str(lp6),
     'Header3': 'Activate server online' 
     }
     return render_template('index2.html', **templateData)
@app.route("/<deviceName>/<action>")  
def action(deviceName,action): 
         if deviceName == 'FanT1':
                actuator = FanT1   
         if deviceName == 'p1': 
                actuator = p1
         if deviceName == 'p2': 
                actuator = p2 
         if deviceName == 'p3': 
                actuator = p3 
         if deviceName == 'p4': 
                actuator = p4 
         if deviceName == 'p5': 
                actuator = p5 
         if deviceName == 'p6': 
                actuator = p6
         if deviceName == 'Allcom': 
                actuator = "Onall"
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                           # Reset pins function  
         if deviceName == 'Reset1':
                actuator = 13  
         if deviceName ==  'Reset2':
                actuator = 19 
         if deviceName == 'Reset3': 
                actuator = 26 
         if deviceName == "Reset4":
                actuator = 16 
         if deviceName == "Reset5": 
                actuator = 20
         if deviceName == 'Reset6': 
                actuator = 21
         # Reset all mode 
         if deviceName == "ResetAll":
                actuator = "resetAll"
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         if action == 'on':
               FanT1.write(1)  
               actuator.write(1) 
               time.sleep(0.3)
               actuator.write(0)

         if action == 'off':
               FanT1.write(0)
               actuator.write(1)
               time.sleep(8)    
               actuator.write(0)

         if action == 'son':
                    GPIO.output(actuator, GPIO.HIGH)
                    time.sleep(0.3)
                    GPIO.output(actuator, GPIO.LOW)
         if action == 'soff':
                    GPIO.output(actuator, GPIO.HIGH)
                    time.sleep(8)   #Hit the button longer  
                    GPIO.output(actuator, GPIO.LOW) 
         if action == 'Allon':
                   if actuator == "Onall": 
                         Liston = ['p1','p2','p3','p6','FanT1']
                         Listdict = [5,6]
                         p1.write(1)
                         time.sleep(0.5)   # Delay time computer 1 
                         p1.write(0)
                         p2.write(1)
                         time.sleep(0.5)   # Delay time computer 2 
                         p2.write(0)
                         p3.write(1)
                         time.sleep(0.5)   # Delay time computer 3 
                         p3.write(0)
                         p6.write(1)
                         time.sleep(0.5)   # Delay time computer 6 
                         p6.write(0)           
                         FanT1.write(1)
                         for r in range(0,int(len(Listdict)-1)):   #Looping computer 5 and 6

                                     GPIO.output(Listdict[r], GPIO.HIGH)
                                     time.sleep(0.5) 
                                     GPIO.output(Listdict[r], GPIO.LOW)
         if action == 'Alloff':
                      if actuator == "Onall":
                         Liston = ['p1','p2','p3','p6','FanT1']
                         Listdict = [5,6]
                         #for i in range(0,int(len(Liston)-1)):
                         p1.write(1)
                         time.sleep(8)
                         p1.write(0)
                         p2.write(1)
                         time.sleep(8)
                         p2.write(0)
                         p3.write(1)
                         time.sleep(8)
                         p3.write(0)         
                         p6.write(1)
                         time.sleep(8)
                         p6.write(0)                
                         FanT1.write(0)
                         for r in range(0,int(len(Listdict)-1)):
                                     GPIO.output(Listdict[r], GPIO.HIGH)
                                     time.sleep(8)
                                     GPIO.output(Listdict[r], GPIO.LOW)
         #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                            #Reset button function 
         if action == 'reset': # detecting the reset function from the web interface 
                       GPIO.output(actuator, GPIO.HIGH) # Logic high pins 
                       time.sleep(0.5)
                       GPIO.output(actuator, GPIO.LOW) # Logic Low pin 
         if action == 'resetAll': # Call function for all reset option 
                       listreset = [13,19,26,16,20,21]  #List pins for reset fuction 
                       for s in range(0,int(len(listreset)-1)):  # List pins for reset function 
                                   GPIO.output(listreset[s], GPIO.HIGH)
                                   time.sleep(0.5) #time delay 5 millli sec 
                                   GPIO.output(listreset[s], GPIO.LOW)    

         #Computer on each unit response signal display function for the confirmation of the activation 
         Comps1 = hardware.analog[Sensor1].read() # Sensor read the activity if the computer Logic TTL reading input 
         Comps2 = hardware.analog[Sensor2].read() # Sensor read the activity computer 2 
         Comps3 = hardware.analog[Sensor3].read() 
         Comps4 = hardware.analog[Sensor4].read() 
         Comps5 = hardware.analog[Sensor5].read() 
         Comps6 = hardware.analog[Sensor6].read()
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>       
         lp1 = GPIO.input(feed1)
         lp2 = GPIO.input(feed2)
         lp3 = GPIO.input(feed3)
         lp4 = GPIO.input(feed4)
         lp5 = GPIO.input(feed5)
         lp6 = GPIO.input(feed6)       
         templateData = {

               'Comp1':Comps1,  # Computer 1 status 
               'Comp2':Comps2,  # Computer 2 status 
               'Comp3':Comps3,  # Computer 3 status 
               'Comp4':Comps4,  # Computer 4 status 
               'Comp5':Comps5,  # Computer 5 status 
               'Comp6':Comps6,   # Computer 6 status
               'lps1':lp1, 
               'lps2':lp2,
               'lps3':lp3, 
               'lps4':lp4, 
               'lps5':lp5, 
               'lps6':lp6
         }
         return render_template('index2.html', **templateData)
#if humidity is not None and temperature is not None:
#        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#   print('Failed to get reading. Try again!')
#   sys.exit(1)
if __name__ =='__main__': # All app runing on the web and deploy 
         app.run(host='0.0.0.0', port=80, debug=True) # Running the host ip  
