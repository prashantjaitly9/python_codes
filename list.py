l1=[4,5,6,1,2,3]
even=[]
odd=[]
name="Prashant"
m=max(l1)
n=min(l1)
print(m,n)

for i in range (0,len(l1)):
    if (l1[i]%2==0):
        even.append(l1[i])
    else:
        odd.append(l1[i])

print(even, odd)

list=['a','b','c','d','e']
vowel=[]
cons=[]
for i in range (0,len(list)):
    if (list[i]=='a'or list[i]=='e' or list[i]=='i' or list[i]=='o' or list[i]=='u'):
        vowel.append(list[i])
    else:
        cons.append(list[i])

print(vowel, cons)

list.remove('a')
print(list)
list.pop(2)
print(list)
l1.sort()
print(l1)
l1.insert(1,20)
print(l1)

