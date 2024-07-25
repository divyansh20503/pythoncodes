#converting days to week year and days
a=int(input("enter any no"))
years = a // 365
weeks=(a-years*365)//7
days = (a - years * 365 - weeks*7)
print("Years = ", years)
print("Weeks=",weeks)
print("Days = ", days)