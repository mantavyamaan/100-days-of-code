import random 

print("Welcome to the rock, paper, and scissor game.")
choice=input("Enter rock, paper, or scissor\n").lower()
while choice!='rock' and choice!='paper' and choice!='scissor':
    choice=input("Enter Correct Choice\n")
if choice=='rock':
    a=0
elif choice=='paper':
    a=1
else:
    a=2
b=random.randint(0,2)
if b==0:
    print("Computer Chose: Rock")
elif b==1:
    print("Computer Chose: Paper")
else: 
    print("Computer Chose: Scissor")
if a==0 and b==1:
    print("You Lost")
elif a==0 and b==2:
    print("You Won")
elif a==1 and b==0:
    print("You Won")
elif a==1 and b==2:
    print("You Lost")
elif a==2 and b==0:
    print("You Lost")
elif a==2 and b==1:
    print("You Won")
else:
    print("Draw")
