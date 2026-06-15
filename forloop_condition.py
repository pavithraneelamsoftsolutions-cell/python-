# #  even number program  i use for loop +if 

# for i in range(1,11):
#     if i%2==0:
#         print(i)

# #  voting eligiblity 

# for i in range(1,6):
#     age=int(input("enter age:"))
#     if age>=18:
#         print("eligible for vote ")



# # even  or odd number  
 
# for i in range (1,11):
#     if i %2==0:
#         print(i,"even number")
#     else:

#       print(i,"odd number")

# # student  fail or pass
# for i in range (1,7):
#     mark= int(input("enter mark:"))
#     if mark>=35:
#         print("pass")
#     else:
#         print("fail")

# for loop + elif 

# grade  calculator:

# for  i in range(1,4):
#     mark = int(input("enter  a mark"))
#     if mark>=90:
#         print("grade A")
#     elif mark >=75:
#         print("grade B")
#     elif mark >=50:
#         print("grade C")
#     else:
#         print("fail")

# nested if  else  in for loop 
# scholarship eligiblity

for i in range (1,4):
    mark = int(input("enetr mark:"))
    attendence= int(input("entre  attendence:"))
    if mark>=80:
        if attendence >=75:
            print("eligible for scholarship")
        else:
            print("attendence less than 75")
    else:
        print("mark less than 80")