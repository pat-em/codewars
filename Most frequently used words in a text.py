import re
from collections import Counter

def top_3_words(text):
    # Use regex to extract words and ignore non-words
    words = re.findall(r"[a-zA-Z']+", text.lower())
    # Count the occurrences of each word
    word_counts = Counter(words)
    # Get the top 3 words (or fewer if there are fewer unique words)
    top_words = word_counts.most_common(3)
    # Return the top words as lowercase strings in descending order of frequency
    if not any(char.isalpha() for char in text):
        return []
    return [word[0] for word in top_words]

print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])