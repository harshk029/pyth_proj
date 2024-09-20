'''
1 for rock
-1 for paper
0 for scissor '''

yourdict = {
    "r":1,"p":-1 ,"s":0
}
reversedict = {
    1:"rock",-1:"paper",0:"scissor"
    }
yourch = str(input("enter your choice:-"))
you = yourdict[yourch]

import random
computer = random.randint(-1,1)
print(f"computer chose:-{reversedict[computer]}")

if(computer == you):
    print("it's a draw")

else:
    if(computer == 1 and you == -1):
        print("you win")
    elif(computer == 1 and you == 0):
        print("you lose")
    
    elif(computer == -1 and you == 1):
        print("you lose")
    elif(computer == -1 and you == 0):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you win")
    elif(computer == 0 and you == -1):
        print("you lose")

    else:
        print("something went wrong")
