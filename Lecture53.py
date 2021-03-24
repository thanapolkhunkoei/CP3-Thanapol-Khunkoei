yourVat = int(input("yourPirce : "))
def vatCalculate(totalpirce):
    result = totalpirce+(totalpirce*7/100)
    return result
print(vatCalculate(yourVat))
