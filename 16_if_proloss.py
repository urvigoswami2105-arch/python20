purchaseprice=int(input("ENTER PURCHASE AMOUNT :"))
sellingprice=int(input("ENTER SELLING AMOUNT :"))

difference=sellingprice - purchaseprice

if purchaseprice>sellingprice:
    print("LOSS IS :",difference)

if purchaseprice<sellingprice:
    print("PROFIT IS :",difference)

if purchaseprice==sellingprice:
    print("NO PROFIT NO LOSS")


