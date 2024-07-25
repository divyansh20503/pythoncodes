#wap to print armstrong no or not
a=int(input("enter the no"))
b=0
d=0
d=d+a
while d>0:
	c=d%10
	b=b+c**3
	d=d//10
print(b)
if b==a:
	print("armstrong")
else:
	print("not armstrong")
