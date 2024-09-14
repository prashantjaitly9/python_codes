# my_tuple = (10,20,30)
# x = my_tuple[0]
# y = my_tuple[1]
# z = my_tuple[2]

# print(x)
# print(y)
# print(z)

# my_list = [1,2,3,4]
# my_list.append(5)
# print(my_list)

# first_name = "Prashant"
# last_name = "Jaitly"
# full_name = first_name + " " + last_name
# print(full_name)

# dict = {"name": "Alice", "age" : 20, "grade" : "A"}
# print(dict)
# dict["grade"] = "A+"
# print(dict)

# my_set = {1,2,3,4}
# my_set.add(5)
# print(my_set)

# age = 25
# convert_age = str(age)
# print(convert_age, "years old")

# a = True
# b = False
# c = a and b
# print(c)

# numbers = [10,20,30,40,50]
# for i in range (0,3):
#     print (numbers[i])

# a = int(input("Enter first numer: "))
# b = int(input("Enter second numer: "))

# sum = a+b
# diff = a-b
# prod = a*b
# div = a/b
# mod = a%b

# print(sum, diff, prod, div, mod)

# if (a>b):
#     print(f"The number {a} is greater than {b}")
# elif(a==b):
#     print(f"The number {a} is equal to {b}")
# else: 
#     print(f"The number {a} is smaller than {b}")

# num1 = 10
# num2 = 20
# num1+=num2
# print(num1)
# num1-=num2
# print(num1)
# num1*=num2
# print(num1)
# num1/=num2
# print(num1)

# bool1 = bool(input("Enter a boolean value: "))
# bool2 = bool(input("Enter another boolean value: "))
# print(bool1 and bool2)
# print(bool1 or bool2)
# print(not bool1)
# print(not bool2)

# x1 = 5
# x2 = 6
# print(x1&x2)
# print(x1|x2)
# print(x1^x2)
# print(~x2)
# print(x1<<x2)
# print(x1>>x2)

# list = ["Prashant", "is", "a", "good", "boy"]
# if "Prashant" in list:
#     print("Prashant is present!")
# else:
#     print("Prashant is absent!")

# p = 10
# q = 7
# print(p//q+10/20*q-q%p*5-3)

# p1 = 50
# p2 = 70
# p3 = f"{p1} is max" if p1>p2 else ("Both are equal" if p1==p2 else f"{p2} is max")
# print(p3)

# str1 = "Prashant"
# str2 = "Prashant"
# print(str1 is str2)
# print(str1 is not str2)





# #number pattern
# rows=int(input("Enter the number of rows: "))
# for i in range (1,rows+1):
#     for k in range(1,rows-i+1):
#         print(" ", end="")
#     for j in range(1,i+1):
#         print(j, end="")
#         if (j==i):
#             while (j!=1):
#                 print(j-1, end="")
#                 j=j-1
                
#     print()




# #inverted pyramid
# rows=int(input("Enter the number of rows: "))
# for i in range (rows, 0, -1):
#     for j in range (rows, i, -1):
#         print(" ", end="")
#     for j in range(i, 0, -1):
#         print("*", end="")
    
#     print()




# # String reverse:
# str=input("Enter a string: ")
# s=""
# i=len(str)-1
# while (i!=-1):
#     s=s+str[i]
#     i=i-1
# print("The reversed string is:", s)




# # String reverse:
# str=input("Enter a string: ")
# s=""
# i=len(str)-1
# while (i!=-1):
#     s=s+str[i]
#     i=i-1
# print("The reversed string is:", s)



# # Multiplication Table:
# a=int(input("Enter the number: "))
# for i in range (1,11):
#     print(f"{a}*{i}={a*i}")


# # Matrix add:
# rows=int(input("Enterv the numebr of rows: "))
# col=int(input("Enter the number of columns: "))
# mat1=[]
# mat2=[]

# res = [[0 for i in range(col)] for j in range(rows)]

# print("Enter values for Matrix1: ")
# for i in range (0, rows):
#     a=[]
#     for j in range (0, col):
#         a.append(int(input()))
#     mat1.append(a)

# print("The entered Matrix 1 is: ", mat1)

# print("Enter values for Matrix2: ")
# for i in range (0, rows):
#     a=[]
#     for j in range (0, col):
#         a.append(int(input()))
#     mat2.append(a)

# print("The entered Matrix 2 is:", mat2)

# for i in range (rows):
#     for j in range (col):
#         res[i][j]=mat1[i][j]+mat2[i][j]

# print(f"The sum of Matrix 1: {mat1} and Matrix 2: {mat2} is: {res}")




# Q.29 Write a Python program that prints the first 10 Fibonacci numbers in a 2x5 grid using nested loops.

# def fib(a):
#     if a<=2:
#         return 1
#     return fib(a-1)+fib(a-2)

# # x=int(input("Enter the length of Fibonacci sequence: "))
# print("The fibonacci sequence in a 2x5 grid form: ")
# for i in range(1,11):
#     if (i%2==0):
#         print("\t", fib(i))
#     else:
#         print(f"{fib(i)}", end="")

    
# 30.   Write a Python program to print the following character pattern using nested loops:
# A
# AB
# ABC
# ABCD

# val = 65
# row = int(input("Enter the number of rows: "))
# for i in range (0,row):
#     for j in range(0,i+1):
#         print(chr(val+j), end="")
#     print()
    
        
# Q31. Input a list of 10 numbers from the user and sort them in ascending order using the Selection sort

lst = []
for i in range(0,10):
    if (i==0):
        lst[i]=int(input("Enter the first number:"))
    elif(i==1):
        lst[i]=int(input("Enter the second number:"))
    else:
        lst[i]=int(input(f"Enter the {i+1}th number:"))

print("Given Unsorted list:")
print(lst)

for i in range (len(lst)-1):
    min = i
    for j in range (i+1, len(lst)):
        if lst[min]>lst[j]:
            min=j

    lst[i], lst[min] = lst[min], lst[i]

print("Sorted Array: ")
print(lst)

