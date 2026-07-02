# text=input("enter your text:")

# print("uppercase",text.upper())
# print("lowercase",text.lower())
# print("title",text.title())
# print("replace word",text.replace("java","python"))
# print("find",text.find("a"))
# print("cont",text.count("a"))
# print("split",text.split())


# student registration system :
student_name=input("enter student name:")
age = int(input("enter  age:"))
marks= int(input ("enter  marks"))
email= input("enter your email:")


marks+=10
name = student_name.title()

if '@' not in email:
    print("invalied email")
else:
    if age>=18 and marks >=40:
        print("student details:")
        print("student name:",name)
        print("age:",age)
        print("marks:",marks)
        print("email:",email)
        print("status: pass")
    elif age>=18 and marks <=40:
        print("fail")
    elif age<18 and marks >=40:
        print("age is not eligible")
    else:
        print("not eligible")

print("character name")
for i in name:
    print(i)
