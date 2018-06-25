def trapezoid(s):
    for c in range(len(s)+1):
        print(s[:c])
    for c in range(len(s)+1):
        print(" "*c+s[c:])


while(1):
	try:
		trapezoid(input("trapezoid: "))
	except KeyboardInterrupt:
		print("\n\nk thx bai\n")
		break
