a=float(input("enter the no of unit consumed"))
if 0<a<150:
	print("The unit is:",a*2.40)
elif 150<a<300:
	print("The bill is:",150*2.40+(a-150)*3.00)
elif 300<a:
	print("The bill is:",150*2.40+150*3.00+(a-300)*3.20)
else:
	print("invalid input")
