student_name =input("enter student name:")
age = int(input("enter age:"))

tamil=int(input("eneter tamil marks:"))
english =int(input("enter english mark:"))
maths = int (input("enter maths mark:"))

total=tamil+english+maths
average =total/3

is_pass = total>=105

eligible_scholarship= total>=250 and age<25

bonus_mark=0
bonus_mark+=5
final_total_mark= total+bonus_mark

print("---student report----")
print("Name:",student_name)
print("Age:",age)

print("Total Marks:",total)
print('Average:',average)
print("pass status:",is_pass)
print("scholarship_elligible:",eligible_scholarship)
print("bonus mark:",bonus_mark)
print("final total marks:",final_total_mark)


# # variables
# student_name
# age
# tamil
# english
# maths
# # input type 
# input 
# # type cast
# data   in string and  we used to convert integer

# # data types 

# String
# integer 

# # operators 

# arithmetic we are used in addition and divison

# comparison operators  >= 
# logical operators
# we used in and means both condition true the value is true 
# assignment operators
# bonus =0 first assign the value 
# bonus+=5 add and store values 
