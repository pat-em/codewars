def how_much_water(water, load, clothes):
    if clothes > 2*load:
        return "Too much clothes" 
    if clothes < load:
        return "Not enough clothes"
    else:
        return round(water * 1.1 ** (clothes - load), 2)


print(how_much_water(10,10,21), 'Too much clothes')
print(how_much_water(10,10,2), 'Not enough clothes')
print(how_much_water(10,11,20), 23.58, "water = 10")     
print(how_much_water(50,15,29), 189.87, "water = 20")