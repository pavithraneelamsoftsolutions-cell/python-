a=[10,20]
b=[10,20]
print("is opertr", a is b)

a=[10,20]
b=a
print("is opertor :",a is b)

# # == vs is 
# a=[10,20]
# b=[10,20]

# print(a==b)


# is not :
a=[1,2]
b=[1,2]
print ("is not ",a is not b)

a=[1,2]
b=a
print("is not",a is not b)

name = None
print( name is None)

a= None
if a is None:
    print("variable is empty")
else:
    print("variable has value")


lang=["python","java","c"]
search_lag="ruby"
if search_lag not in lang:
    print(f"yes,{search_lag} is not in the list")
else:
    print(f"no,{search_lag} is already in the list")