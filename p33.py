class Bulldog(): #super,parent,base class
	def grawl(self):
		print("Bruno")
		print("Gurr.....Gurr.....!!")
class Rundog(Bulldog): #one class occur the property of another class,child,sub,derive class,inheritence
	def bark(self):
		print("Sheru")
		print("Bho....Bho....!!!")
dog=Rundog()
dog.bark()
dog.grawl()