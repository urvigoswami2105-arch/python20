number=input("enter 2 digit number")
number=int(number)

lastnum=number % 10
print(lastnum)

firstnum=number // 10
print(firstnum)

words=['zero','one','two','three','four','five','five','six','seven','eight','nine',]
print(words)

print(words[firstnum],words[lastnum])