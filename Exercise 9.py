Username = "asa"
Password = 111
Count = 0

while (Username != "admin" or Password != 123) and Count < 3:
    Username = str(input("Input your Username : "))
    Password = int(input("Input your Password : "))
    if Username == "admin" and Password == 123:
        print("Welcome to Window!!!")
    else:
        print("Username or Password had wrong, Please try again!!!")
    Count +=1
if Count == 3:
    print("Your PC had been locked, See you next time!!!")
