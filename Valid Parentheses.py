
def valid_parentheses(paren_str):
    while "()" in paren_str:
        paren_str = paren_str.replace("()", "")
    
    # if paren_str == "":
    #     return True
    # else:
    #     return False
    return paren_str == ""

paren_str = ")(()))"
print(valid_parentheses(paren_str))

# while "()" in paren_str:
#     paren_str = paren_str.replace("()", "")
    
# if paren_str == "":
#     print("T")
# else:
#     print("F")