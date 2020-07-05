Username = str(input("Username : "))
Password = int(input("Password : "))
if Username == "asd" and Password == 123:
    print("Welcome to GG store")
    print("-------Menu-------")
    print("1) Apple    10  THB")
    print("2) Banana   5   THB")
    print("3) Hotdog   20  THB")
    print("4) Sandwich  30  THB")
    print("5) Shoes    200 THB")
    Number = int(input("What Number do you want? : "))
    if Number == 1:
        print("Your Product : Apple")
        Amount = int(input("How many do you want : "))
        print("Total =",Amount*10)
    elif Number == 2:
        print("Your Product : Banana")
        Amount = int(input("How many do you want : "))
        print("Total =", Amount * 5)
    elif Number == 3:
        print("Your Product : Hotdog")
        Amount = int(input("How many do you want : "))
        print("Total =", Amount * 20)
    elif Number == 4:
        print("Your Product : Sandwich")
        Amount = int(input("How many do you want : "))
        print("Total =", Amount * 30)
    elif Number == 5:
        print("Your Product : Shoes")
        Amount = int(input("How many do you want : "))
        print("Total =", Amount * 200)
    else:
        print("Just press 1 to 5, Try again!!!")
    print("Thank you!!!")
else:
    print("Username or Password was wrong!!!")