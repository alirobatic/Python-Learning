file = open("text","w")                                        #
file.write("ali")
file.close()

print("....................")
file_1 = open("text" , "r")
x = file_1.read()
print(x)
file_1.close()

print("....................")
file_2 = open("text" , "a")
x1 = file_2.write("behroz")
file_2.close()

print("....................")
#with open("text" , "w" ) as file:
    
print("....................")
name = input("your name =")
family = input("your family =")
with open("user" , "w")as file:
    file.write(name + "\n")
    file.write(family)
