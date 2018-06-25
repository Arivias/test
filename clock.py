import matplotlib.pyplot as plt
import time
import math

def sleep(ms):
	now = round(time.time()*1000)
	while round(time.time()*1000) < now + ms:
		asdf=0

def x(t):
	t*=6
	return math.degrees(math.cos(t))/0.5
def y(t):
	t*=6
	return math.degrees(math.sin(t))/0.5

#print ("a")
#sleep(2000)
#print("b")

origin=0.5
tim=0

while 1:
	plt.axis([0,1,0,1])
	plt.plot([0.5,0.5+x(tim)],[0.5,0.5 + y(tim)])
	sleep(1000)
	tim+=1
	plt.pause(0.05)
	plt.cla()
