num=int(input("Enter a number: "))
if num<2:
    print("Enter another number!")

isComp=False 
for i in range (2, int(num**(1/2))):
    if num%i==0:
        isComp=True
        break
if isComp:
    print("The number is composite")
else:
    print("The number is prime")