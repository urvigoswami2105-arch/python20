p1=int(input("ENTER FIRST PRODUCT PRICE :"))
w1=int(input("ENTER FIRST PRODUCT WEIGHT :"))

p2=int(input("ENTER SECOND PRODUCT PRICE :"))
w2=int(input("ENTER SECOND PRODUCT WEIGHT :"))

price_per_gm = p1 / w1
price_per_gm2= p2 / w2

if price_per_gm<price_per_gm2:
    print("FIRST PRODUCT IS CHEAPER")
else: 
    print("SECOND PRODUCT IS CHEAPER")