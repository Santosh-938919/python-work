# str=(input("enter the string:"))
# v=['a','e','i','o','u']
# c=0
# r=[]

# for i in range(len(str)):


#   if str[i] in v:
  
#     c+=1
#     r=r+str[i]
# if c == 0:
     
#      print("it is not vowel")
# else:
#     print("it is vowel",c,r)
    
 
# string=input("enter the syring")
# v=['a','e','i','o','u']
# r=""
# for i in range(len(string)):
#   if string[i] not in v:
#     r=r+string[i]

# print("\n after removing vowels:",r)   

string=input("enter the string")
v=['a','e','i','o','u']
r=""
for i in range(len(string)):
  if string[i] in v:
    r=r+string[i]

print("vowel in string:",r)    

