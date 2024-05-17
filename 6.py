# x = '1.5'
# print(type(x))
# print(x[0])
# print(x[1])
# print(x[2])

# message = 'hello every one "say something"'
# print(message)
# message = "hello every one \"say something\""
# print(message)

# message = "hello every one\nwelcome to python class"
# print(message)
# message = """hello every one 
# welcome to python class"""
# print(message)
# message = '''hello every one 
# welcome to python class'''
# print(message)

# message = '''hello every one "say something"'''
# print(message)

# name = input("enter a name: ")
# family = input("enter a family: ")

# print(name + " " +family)
# print(name, family)
# print(f"{name} {family}")
# print("%s %s"%(name, family))


# x = int(input("enter a number: "))
# y = int(input("enter a number: "))

# print(x + y)

# x = "*" * 3
# print(x)

# x = [1,2]
# print(x * 5)

# name = input("enter a name: ")
# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[len(name) - 1])

# for char in name:
#     print(char, end=" ")
# print()   
# for i in range(len(name)):
#     print(i, name[i])
    
# for item in enumerate(name):
#     print(item[0], item[1])
# for i, val in enumerate(name):
#     print(i, val)
    

# for x,y in enumerate("sa"):  
    
#     print(x,y)
# import string
# x = "abc12bf67b4by"
# all_digits = string.digits

# def my_is_decimal(char):
#     if char in all_digits:
#         return True
#     return False
# s = 0
# for item in x :
#     if my_is_decimal(item):
#         s += int(item)
# print(s)
    
# x = "abc12bf67b4by"
# all_digits = string.digits

# s = 0
# for val in x:
#     if val in all_digits:
#         s += int(val)
# print(s)
        
   
# s = 0
# for item in x:
#     if item.isdecimal():
#         s += int(item)
        
# print(s)
        
        
# l1 = [1,2,3,4,5,6,7]
# l2 = [1,"ali", "sara", 100, 10.6, 10.3]

# def sum_of_even_odd_numbers(items):
#     s_odd = 0
#     s_even = 0
#     for item in items:
#         if type(item) == int:
#             if int(item) % 2 == 0:
#                 s_even += float(item)
#             else:
#                 s_odd += float(item)
#         elif type(item) == float:
#             if int(str(item).split(".")[-1]) % 2 == 0:
#                 s_even += item
#             else:
#                 s_odd += item
                
#     return s_even, s_odd
                
# print(sum_of_even_odd_numbers(l1))
# print(sum_of_even_odd_numbers(l2))


# numbers = [1,2,3,4,5,6,1,1,3,2,4,2]
# print(numbers.count(2))

# count = 0
# for number in numbers:
#     if number == 2:
#         count += 1
# print(count)


numbers = [[1,2],[3,4,5,6,2],[1,2,2,2,0],[1,2,3,4,2]]
# c = 0
# for row in numbers:
#     for col in row:
#         if col == 2:
#             c += 1
# print(c)

i = 0
c = numbers[0].count(2)
for index,row in enumerate(numbers):
    if  row.count(2) > c:
        c = row.count(2)
        i = index
print(i)