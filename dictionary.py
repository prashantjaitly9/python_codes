d={"name": "Prashant", "age": 22, "deptt": "MCA"}
print(d["deptt"])

books=[{"Title": "Harry Potter and the Philosopher's Stone", "Author": "JK Rowling", "Volume": 1}, 
       {"Title": "Harry Potter and the Chamber of Secrets", "Author": "JK Rowling", "Volume": 2},
       {"Title": "Harry Potter and the Prisoner of Azkaban", "Author": "JK Rowling", "Volume": 3},
       {"Title": "Harry Potter and the Goblet of Fire", "Author": "JK Rowling", "Volume": 4},
       {"Title": "Harry Potter and the Order of the Pheonix", "Author": "JK Rowling", "Volume": 5},
       {"Title": "Harry Potter and the Half Blood Prince", "Author": "JK Rowling", "Volume": 6},
       {"Title": "Harry Potter and the Deathly Hallows", "Author": "JK Rowling", "Volume": 7,"Volume":8},
       ]

for i in range(0, len(books)):
    print(books[i])
    if books[i]["Volume"]==7:
        books[i]["Author"]="Prashant"
print(books)

