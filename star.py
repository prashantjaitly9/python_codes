rows = int(input("Enter the number of rows: "))
for i in range (0,rows+1):
    sum = ""
    for j in range (0,i):
        sum = sum + "*"
        print(sum)
    print(" ")