def order_weight(strng):

    list_of_numbers = strng.split(" ")

    list_of_sum = []

    for i in range(len(list_of_numbers)):
        sum_digits = 0
        for d in list_of_numbers[i]:
            sum_digits += int(d)
        list_of_sum.append(sum_digits)

    t = list(zip(list_of_sum, list_of_numbers))
    t.sort()

    new_list_of_numbers = []
    for i in range(len(t)):
        weight_and_sum = t[i]
        new_list_of_numbers.append(weight_and_sum[1])
    return " ".join(new_list_of_numbers)


strng = "103 123 4444 99 2000"
print(order_weight(strng))