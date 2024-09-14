# def pow(num, exp):
#     prod=1
#     for i in range(exp):
#         prod*=num
#     return prod

# n=int(input("Enter a number:"))
# e=int(input("Enter exponent:"))
# print(pow(n,e))

def recPow(a,n):#multiplication: 8 times, minimize using a temp variable

    if n==1:
        return a
    elif (n%2==0):
        return recPow(a,n/2)*recPow(a,n/2)
    else:
        return a*recPow(a,(n-1)/2)*recPow(a,(n-1)/2)
    
print(recPow(2,5))
