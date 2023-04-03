def in_array(array1, array2):
    r = []

    for word1 in array1:
        for word2 in array2:
            if word1 in word2 and word1 not in r:
                r.append(word1)
    
    return sorted(r)

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))
