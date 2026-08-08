a = {"ali" , 21 , "reza"}                          #set
print(type(a))

print(".................................")

a.add(30)                                          #Add a member
print(a)

print(".................................")

a.update([35,"amir"])                             #Adding more than one member 
print(a)

print(".................................")

print(35 in a)                                    #Does this member exist in this set?

print(".................................")
print(".................................")


my_list = {1 , 3 , 5 , 7 }
my_list1 = {2 , 4 , 6 , 8 }
print(my_list.union(my_list1))                    #The union of two sets

print("........")

my_list2 = {1, 9 , 8 , 5}
r = my_list.intersection(my_list2)                #Intersection of two sets
print(r)

print(".........")

my_list4 = {2, 2 , 4 ,6}                          # show that duplicates have been removed
print(my_list4)

print(".........")

r1 = my_list.issubset(my_list1)                   #Subset
print(r1)

print(".........")                                #metod 
my_list.remove(1)
print(my_list)
my_list.discard(1)
print(my_list)
