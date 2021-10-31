'''
For loop
'''

for x in range(10):
    print(2*x, end=' ') # to print without line break
print(end='\n\n')

a = ['Abhi', 'Nand', 'Adi']

for name in a:
    print(name*2)
print()


'''
while loop
'''

n = 5

while n>=0:
    print(n, end=' ')
    n -= 1
print(end='\n\n')


'''
break and continue
'''

for i in range(10):
    if i>6:
        print(i)
        break
    else:
        print(i,end=' ')
        continue

