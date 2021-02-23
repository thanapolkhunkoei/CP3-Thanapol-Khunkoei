# Purchase
username = input("username : ")
password = input("password : ")
apple = 100
banana = 80
orange = 70
papaya = 20
if username == "admingolf" and password == "1234":
    print("Welcome to our Shop")
    print("----Gofu Shop----")
    print("1.Apple      : 100 TB/Unit")
    print("2.Banana     :  80 TB/unit")
    print("3.Orange     :  70 TB/unit")
    print("4.Papaya     :  20 TB/unit")
    item = input("Select number of item : ")
    amount = int(input("Amount : "))
    if item  == "1":
        print("total :", apple*amount)
    elif item  == "2":
        print("total :", banana*amount)
    elif item  == "3":
        print("total :", orange*amount)
    elif item  == "4":
        print("total :", papaya*amount)
else:
    print("usename or password incorrect !!")
