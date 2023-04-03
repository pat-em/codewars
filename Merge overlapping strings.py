def merge_strings(first, second):

    sets_list = []

    for i in range(1, len(first)+1):
        set_to_check = first[len(first)-i:len(first)]
        if i<=len(second):
            if set_to_check in second[0:i]:
                sets_list.append(set_to_check)

    length_list = []

    for x in sets_list:
        length_list.append(len(x))

    if first != second and len(length_list) != 0:
        word = first + second[max(length_list):]
    elif first != second and len(length_list) == 0:
        word = first + second
    else:
        word = first

    return word
    
#############
# def merge_strings(first, second):
#     return [first + second[i:] for i in range(min(len(first), len(second))+1) if first[len(first)-i:] == second[:i]][-1]

