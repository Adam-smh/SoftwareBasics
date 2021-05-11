string = input("Enter String")
c = input("Character")

count = 0

for i in string:
    if i == c:
        count += 1
    print(count, c)
