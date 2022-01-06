import random
print("**********DICE ROLL**********")
try:
    while(True):
        a=int(input("enter 1 for Roll the Dice or enter 0 for Quite : "))
        if (a==1):
            number=random.randint(1,6)
            print(number)
        elif(a==0):
            print("you quite the game")
            exit()
        elif((a==0) or (a==1) != a):
            print("select correct input!!!!")
except:
    print("enter valid input")


    
