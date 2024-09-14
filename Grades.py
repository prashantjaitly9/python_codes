name=input("Enter your name: ")

grades={"Prashant" : {"Grade" : "A++", "Course": "MCA"},
        "Rishabh" : {"Grade" : "O", "Course" : "MCA"},
        "Salman" : {"Grade" : "D", "Course" : "MBA"}}
for i in grades:
    print(grades[i])
if name in grades:
    print(True)
else:
    print(False)