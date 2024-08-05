year=int(input("enter the year"))
if year%4==0 or year%400==0  or year%100==0:
  print("leap year")
else:
  print("it is not leap year")