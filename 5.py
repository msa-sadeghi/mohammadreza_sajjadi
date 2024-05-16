# import random
# positions = []
# for i in range(100):
#     temp = []
#     for j in range(100):
#         x = random.randrange(10000)
#         temp.append(x)
#     positions.append(temp)
        

# def my_func(heights):
#     max_height = heights[0][0]
#     res = []
#     for i in range(len(heights)):
#         for j in range(len(heights[i])):
#             if heights[i][j] > max_height:
#                 max_height = heights[i][j]
#                 res = [i,j]
#     if len(res) == 0:
#         res = [0,0]
#     return res

# print(my_func(positions))
                
    

# def reverse_str(string):
#     return string[::-1]

# print(reverse_str("tiyam"))

# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[0:3])
# print(numbers[:3])
# print(numbers[6:9])
# print(numbers[6:])
# print(numbers[-3:])
# print(numbers[8::-1])

# string = "ali"
# print(string[:2])
# print(string[1:])
# print(string[::-1])

# def reverse_str(string):
#     res = []
#     for s in string:
#         res.insert(0,s)
#     # r = ""
#     # for i in res:
#     #     r += i
#     # return r
#     return "".join(res)

# print(reverse_str("nikan"))


# list1 = [1,2,3,4,5]
# list2 = [2,3,4,5,6]

# def my_sort(l1, l2):
#     l = l1 + l2
#     l.sort()
#     return l

# print(my_sort(list1, list2))


# def my_sort(l1, l2):
#     l  = l1 + l2
#     for i in range(len(l)):
#         for j in range(i + 1, len(l)):
#             if l[i] > l [j]:
#                 l[i],l[j] = l[j] , l[i]
                
#     return l
# print(my_sort(list1, list2))
        
        
dis ={}
min_dist, max_dist = (0,0)
min_city, max_city = ("", "")
for i in range(3):
    name = input("enter city name: ")
    dist = int(input("enter the distance: "))
    dis[name] = dist
    if i == 0:
        min_city, max_city = (name, name)
        min_dist, max_dist = (dist, dist)
    if dist < min_dist:
        min_dist = dist
        min_city = name
    if dist > max_dist:
        max_dist = dist
        max_city = name
        
print(max_city, min_city)