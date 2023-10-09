numbers = [1, 2, 3, 4, 5, 6]

temp = numbers[0]
numbers[0] = numbers[1]
numbers[1] = temp

temp2 = numbers[4]
numbers[4] = numbers[5]
numbers[5] = temp2

print(numbers)

i = 5

while i == 5:
    print("That just my baby doge.")