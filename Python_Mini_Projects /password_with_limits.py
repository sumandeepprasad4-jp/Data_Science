correct_password="deep"
print("You have maximum 3 attempts")
for n in range(1,4):
    user_password=input("Eneter the vlaue:")
    if correct_password==user_password:
        print("Correct password...")
        break
    else:
        print("Wrong password ! please try again..")
        n+=1
        if(n==4):
            print("You have reached your maxumum limit")