def fib(a):
    if a<=2:
        return 1
    return fib(a-1)+fib(a-2)

x=int(input("Enter the length of Fibonacci sequence: "))

for i in range(1,x+1):
    print(fib(i))
        
    