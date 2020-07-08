number = int(input("Number >> " ))
plus = 0
for i in range(number):
    print(" "*(number-(i+1)),"*"*(i+1)+(plus*"*"))
    plus += 1