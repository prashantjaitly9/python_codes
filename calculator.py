ch=0

while(ch!=6):
    print("Welcone to the Calculator!")
    print("Choose any one of the given options")
    print("1: Addition \n2: Subtraction \n3:multipliation \n4:Division \n5:Modulus \n6:Exit")

    ch=int(input("Enter your choice: "))
    if ch==6:
        break
    
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))

    if ch==1:
        print("Sum=", num1+num2)
    elif ch==2:
        print("Difference=", num1-num2)
    elif ch==3:
        print("Product=", num1*num2)
    elif ch==4:
        print("Division=", num1/num2)
    elif ch==5:
        print("Modulus=", num1%num2)
    else:
        print("Wrong choice! Enter a listed number")

  