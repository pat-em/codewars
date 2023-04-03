def disemvowel(string_):
    vowels_list = ["o", "a", "e", "i", "u", "O", "A", "E", "I", "U"]
    for i in string_:
        if i in vowels_list:
            string_ = string_.replace(i, "")
    
    return string_

print(disemvowel("This website is for losers LOL!"))