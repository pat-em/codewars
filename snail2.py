def snail(array):
    # Initialize empty result list
    result = []
    
    # Loop until all elements have been processed
    while len(array) > 0:
        # Add the top row to the result list
        result += array.pop(0)

        # Add the rightmost column to the result list
        for row in array:
            result.append(row.pop())

        # Add the bottom row in reverse order to the result list
        if array:
            result += array.pop()[::-1]

        # Add the leftmost column in reverse order to the result list
        for row in reversed(array):
            result.append(row.pop(0))

    # Return the result list
    return result

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print ("REVERSED ARRAY", list(reversed(array)))

print(snail(array))