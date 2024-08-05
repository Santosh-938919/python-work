num=int(input("enter the numner"))
temp=num
rev=0
while(num>0):
  dig=num%10
  rev=rev*10+dig
  num=num//10


print(rev)


# we can do like this also

# num=int(input("enter the numner"))
# print("revesed no"+str(num)[::-1])
