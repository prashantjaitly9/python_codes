def fact(i):
    if i==1 or i==0:
        return 1
    elif i<0:
        return -1
    return i*fact(i-1)

a=int(input("Enter a number: "))

x=fact(a)
if x==-1:
    print("Enter a positive number!")
else:
    print(x)