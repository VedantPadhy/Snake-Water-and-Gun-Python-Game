'''
1 for snake 
-1 for water
0 for gun
'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice (snake, water, gun): ")
youdict={"snake":1, "water":-1, "gun":0}
you = youdict[youstr]
reversedict={1:"snake",-1:"water",0 :"gun"}
print(f"you chose:{dict[you]}")
print(f"computer chose: {dict[computer]}")
if (computer==-1 and you==1):
    print("You win!")
elif (computer==-1 and you==0):
    print("You lose!")
elif (computer==-1 and you==-1):
    print("It's a tie!")
elif (computer==0 and you==-1):
    print("You win!")
elif (computer==0 and you==1):
    print("You lose!")
elif (computer==0 and you==0):
    print("It's a tie!")
elif(computer==1 and you==0):
    print("You win!")
elif(computer==1 and you==-1):
    print("You lose!")
elif(computer==1 and you==1):
    print("It's a tie!")
else:
    print("Invalid Input")
