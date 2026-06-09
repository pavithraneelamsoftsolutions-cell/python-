name = input("enter  employee name:")
basic = float("salary:")
hra = float (input("enter hra"))
da = float(input("enter da"))


gross_salary = basic+hra+da

print ("employee name",name)
print (" gross salary",gross_salary)

print( "salary above 30000:",gross_salary)
print("salary between 30000 and 50000:",gross_salary>=30000 and gross_salary>=50000)
