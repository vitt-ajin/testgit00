userInput=input("User : ")
passInput=input("Pass : ")
if userInput=="admin"and passInput=="1234":
    print("Done !")
    print("-----iShop-----")
    print("1. Vat Cal")
    print("2. Price Cal")
    userSelect=int(input(">> "))
    if userSelect==1:
        price=int(input("Price :"))
        vat=7
        result=price+(price*vat/100)
        print(result)
    elif userSelect==2:
        price1=int(input("First PP: "))
        price2=int(input("Second PP: "))
        print(price1+price2)