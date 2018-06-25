import random
def rand(i):
	return (random.randint(0,i)*random.randint(0,i))%i


def trapezoid(s):
    for c in range(len(s)+1):
        print(s[:c])
    for c in range(len(s)+1):
        print(" "*c+s[c:])


c="qwrtpsdfghjklzxcvbnm"
v="eyuioa"
count=20
ln=5
for words in range(count):
	w=""
	ch=0
	while ch<ln:
		w+=c[rand(len(c))]
		ch+=1
		if ch>=ln:
			break
		for vw in range(rand(3)):
			w+=v[rand(len(v))]
			ch+=1
			if ch>=ln:
				break
	trapezoid(w)
