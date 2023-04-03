import string

alphabet = string.ascii_lowercase

def alphabet_position(text):
    position_list = ""
    text = text.lower()
    for i in text:
        if i in alphabet:
            position_list += str(alphabet.index(i)+1) + " "
    
    
    return position_list[:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))

#rozw 1
def alphabet_position(s):
  return " ".join(str(ord(c)-ord("a")+1) for c in s.lower() if c.isalpha())
#rozw 2
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        for letter in text:
            if letter.isalpha() == True:
                result = result + ' ' + str(alphabet.index(letter) + 1)
        return result.lstrip(' ')