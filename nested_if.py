age=22
degree = True
if age >=21:
   if degree:
    print("eligible for job")


# Atm withdrawal
# 1.amtm card  must be in valid
# 2.account balance must be in sufficient 

card_valid = True
balance =5000
if card_valid:
    if balance>=1000:
        print("withdrawal successfully")

# # college admission:
# condition 
# student must passed in 12th
# student mark above 75%

# student_12thpassed = True
# student_mark =70
# if student_12thpassed:
#     if student_mark>=75:
#         print("admission approved")

# driving license:

age =16
if age>=18:
    print("eligible")
else:
    print("not eligible")


age =20
has_document = True
if age>=18:
    if has_document:
        print("license aprroved")
    else:
        print("document missing")
else:
    print("age is not eligible")


# scholarship_elligible

# mark must  be 80 or above 
# attendance  must be 75% or above 

mark =80
attendance =50
if mark>=80:
    if attendance >=75:
        print("eligible for scholarship")

    else:
        print("attendence less than 75")
else:
    print("marks lessthan 80")