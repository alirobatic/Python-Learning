my_dic = {"name" : [ "alireza" , "amir" , "mohammad"], "family" : "askary" , "age" :[ 27 , 23 ,30] ,"from" : "shahrebabak"}
print(my_dic["name"][1] , my_dic["age"][2])      #Calling

print(".................................................")

my_dic["family"] = "amiri"                     #changing a variable in a dictionary
print(my_dic)                                   

print(".................................................")

my_dic ["height"] = 178                        #add key in dictioary
print(my_dic)

print(".................................................")

print(my_dic.keys())                           #calling the key

print(".................................................")

print(my_dic.values())                         #calling the variable

print(".................................................")

print(len(my_dic))                             #Dictionary length

print(".................................................")

my_dic1 =  {"apple" : 2000 , "banana" : 4000 , "melon" : 3000}             #practice

my_dic1["apple"] = 2500
my_dic1["pistachio"] = 6000
print(my_dic1)
print(my_dic1.get("melon"))

print(".................................................")

n = input("name =")                                                        #practice
f = input("family=")
a = int(input("age="))
information = {"name": n ,
 "family": f ,
 "age":a       
    }
print(information)