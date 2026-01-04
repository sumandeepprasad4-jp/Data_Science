try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print("what kind of operation do you want to perform. press + for addition \n press - for subtraction \n press / for division \n press * for multiplication")
    o=input("enter your operation:")
    match o:
        case "+":
            print(f"The reslt is :{a+b}")
        case "-":
            print(f"The reslt is :{a-b}")
        case "/":
            print(f"The reslt is :{a/b}")
        case "*":
            print(f"The reslt is :{a*b}")
        case default:
            print(f"There was an error")

except Exception as e:
    print(f"Error ocure:{e}")

