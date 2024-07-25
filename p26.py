#wap to convert binary to decimal equivalent
n=int(input("enter no in binary"))
decimal = 0
power = 1
while n>0:
	rem = n%10
	n=n//10
	decimal += rem*power
	power = power*2
print(decimal)
