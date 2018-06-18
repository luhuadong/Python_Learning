# 九九乘法表

'''
 For in 方法
'''

print("")
print("#"*72)
print("\t\t\t\t[for in]")

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
    print("")

print("-"*72)

for i in range(9, 0, -1):
    for j in range(1, i+1):
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
    print("")

print("="*72)

for i in range(1, 10):
    print(" "*8*(9-i), end="")
    for j in range(i, 0, -1):
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
    print("")

print("-"*72)

for i in range(9, 0, -1):
    print(" "*8*(9-i), end="")
    for j in range(i, 0, -1):
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
    print("")

'''
 While 方法
'''
print("")
print("#"*72)
print("\t\t\t\t[while]")

i=1
while i<10:
    j=1
    while j<i+1:
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
        j=j+1
    i=i+1
    print("")

print("-"*72)

i=9
while i>0:
    j=1
    while j<i+1:
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
        j=j+1
    i=i-1
    print("")

print("="*72)

i=1
while i<10:
    j=i
    print(" "*8*(9-i), end="")
    while j>0:
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
        j=j-1
    i=i+1
    print("")

print("-"*72)

i=9
while i>0:
    j=i
    print(" "*8*(9-i), end="")
    while j>0:
        print("{}*{}={:<3}".format(j,i,i*j), end=" ")
        j=j-1
    i=i-1
    print("")

print("")
 
