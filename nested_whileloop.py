# i=1
# while i<=3:
#     j=1
#     while j<=2:
#         print(i,j)
#         j+=1
#     print() 
#     i+=1    

# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j+=1
#     print()
#     i+=1

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1


# i=1
# while i<=5:
#     j=0
#     while j<i:
#         print(chr(65+j),end=" ")
#         j+=1
#     print()
#     i+=1


# i=1
# while i<=3:
#     j=1
#     while j<=3:
#         print("*",end=" ")
#         j+=1
#     print()
#     i+=1


name ="text"
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])

name ="text"
print(name[0])
print(name[1])
print(name[2])
print(name[3])

name = "python"
print(len(name))

name = "product   details"
print(len(name))


name  = "python"

for i in name:
   print(i)

name = "kaviya"
i=0
while i<len(name):
    print(name[i])
    i+=1
name = "kaviya"
i= len(name)-1 
while i>=0:
    print(name[i])
    i-=1
    


name = "mango"
print(name[0:5])
print(name[1:4])
print(name[2:3])
print(name[1:])


# string concatination:
name  = "pavithra"
lastname="balakrishnan" 
text="hai"
print(name+lastname+text)
print(name+" "+lastname+" "+text)

#  string repitation
print("python"*3)

print("group \n"*3)

# membership operator :
name ="python"
print("z" in name)


name ="python"
print("y" not in name)


email_id="pavi@gmail.com"
if "@" in email_id:
    print("valied")
else:
    print("invalied")

email_id="pavi@gmail.com"
if "@" not in email_id:
    print("valied")
else:
    print("invalied")