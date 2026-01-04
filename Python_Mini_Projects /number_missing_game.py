import random
print("Welcome to the number guessing game")
print("The secret number is between 1 and 50")
n=10
is_guess=False
random_no=random.randint(1,50)
for i in range(0,n):
    print(f"you have {n-i} attempts left")
    user_input=int(input("Enter your guess:"))
    if  random_no<user_input<=50:
        print("your guess is wrong! Try lower")
    elif 0<=user_input<random_no:
        print("Youe guess is wrong! higher")
    elif user_input>50 or user_input<0:
        print("invalid number! choose between 1-50")
    else:
        print("Congrats your guess is correct!")
        is_guess=True
        break
if is_guess==False:
    print("Bad luck! you exhausted all your attemps")
print(f"The number is {random_no}. Game over!!!")





''''
# we can use a loop like this also coth are correct 

    if user_number == secret_number:
        print("Congrats, your guess is correct!")
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Your guess is wrong! Try {higher_or_lower} number.")
    num += 1
    attempts -= 1
'''