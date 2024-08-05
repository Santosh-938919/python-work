# f=open("sant.txt","w")
# f.write("kaise ho aap santosh")
# f.close()
# f=open("sant.txt","rt")
# # print(f.read(14))
# print(f.readline())
# f.close()


# f=open("sant.txt","rt")
# for x in f:
#   print(x)

# import os
# # os.remove("hello.txt")
# if os.path.exists("hello.txt"):
#   os.remove("hello.txt")
# else:
#   print("the file does not exist")

# with open("sant.txt") as f:
#   data=f.read()
#   print(data)

# with open("sant.txt" ,"a") as f:
#   f.write("hello Bca !!!")


# with open ("sant.txt","r") as f:
#   data=f.readlines()
#   for i in data:
#     word= i.split()
#     print(word)



# with open("sant.txt","r") as f:
#   for l in f:
#     for y in l.split():
#       print(y)

f=open("sant.txt","r")
while 1:
  char = f.read(1)
  if not char:
      break
  print(char)
f.close()  