#wap to input coordinate and determine its quadrant
x=int(input("enter the x coordinate"))
y=int(input("enter the y coordinate"))
if x>0 and y>0:
	print("1st quadrant")
elif x>0 and y<0:
	print("4th quadrant")
elif x<0 and y>0:
	print("2nd quadrant")
else:
	print("3rd quadrant")