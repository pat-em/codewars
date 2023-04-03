numbers = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers.remove(0)
        numbers.append(0)
    
print(numbers)