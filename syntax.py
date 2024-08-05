# print("sno:",1)
# print("name:","santosh prasad")
# print("roll no:",80)
# print("age:",21)

# join one statement by / backslash

# if 100>10 and \
# 9<=5 and \
# True!=False and \
# False==False:
#   print("correct condition")

# spreading the content in variable
# list=[20,30,
#       40,50,
#       60,45,
#       450,70]
# print(list)

# funtion block
# we can do in this in idle shell or attractive gui shell
# def sant(mes):
#   print("hello",mes) 


# complex variable example
# a=5+9J
# b=6+2j
# c=a*b
# print(c)

# str="santosh prasad"
# print(len(str))
# print(str[-5])

# print("santosh \\ prasad")
# a="santosh"
# b="prasad"
# print(a+b)
# print(a*3)
# print(a[0:3])
# print(a.upper())
# print(b.lower())
# print("n" in a)
# print(a.replace(a,"sangt"))


# list and multiple inner list
# list=["santosh ","prasad",2,7.8,True,None]
# print(list[0:3])

# data=[1,2,3,[4,5,6,[7,8,[9]]],10]
# print(data)
# print(data[0])
# print(data[3])
# print(data[4])
# print(data[3][0])
# print(data[3][3])
# print(data[3][3][0])
# print(data[3][3][2])

# different data converted in list

# num=list("santosh")
# print(num)
# num=dict({1:"santosh",2:"prasad"})
# print(num)
# num=list((40,20,30))
# print(num)
# num=list({400,500,600})
# print(num)

# iterate through list
# num=[1,2,3,4]
# for var in num:
#   print(var)


# tuples
# tup=(1,)
# print(tup)
# print(len(tup))

# list=["santosh","prasad"]
# list.append("ravisannu")
# list.remove("santosh")

# print(list)

# tpl=tuple([1,2,3,4])
# tpl=tuple({1,2,3,4})
# print(type(tpl))


# set variable
# odd={1,3,5,7,9 ,3,9,7,4,5}
# stu={1,'santosh',10.5,True}
# print(odd)
# print(stu)

# s=set()
# s.add(10)
# s.add(20)
# s.add(30)
# print(s)
# num={2,3,4,5}
# s.update(num)
# print(s)
# s.remove(3)
# print(s)

# operation of set

# s1={1,2,3}
# s2={2,3,4}
# print(s1.union(s2))

# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1. symmetric_difference(s2))

# dictionary variable

# roll={"1":"santosh","2":"prasad"}
# print(roll["2"])

# dict=dict(i='one',ii='two',iii='three')
# print(dict['i'])
# empty=dict()
# print(empty)


# for key in roll:
#   print("key="+key+",value="+roll[key])

# del roll["1"]
# print(roll)
# print(roll)
# delvalue=roll.pop("2")
# print("deleted value is :",delvalue)
# print(roll.popitem())
# print(roll)


# print(roll.key())
# d1 = {'name': 'santosh', 'age': 21, 'marks': 80, 'course': 'BCA'}
# print(d1.keys())
# print(d1.values())

# d1 = {'name': 'santosh', 'age': 21, 'marks': 80, 'course': 'BCA'}

# print('name'in d1)
# if('name' in d1):
#   print("key is found")
# else:
#   print("key is not found")


# d1={"name":"santosh","age":25, "rollno":1}
# d2={"name":"Vaibhav","age":23, "rollno":50}
# d3={"name":"Shanku", "age":20, "rollno":30}
# stu={1:d1,2:d2,3:d3}
# print(stu)
# print(stu[]["name"])


# local varible

# def msg():
#     name = 'santosh'
#     print('Hello ', name)
# msg()
# print(msg)


# global variable
# name = 'santosh'
# def msg():
#     global name
#     name = 'prasad'
#     print('Hello ', name)
# msg()
# print(name)


