# strng = "103 123 4444 99 2000"

def sum_string(s):
    sum = 0
    for digit in s:
        sum += int(digit)
    return sum

def order_weight(strng):
    initial_list = sorted(strng.split()) #['99', '103', '123', '2000', '4444']
    result = " ".join(sorted(initial_list, key=sum_string))

    return result

    