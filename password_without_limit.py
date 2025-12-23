acutal_password="deep"
while True:
    user=input("Enter your password:")
    if(user==acutal_password):
        print("Correct password")
        break
    print("wrong password! please try again")