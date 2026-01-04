import random
print("Welcome to the game of roll and dice")
#print()
while True:
    choice=input("Press 'space' to roll a die or 'q' to quit the game ")
    # if you want to remove the spaces before and after the word then use the strip().
    # choice=choice.strip()
    if choice=="q":
        print("Thanks for playing the game, Bye")
        break
    elif choice=="":
        number=random.randint(1,6)
        print(f"Your number is {number}")
    else:
        print("invalid input")
