# Armstrong number.
# II. Fibonacci series.
# III. Factorial of a number.
# IV. Palindrome of a number.

# num=int(input("enter the number"))
# temp=num
# rev=0
# while num>0:
#   sum=num%10
#   rev=rev+ pow(sum,3)
#   num//=10 
# if rev==temp:
 
#     print("it is  armstrong")
# else:
#     print("it is not armstrong")



num=int(input("enter the number"))
temp=num
rev=0
while num>0:
  sum=num%10
  rev=rev+pow(sum,3)
  num//=10
if (rev==temp):
  print("it is armstrong number")

else:
  print("it is not armstrong number")  