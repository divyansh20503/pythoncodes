#wap to calculate gross salary
a=int(input("enter your salary"))
if 0<a<4001:
	print("The ga is:",a*0.1+a*0.5+a)
elif 4000<a<8001:
	print("The ga is:",a*0.2+a*0.6+a)
elif 8000<a<12001:
	print("The ga is:",a*0.25+a*0.7+a)
elif 12000<a:
	print("The ga is:",a*0.3+a*0.8+a)
else:
	print("invalid input")
