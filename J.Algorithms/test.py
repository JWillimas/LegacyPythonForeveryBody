test=[5, 16, 99, 12, 567, 23, 15, 72, 3]
test[0],test[1]=test[1],test[0]
print(len(test))#9
for i in range(len(test)):#range(9)--->0-8(9nums)
    print(i)
print(test[0:8])
print(min(test))

test1="1234 5678 9012 3456"
print(list(test1))