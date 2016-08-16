number = [3, 1, 4, 1, 5, 9, 2]

#1. Change the first element of numbers to "ten"

number[0] = "ten"

#2. Change the last element of numbers to 1

number[len(number)-1] = 1

#3.Get all the element from numbers except the first two

for x in range(2, len(number)):
    print(number[x])

#4.Check if 9 is an element of numbers

if 9 in number:
    print("Yes")
else:
    print("No")

