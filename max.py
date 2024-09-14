def maximum(list):

    max=list[0]
    min=list[0]
    for i in range(1, len(list)):
        if (list[i]>max):
            max=list[i]
        elif (list[i]<min):
            min=list[i]

    return max,min

list=[1,2,3,4,5,6]
print(maximum(list))
