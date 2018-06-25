import random

array = []
bestI=0
bestV=-100
ln = 10
runs = 100
for i in range(ln):
	array.append(1/random.randint(0,100))
print(array)
for i in range(runs):
	
