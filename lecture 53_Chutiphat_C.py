def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

x = int(input("Number : "))
print(vatCalculate(x))