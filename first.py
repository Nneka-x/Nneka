# print("Hello World")

# x=5
# y="hello world" 
# print (x) 
# print (y) 

# for x in range(0, 101, 2):
#  print(x) 

# import random

# print(random.randrange(1,10))

# a = "mango","banana","cherry"
# print(a[0])   


# a = "Nneka Nwanze"
# print(len(a))

# b  = "hello world"
# print(b[2:5])

# n = "thewisdom machine"
# print(n[1:])

# txt = "the best things in life are free"
# print("free" in txt)


# txt = "the best things in life are free"
# if "free" in txt:
#   print("yes,  why not")

# b = "Thewisdom machine"
# print(b[-5:-2])

# a = "Thewisdom machine"
# print(a.upper())

# a = "Thewisdom machine"
# print(a.lower())

# a = " Thewisdom machine"
# print(a.strip())   

# a = "Hello, world"
# print(a.replace("H" , "J"))

# a = "Hello, World"
# print(a.split(","))

# a = "hello"
# b = "World"
# c = a + b
# print(c)

# a = "hello"
# b = "World"
# c = a + " " + b
# print(c)

# for x in "cherry":
#   print (x)


# age = 22
# txt = "My name is Nneka, I am" + age  
# txt = "My name is Nneka, and I am {} "
# print(txt.format(age))


# quantity = 3
# itemno = 567
# price = 49.95
# txt = "I want {} quantites of deio and {} items of mio with a price of {}"
# print(txt.format(quantity,itemno,price))

# txt = "I want {0} quantites of deio and {2} items of mio with a price of {1}"
# print(txt.format(quantity,itemno,price))


# txt = "Hello, welcome to my world"
# x = txt.endswith("my world")
# print (x)

# x = "Hello world"
# print(len(x))

# a = 50
# b = 5

# thislist = ["apple","banana","cherry"]
# print(thislist[1])

# thislist = ["apple","banana","cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)


# numbers_x = [10, 20, 30, 40, 10]
# if numbers_x [0]== numbers_x [-1] :
#   print("good")
# else  :
#   print("bad")

# numbers_x = [10, 20, 30, 40, 10]
# first_num = numbers_x[0]
# last_num = numbers_x [-1]
# if first_num == last_num:
#     #  return True
#     print("yes")
# else:
#     # return False
#     print("No")

# thislist = ["apple","banana","cherry"]
# thislist.remove("cherry")
# print(thislist)

# thislist = ["apple","banana","cherry"]
# thislist.pop(1)
# thislist.clear()
# print(thislist)

# thislist = ["apple","banana","cherry","watermelon"]
# for x in thislist :
#   print(x)
# for i in range(len(thislist)) :
#   print(thislist[i])

# thislist = [100,50,65,82,23]
# thislist.sort()
# thislist.sort(reverse = True)
# print(thislist)


# thislist = "1234abcd"
# print(thislist[::-1])


# x = ('apple', 'banana','cherry')
# y = list(x)
# y[1] = 'kiwi'
# x = tuple(y)
# print(type(x))

# thistuple = ("apple","kiwi","cherry")
# print(thistuple)

# thistuple = ("apple",10,6.5,"kiwi")
# print(thistuple)

# thistuple = (10,3,500,67,82)
# print(thistuple[2])


# thistuple = ("apple","kiwi","watermelon","cherry")
# y = list(thistuple)
# print(y)
# nn1 = thistuple[0]
# nn2 = thistuple[1]
# nn3 = thistuple[2]
# nn4 = thistuple[3]
# print(nn1,nn2,nn3,nn4)

# thisset = {"apple","banana","cherry"}
# thisset.discard("kiwi")
# thisset.remove("kiwi")

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# thisset = {"apple","kiwi","cherry"}
# print(thisset)

# thisset = {"apple","kiwi","cherry"}
# mylist = ["google","banana","android"]
# thisset.add("google")
# print(thisset)

# thisset = {"apple","kiwi","cherry"}
# if "cherry" in thisset :
#     thisset.remove("cherry")
#     print(thisset)

# thisset = {"apple","kiwi","cherry"}
# myset = {"apple","google","android","cherry"}
# thisset.symmetric_difference_update(myset)
# print(thisset)

# a = 790
# b = 200
# if b > a :
#     print("b is greater than a")
# elif b == a : 
#     print("your dad's a hoe")
# else :
#     print("you are dumb")

# i = 1
# while i < 15 :
#     print(i)
#     if i == 14 :
#     #   break
#       continue 
#     i += 1


# firstval = input("enter : ")
# firstval = int(firstval)
# sign = input("operator : ")
# secondval = input("enter : ")
# secondval = int(secondval)
# error = "invalid"
# if sign == "+"  :
#     print (firstval + secondval)
# elif sign == "-" :
#     print(firstval - secondval)
# elif sign == "*" :
#     print(firstval * secondval)
# elif sign == "/" :    
#     print(firstval / secondval)
# elif sign != "+,-,*,/" :
#     print(error)


# P = input("enter: ")
# P = int(P)
# cal = input("op : ")
# T = input("enter : ")
# T = int(T)
# cal = input("op : ")
# R = input("enter : ")
# R = int(R)
# r = input("enter : ")
# r = int(r)
# t = input("enter : ")
# t = int(t)
# CI = P*(1+r/100)(t-1)
# # SI = (P*T*R)/100
# # print (SI)
# print(CI)

# from random import randint

# #list of choice options
# t = ["Rock", "Paper", "Scissors"]

# #random choice for computer
# comp_choice = t[randint(0,2)]

# player_choice = 1
# computer_win=0
# player_win=0

# while player_choice == 1:
# #player choses its option
#     player_choice = input("Rock, Paper, Scissors?")
#     comp_choice = t[randint(0,2)]
#     if player_choice == comp_choice:
#         print("Tie!")
#         print("Score")
#         print("computer win:",computer_win)
#         print("player win:",player_win)
#     elif player_choice == "Rock":
#         if comp_choice == "Paper":
#             print("You lose! computer chose", comp_choice, "player chose", player_choice)
#             computer_win+=1
#             print("Score")
#             print("computer win:",computer_win)
#             print("player win:",player_win)
             
#         else:
#             print("You win! player chose", player_choice, "computer chose", comp_choice)
#             player_win+=1
#             print("Score")
#             print("computer win:",computer_win)
#             print("player win:",player_win)
#     elif player_choice == "Paper":
#         if comp_choice == "Scissors":
#             print("You lose! computer chose", comp_choice, "player chose", player_choice)
#             computer_win+=1
#             print("Score")
#             print("computer win:",computer_win)
#             print("player win:",player_win)
#         else:
#             print("You win! player chose", player_choice, "computer chose", comp_choice)
#             player_win+=1
#             print("Score")
#             print("computer win:",computer_win)
#             print("player win:",player_win)
#     elif player_choice == "Scissors":
#         if comp_choice == "Rock":
#             print("You lose computer chose", comp_choice, "player chose", player_choice)
#             computer_win+=1
#             print("Score")
#             print("computer win:",computer_win)
#             print("player win:",player_win)
#         else:
#             print("You win! player chose", player_choice, "computer chose", comp_choice)
#             player_win+=1
#             print("Score")
#             print("computer win:",computer_win)
#             print("player win:",player_win)
#     else:
#         print("That's not a valid play.")


