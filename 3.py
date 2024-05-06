list1 = [1,2,3,4]
print(list("abcd"))
print(list1[0])
print(list1[-1])
print(list1[len(list1) - 1])

for n in list1:
    print(n, end=" ")
print()
for i in range(len(list1)):
    print(list1[i], end=" ")
list1 = [["a", "b"], ["c","d"]]
print(list1[0][0])
print(list1[0][1])

print(list1[1][0])
print(list1[1][1])

for row in list1:
    for col in row:
        print(col, end=" ")
    print()
  
# def A(n):
#     result = []
#     for i in range(1, n+1):
#         row = []
#         for j in range(1, n+1):
#             row.append(i*j)
#         result.append(row)
        
#     return result

# print(A(2))
        
        
# def B(list):
#     max = list[0][0]
#     for i in list:
#         for j in i:
#             if j > max:
#                 max = j
#     return max

# print(B([[1,2], [2,4]]))

students_info = []
for i in range(3):
    name = input("Enter student's name: ")
    math = float(input("Enter student's math score: "))
    computer = float(input("Enter student's computer score: "))
    students_info.append([name, math, computer])

print("student info before anything", students_info)   
def A(students_info):
    for i in range(len(students_info)):
        m = (students_info[i][1] + students_info[i][2])/2
        students_info[i].append(m)
        
A(students_info)
print("student info after something", students_info)