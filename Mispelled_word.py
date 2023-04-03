def mispelled(word1,word2):

    if len(word1) == len(word2):
        lst = []
        lst.extend("S" if a == b else "D" for a, b in zip(word1, word2))
        if lst.count("D") > 1:
            return False
        else:
            return True
        
    if len(word1) > len(word2):
        if (len(word1) - len(word2)) > 1:
            return False
        else:
            if word2 in word1:
                return True
            else:
                return False
            
    if len(word2) > len(word1):
        if (len(word2) - len(word1)) > 1:
            return False
        else:
            if word1 in word2:
                return True
            else:
                return False    
            
print(mispelled('wTytMCF','aHR3IZ4'))
print(mispelled('versed','applb'))
print(mispelled('versed','v5rsed'))
print(mispelled('1versed','versed'))
print(mispelled('versed','versed'))

################################3
def mispelled(word1, word2):
    l1, l2 = len(word1), len(word2)
    if l1 == l2:
        return sum(1 for a, b in zip(word1, word2) if a != b) <= 1
    if l1 - l2 == 1:
        return word1.startswith(word2) or word1.endswith(word2)
    if l1 - l2 == -1:
        return word2.startswith(word1) or word2.endswith(word1)
    return False