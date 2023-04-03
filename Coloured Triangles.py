def triangle(initial_row):
    
    if len(initial_row) == 1:
        return initial_row

    previous_row = initial_row

    def next(previous_row):
        previous_row = list(previous_row)
        next_row = []
        for i in range(len(previous_row)-1):
            if previous_row[i] == previous_row[i+1]:
                next_row.append(previous_row[i])
            else:
                if (previous_row[i] == "R" and previous_row[i+1] == "G") or (previous_row[i] == "G" and previous_row[i+1] == "R"):
                    next_row.append("B")
                if (previous_row[i] == "R" and previous_row[i+1] == "B") or (previous_row[i] == "B" and previous_row[i+1] == "R"):
                    next_row.append("G")
                if (previous_row[i] == "G" and previous_row[i+1] == "B") or (previous_row[i] == "B" and previous_row[i+1] == "G"):
                    next_row.append("R")


        return "".join(next_row)
    
    while len(previous_row) > 1:
        print(previous_row)
        previous_row = next(previous_row)
    
    last_row = previous_row
  
    return last_row
triangle("RBRGBRBGGRRRBGBBBGG")
##############################################
COLORS = set("RGB")

def triangle(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row
