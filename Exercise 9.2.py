CountNumber = 0
UserID = "xxx"
Password = 000

while CountNumber < 3:
    UserID = str(input("Your UserID >> "))
    Password = int(input("Your Password >> "))
    if UserID == "admin" and Password == 123:
        print("Welcome to Window 9_2 !!!")
        CountNumber = 100
    else:
        print("UserID or Password isn't correct!!!")
    CountNumber += 1
if CountNumber == 3:
    print("Computer had been locked!!!")