# in python variables can store multiple type of things
# name = "Abhi"
# print(name)
# name = 234
# print(name)

my_list = [1, 2, 3, "Abhi"]
print(my_list)

'''
indexing
'''
print(my_list[0]) # first element
print(my_list[3])# last elementś
print(my_list[-4]) # first element
print(my_list[-1])# last elementś
# if index > 3 and index < -4 then error is thrown

'''
Slicing
'''
print(my_list[1:4])
print(my_list[::-1]) # to get number in reverse order


del my_list[0]
print(my_list)

'''
list comprehension
'''
# a = [1,2,3,4,5,6,7,8,9]

a = [x for x in range(10) if x%2==0]
print(a)

b = [3**x for x in range(5)]
print(b)

'''
list method
'''
my_list.append("Gautam")
print(my_list)

my_list.insert(1, 2.3)
print(my_list)

# my_list.sort()
# print(my_list)

# pop(index) to pop that element from that index
# clear() to clear whole list
# reverse() to reverse list
# index to get index of element
# count to check count of element in list

'''
list function
'''
print(len(my_list)) # to get length of list
print(max(my_list)) # to get max element from list
# to get minium use min() function
# to get a paticular sequence converted into list use list() function
# to get sum of all num in list 


