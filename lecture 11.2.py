number = int(input("Number >> "))
ii = 1
plus = 0
for i in range(number):
    text = ""
    for ii in range(i+1):
        text += "*"
    print(" "*(number-(i+1))+(text+"*"*plus))
    plus += 1
