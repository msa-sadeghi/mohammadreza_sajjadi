# lower = 1
# upper = 7
# counter = 0
# for i in range(lower, upper + 1):
#     if i > 1:
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             counter += 1
            
# print(counter)



# for i in range(4):
#     x = input("> ")
#     if x == "0":
#         break
    
# else:
#     print("salaam",i)



# def is_prime_number(num):
#     res = True
#     for i in range(2, num):
#         if num % i == 0:
#             res = False
#             break
#     return res
            
# x = int(input("enter a number: "))
# print(is_prime_number(x))

all_names = []
counts = {}
for i in range(3):
    name = input("enter a name: ")
    all_names.append(name)

for name in all_names:
    counts[name]     = all_names.count(name)
    
print(all_names)
print(counts)

max_name = list(counts.keys())[0]
max_count = counts.get(max_name)
print(max_count)
for item in counts.items():
    if item[1] > max_count:
        max_count = item[1]
        max_name = item[0]
        
print(max_name)