for i in range(1,6): #iterators, the value of i in for loop doesn't vary with inside block
    print(i)
    if (i%2):
        i=i+100
        print(i)
        continue
    print ("Hello")