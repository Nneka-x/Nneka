
import random
 
gameList =["rock","scissors","paper"]
userchoice =str(input("enter a value from the list: "))
comchoice = random.choice(gameList)
if userchoice  in gameList:
    print("working")
else:
    print("invalid value")
if userchoice =="rock"  and comchoice =="scissors":
    print("rock X scissors !!! i win")
elif userchoice =="paper" and comchoice =="rock":
    print("paper X rock so i win")
elif userchoice =="scissors" and comchoice =="paper":
    print("scissors X paper so i win ")
elif  comchoice =="rock" and userchoice =="scissors":
    print("rock beats scissor so computer wins")
elif comchoice =="paper" and userchoice =="rock":
    print("paper beats rock so computer wins")
elif  comchoice =="scissors" and userchoice =="paper":
    print("scissors beats paper so computer win")