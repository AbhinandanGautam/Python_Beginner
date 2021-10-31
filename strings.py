name = 'Abhinandan'
print(name)

'''
indexing
'''
print(name[0]) # first character
print(name[-10]) # first character
print(name[9]) # last character 
print(name[-1]) # last character

'''
Slicing 
'''
print(name[:5])
print(name[1:5])
print(name[5:])
print(name[1:7:2])
print(name[::-1]) # print string in reverse order


a = "abhi"
b = "nand"
print(a+b)
print(a*3)

str = "Hello world"
for i in str:
    print(i,end=' ')
print()

'''
some functions
'''
password = "123"

# isalpha()
print(password.isalpha())

# isdigit()
print(password.isdigit())

# islower to check all characters are lowercase or not
# isupper to check all characters are uppercase or not
# lower to convert all uppercase to lowercase
# upper to convert all lowercase to uppercase

# sname = "Gautam"
# print(sname)

# para = '''Hello
# Welcome,
# To Nand's PC
# We are doing python programming'''
# print(para)

# paragraph = """Python is most useful language in 2021
# It is use for various purposes : 
# 1. Data Science
# 2. Machine Learning
# 3. Artifical Intelligence
# 4. Backend"""
# print(paragraph)