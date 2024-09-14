a=int(input("Enter a 2-digit number: "))
o=a%10
t=(a-o)/10

o1=o
t1=t

o=o+t
t=o-t
o=o-t

if (o1==o and t1==t):
    print ("Palindrome")
else:
    print ("Not palindrome")
