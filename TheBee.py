def the_bee(n):
    cells = [0]*(2*n+1)
    cells[n] = 1
    
    for i in range(1, 4*n-2):
        for j in range(i%2+1, 2*n, 2):
            cells[j-1] += cells[j]
            cells[j+1] += cells[j]
    
    return cells[n]

print(the_bee(5))