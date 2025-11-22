#Set:They are very helpful when you don't need to store the values in any specific order
# and when you only need to store unique values.

my_set={1,2,3,4,5}
my_set.add(6)

my_set.remove(6)
my_set.discard(6)

print(my_set)

print("-"*50,"\n")#-----------------------------------------------------

#methods that perform common mathematical set operations.

my_set={1,2,3,4,5,6,7}
your_set={1,2,3,4,5}

print("my_set is subset of your_set:",my_set.issubset(your_set))

print("my_set is superset of your_set:",my_set.issuperset(your_set))

your_set={4,9}

print("my_set is disjoint with your_set:",my_set.isdisjoint(your_set))


print(my_set|your_set)

my_set|=your_set

print("my_set|=your_set=",my_set)


my_set={1,2,3,4,5,6,7}


print(my_set&your_set)

my_set={1,2,3,4,5,6,7}
your_set={1,2,3,4,5}

print(my_set-your_set)

print(my_set^your_set)


print("-"*50,"\n")#-----------------------------------------------------