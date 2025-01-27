print("Welcome to Number Guessing Game!")
print("I am thinking number between 1 and 100")
level=input("Choose a difficulty. Type 'easy' or 'hard'")
import random
n=random.randint(0,100)
if(level=="easy"):
    print("You have 10 attempts remaining to guess the number.")
    
    for i in range(1,11):
        guess=int(input("make a guess"))
        if(guess<n):
            print("Too low")
        elif(guess>n):
            print("Too high")
        else:
            print(f"You got it.The answer is {n}")
else:
    print("You have 5 remainings to guess the number")
    for i in range(1,6):
        guess=int(input("make a guess"))
        if(guess<n):
            print("Too low")
        elif(guess>n):
            print("Too high")
        else:
            print(f"You got it.The answer is {n}")
 

