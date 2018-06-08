import serial
import time
import httplib2 
ser = serial.Serial('COM3', 9600) 
ser.baudrate = 9600
a = 0
b = 0
while True:
	ch = ser.readline()
	a = float(ch[0:4])
	b = float(ch[6:10])
	conn = httplib2.Http() 
	conn.request("http://api.thingspeak.com/update?key=88O2KI49L8SZ1XWA&field1={0}&field2={1}".format(a,b))
	print "sent {0} {1}".format(a,b)
	time.sleep(1)