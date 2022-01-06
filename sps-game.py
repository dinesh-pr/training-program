import random
def sps_game():
        n=0
        u=0
        while(n<=5):   
            s=random.choice(['stone','paper','sissor'])  
            a=input("enter your choice from these: Stone , Paper ,Sissor :")
            f=open('sps-game.txt','a')
            if((a == 'stone') or (a== 'paper') or (a== 'sissor')):
                if(a=='stone' and s=="sissor"):
                    print("YOU WIN !!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: you win \n ")
                    f.close()
                    u+=1
                elif(a=='paper' and s=="stone"):
                    print("YOU WIN !!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: you win \n ")
                    f.close()
                    u+=1
                elif(a=='sissor' and s=="paper"):
                    print("YOU WIN !!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: you win \n ")
                    f.close()
                    u+=1
                elif(s=='stone' and a=='sissor'):
                    print("you fail!!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: computer win \n ")
                    f.close()
                elif(s=='paper' and a=='stone'):
                    print("you fail!!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: computer win \n ")
                    f.close()
                elif(s=='sissor' and a=='paper'):
                    print("you fail!!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: computer win \n ")
                    f.close()
                elif(a==s):
                    print("round is tie")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: Tie \n ")
                    f.close()
                n+=1
            else:
                print("check input")
        print(f"you win {u} times")
sps_game()
