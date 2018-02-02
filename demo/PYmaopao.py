"""
冒泡
"""
mylist = [1, 21, 3, 6, 4, 10]
for i in range(0, len(mylist)):
    for j in range(0, len(mylist) - 1 - i):
        if mylist[j] > mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
for k in range(0, len(mylist)):
    print(mylist[k])
