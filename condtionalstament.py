# age = int (input("enter your age :"))
# if age>=18:
#     print ("eligible for vote:")
 
 
# mark = int(input("enter mark:"))
# if mark >=35:
#     print("pass")
# else:
#    print("fail")


# stude mark grade check


# mark =  int(input("enter mark:"))
# if mark>=90:
#    print("grade A")
# elif mark >=75:
#    print("grade B")
# elif mark>=50:
#    print("grade c")
# else:
#  print ("fail")

#  even or odd number 
# num = int(input("enter  a  number:"))
# if num%2==0:
#    print("even number")
# else:
#   print("odd number")

# pastive,native,zero

# if elif else 

# num = int(input("enter  the number:"))
# if num>0:
#     print("positive number")
# elif num<0:
#     print("nagative number")
# else:
#     print("zero")
# largest of two numbers :

# a =  int(input("enter a fisrt  number: "))
# b = int(input ("enter a second  number:"))
# c= int(input("enter a third number :"))

# if a>b and a>c:
#     print("largest number is A:",a)
# elif b>c:
#     print("largest number is B:",b)
# else:
#     print("largest number is C:",c)

# ATM withdrawal:
balance = 5000
amount = int(input("enter a withdrawal amount:"))
if amount<= balance:
    balance =balance-amount
    print("transaction successfully")
    print("remaining balance:",balance)

else:
    print(" insufficient balance")