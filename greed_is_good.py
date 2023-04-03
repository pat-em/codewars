points = {
    1:1000,
    6:600,
    5:500,
    4:400,
    3:300,
    2:200
          }

def score(dice):
    sum = 0

    for i in range(7):
        if dice.count(i) >= 3:
            sum += points[i]

    for i in range(1,3):
        if dice.count(1) == i:
            sum += i *100
        if dice.count(5) == i:
            sum += i *50

    for i in range(4,6):
        if dice.count(1) == i:
            sum += (i-3) *100
        if dice.count(5) == i:
            sum += (i-3) *50

    return sum

# SCORES = [
#   # triples
#   ["111", 1000],
#   ["666", 600],
#   ["555", 500],
#   ["444", 400],
#   ["333", 300],
#   ["222", 200],
#   # singles
#   ["1", 100],
#   ["1", 100],
#   ["5", 50],
#   ["5", 50] ]


# def score(dice):
#     dice = "".join(str(d) for d in sorted(dice))
#     total = 0
    
#     for key, val in SCORES:
#         if key in dice:
#             total += val
#             dice = dice.replace(key, "", 1)
    
#     return total