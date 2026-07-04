# fruits =["apple","grapes","mango","pineapple"]
# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])
# # print(fruits[3])
# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])
# print(fruits[-4])



# string_list = ["apple","mango","banana"]

# string_list[1]="watermelon"
# print(string_list)



# length of  list :

# string_list = ["apple","mango","banana","mango1"]
# print(len(string_list))

# list traversal:
# student =["ravi","rahul","kalai"]
# for  name  in student:
#     print(name)

# list  slicing:
# student =["ravi","rahul","kalai","kumar","devi"]
# print(student[0:4])

# append:
# student =["ravi","rahul","kalai","kumar","devi"]
# student.append("priya")
# print(student)


# insert()
# student =["ravi","rahul","kalai","kumar","devi"]
# student.insert(1,"priya")
# print(student)


# remove
# student =["ravi","rahul","kalai","kumar","devi"]
# student.remove("kalai")
# print(student)

# pop()
# student =["ravi","rahul","kalai","kumar","devi"]
# student.pop()
# print(student)

# # sort() assending order
# student =["ravi","rahul","kalai","kumar","devi"]
# student.sort()
# print(student)
# # sort() descending order
# student =["ravi","rahul","kalai","kumar","devi"]
# student.sort(reverse=True)
# print(student)

# # reverse  ()
# student =["ravi","rahul","kalai","kumar","devi"]
# student.reverse()
# print(student)

# # clear()
# student =["ravi","rahul","kalai","kumar","devi"]
# student.clear()
# print(student)

# # copy()
# student =["ravi","rahul","kalai","kumar","devi"]
# new_student=student.copy()
# print(new_student)

# # extend
# student =["ravi","rahul","kalai","kumar","devi"]
# new_student= ["zara","kavitha"]
# student.extend(new_student)
# print(student)

# # index()
# student =["ravi","rahul","kalai","kumar","devi"]
# print(student.index("ravi"))
# print(student.index("rahul"))
# print(student.index("kalai"))
# print(student.index("kumar"))
# print(student.index("devi"))


number=[10,20,10,40,60,10]
print(number.count(10))

student =["ravi","rahul","kalai","kumar","devi","ravi","devi","ravi"]
print(student.count("ravi"))
print(student.count("devi"))


# create empty list 

list=[]

# add 5 number using append

list.append(10)
list.append(20)
list.append(30)
list.insert(2,60)
print(list)

list.remove(30)
print(list)
print(len(list))
print(list.count(10))
# find the index of python 
lang=["java","python","c"]
print(lang.index("python"))


students =["ravi","rahul","kalai","kumar","devi","ravi","devi","ravi"]
unique_student=[]
for student in students: 
    if student not in unique_student:
        unique_student.append(student)
print("original ",students)
print("unique student",unique_student)


# student mark manager:
marks=[]
for i in range(5):
    mark= int(input(f"enter mark {i+1}:"))
    marks.append(mark)
print("\n marks:",marks)
