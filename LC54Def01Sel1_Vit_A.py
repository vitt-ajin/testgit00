def login():
    userInput = input("User : ")
    passInput = input("Pass : ")
    if userInput == "admin" and passInput == "1234":
        ShowMenu()
        return True
    else:
        login()
        return False
def ShowMenu():
    print("-----iShop-----")
    print("1. Vat Calculate")
    print("2. Price Calculate")
    return menuSelect()
def menuSelect():
    userSelect=int(input(">> "))
    if userSelect==1:
        print(vatCalculate(int(input("Vat price : "))))
    elif userSelect == 2:
        print(priceCalculate())
    return 0

def vatCalculate(totalPrice):
   vat=7
   result=totalPrice+(totalPrice*vat/100)
   return result
def priceCalculate():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    return vatCalculate(price1 + price2)
login()