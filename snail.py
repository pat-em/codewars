def snail(array):

    lst = []

    while len(array) > 1:

        lst.extend(array[0])

        for i in range(1, len(array)-1):
            row = array[i]
            lst.append(row[len(array)-1])
            row.pop(len(array)-1)
            print("POP1", array)

        row = array[len(array)-1]
        row.reverse()
        lst = lst + row

        new_list_to_add = []
        for i in range(1, len(array)-1):
            row = array[i]
            new_list_to_add.append(row[0])
            row.pop(0)
            print("POP2", array)
        new_list_to_add.reverse()
        lst = lst + new_list_to_add


        array.pop(0)
        print("POP3", array)
        array.pop(-1)
        print("POP4", array)

    if len(array) == 0:
        return lst
    else:
        return lst + array[0]
        
array = [[1,2,3,],
         [8,9,4,],
         [7,6,5,]]

print(snail(array))


#dodać while - dopóki array nie jest puste to powtarzaj to co wyżej, nowe arrat to....

# print(lst)
# print(array)


# def snail(snail_map):
#     first_row = snail_map[0]
#     second_row = snail_map[1]
#     third_row = snail_map[2]
#     lst = []
#     lst.extend([first_row[0], first_row[1], first_row[2], second_row[2], third_row[2], third_row[1], third_row[0], second_row[0], second_row[1]])
#     print(lst)
#     return lst


# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]

# print(snail(array))