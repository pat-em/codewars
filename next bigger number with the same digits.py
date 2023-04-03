# def next_bigger(n):
#     digits = list(str(n))

#     for i in range(len(digits)-2, -1, -1):
#         if digits[i] < digits[i+1]:
#             j = len(digits)-1
#             while digits[j] <= digits[i]:
#                 j -= 1
#             digits[i], digits[j] = digits[j], digits[i]
#             digits[i+1:] = sorted(digits[i+1:])
#             return int(''.join(digits))
        
#     return(-1)

# print(next_bigger(2017))

def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    a = n
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(n)):
            return a

print(next_bigger(10009))



