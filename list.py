# string=input("enter the string")
# h=string.slice()
# print(h)
# # h.append("santosh")

# print(h)

# l1=[1,'santosh','apple']
# l2=[2,'hellio','da']
# l1.append("green")
# l1.append("yellow")
# l1.append("black")
# print(l1)
# l1.remove("santosh")
# l2.append("hii")
# l2.remove("da")
# print(l2)
# s1=l1+l2
# print(s1)

# a="hello"
# b="santosh"
# c=a+b
# print(c)

# course=["sant","hell","kaise ho"]
# course[0]="santosh"
# course[1]="hello"
# course.append("prasad")
# # del course[0]
# # course.remove("santosh")
# course.pop(1)
# print(course)


# s= set()
# s.add(10)
# s.add(20)
# s.add(30)
# s.add(40)
# # print(s)
# printnum={1,2,3,4}
# s.update(printnum)
# s.remove(2)
# print(s)

s1={1,2,3,4,5} 
s2={4,5,6,7,8} 
s1|s2
print(s1,s2)
print(s2.union(s1))

# d = {} # empty dictionary

# numNames={1:"One", 2: "Two", 3:"Three"} # int key, string value

# decNames={1.5:"One and Half", 2.5: "Two and Half", 3.5:"Three and Half"} # float key, string value

# items={("Parker","Reynolds","Camlin"):"pen", ("LG","Whirlpool","Samsung"): "Refrigerator"} # tuple key, string value

# romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5} # string key, int value

# print(d)
# print(numNames)
# print(decNames)
# print(items)
# print(romanNums)



# roll = {"1":"Aditya", "2":"Mukul", "3":"Sneha"}
# for key in roll:
#     print("Key = " + key + ", Value = " + roll[key]) 


# length = 100

# if length > 100:
#     print("length is greater than 100")
# elif length == 100:
#     print("length is 100")
# elif length < 100:
#     print("length is less than 100")
    


# length = 50
# width = 5
# area = length*width

# if area > 100:
#     if area > 500:
#         print("area is greater than 500")
#     else:
#         if area < 500 and area > 400:
#             print("area is")
#         elif area < 500 and area > 300:
#             print("area is between 300 and 500")
#         else:
#             print("area is between 200 and 500")
# elif area == 100:
#     print("area is 100")
# else:
#     print("area is less than 100")

# num = 0

# while num < 5:
#     num += 1   
#     print('num = ', num)
#     if num == 3: # condition before exiting a loop
#         break

# for i in range(1, 5):
#     if i > 2:
#         break
#     print(i)


# for x in range(1,4):
#     for y in range(1,3):
#         print('x = ', x, ', y = ', y) 


# for x in range(2,10,2):
#     print(x)


# for x in range(10,0,-1):
#     print(x)


def mult(a,b):
    return a*b
def avrg(x, y):
    return (x + y)/2
def power(x, y):
    return x**y


# import sys
# print(sys.path)
# import statistics
# print(statistics.mean([2,5,6,9,12,16,20]))
# print(statistics.median([1,2,3,8,9]))
# print(statistics.mode([2,5,3,2,8,3,9,4,2,5,6]))
# print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))


# def add(a, b): 
#     return a + b

# total=add(100, 200) 
# print(total)
# total=add(50, add(100, 200))
# print(total)


# def fn(**a):
#     for i in a.items():
#         print (i)
# fn(rollno=5,name="Aditya",age=20,program="BCA")

# x = lambda name : print('hello', name)
# x("santosh")


# sum = lambda x,y,z : x+y+z
# print(sum(4,5,6))
# sum = lambda *x: x[0]+x[1]+x[2]+x[3]  
# print(sum(4,5,6,5))


# msg = lambda : print('Hello BCA Class!')
# msg()

(lambda x: x*x)(5)
