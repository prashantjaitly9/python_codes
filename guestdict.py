dict = {"Prashant":"20/07/1998", "Praveen": "26/10/2004"}
name=input("Enter your name: ")
print(dict.get(name))

for i in dict.keys():
    if i==name:
        print(i)
    