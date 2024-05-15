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

# f = {}
# for i in range(3):
#     name = input("enter a name: ")
#     sport = input("enter a sport: ")
#     f[name] = sport

# print(f['a'])

# name_count = {}
# for i in range(5):
#     name = input("enter a name: ")
#     if name not in name_count:
#         name_count[name] = 1
#     else:
#         name_count[name] += 1
# print(name_count)


# def find_max(info)    :
#     keys = list(info.keys())
#     res = keys[0]
#     m = info[res]
#     for item in info.items():
#         if item[1] > m:
#             m = item[1]
#             res = item[0]
#     return res 
# print(find_max(name_count))



# persons = {
#     "ali":2,
#     "roze":1,
#     "martin":5,
#     "sara":3,
#     "mina":2,
# }

# for i, j in persons.items():
#     print(i,j)

# all_trans = [100, -50, 300, -200]
all_trans = []
while True:
    t = float(input("enter transaction amount: "))
    all_trans.append(t)
    if input("> if you want to quit enter 0 ") == "0":
        break
    

total = 0
max_total = 0
def func(x):
    global total, max_total
    for n in x :
            total += n
            if total > max_total:
                max_total = total
    return max_total
print(func(all_trans))