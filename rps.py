import random

USER_SCORE = 0
COMPUTER_SCORE = 0



k=int(input())
for i in range(0, k):
    print("ROCK=1 , PAPER=2 , SCISSOR=3")
    a=int(input())
    b=random.randint(1,4)
    if (a == 1 and b == 1):
        print(b)
        print("it's a tie")
    elif (a == 1 and b == 2):
        print(b)
        print("computer wins")
        COMPUTER_SCORE+=10
    elif (a == 1 and b == 3):
        print(b)
        print("user wins")
        USER_SCORE+=10
    elif (a == 2 and b == 1):
        print(b)
        print("user wins")
        USER_SCORE+=10
    elif (a == 2 and b == 2):
        print(b)
        print("it's a tie")
    elif (a == 2 and b == 3):
        print(b)
        print("computer wins")
        COMPUTER_SCORE+=10
    elif (a == 3 and b == 1):
        print(b)
        print("computer wins")
        COMPUTER_SCORE+=10
    elif (a == 3 and b == 2):
        print(b)
        print("user wins")
        USER_SCORE+=10
    elif (a == 3 and b == 3):
        print(b)
        print("it's a tie")




print("USER_SCORE : " + str(USER_SCORE))
print("COMPUTER_SCORE : " + str(COMPUTER_SCORE))





if (USER_SCORE>COMPUTER_SCORE):
    print("YOU WIN")
elif (USER_SCORE==COMPUTER_SCORE):
    print("IT'S A TIE")
else :
    print("YOU LOST")
hey
