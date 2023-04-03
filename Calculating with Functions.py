numbers = {"zero": "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def CreateFunction(number_Name):
    source_f = '''
def f(*args):
    if len(args) == 0:
        global second
        second = "{}"
        return second
    else:
        source = ""
        first = "{}"
        source += first
        if args[0] == plus(*args): 
            source += plus(*args)
        elif args[0] == minus(*args):
            source += minus(*args)
        elif args[0] == times(*args):
            source += times(*args)
        elif args[0] == divided_by(*args):
            source += divided_by(*args)
        
        source += second
        result = eval(source)
        return(result)           
'''.format(numbers[number_Name], numbers[number_Name])
    exec(source_f, globals())
    return f

zero = CreateFunction("zero")
one = CreateFunction("one")
two = CreateFunction("two")
three = CreateFunction("three")
four = CreateFunction("four")
five = CreateFunction("five")
six = CreateFunction("six")
seven = CreateFunction("seven")
eight = CreateFunction("eight")
nine = CreateFunction("nine")

def plus(*args):
    return "+"

def minus(*args):
    return "-"

def times(*args):
    return "*"

def divided_by(*args):
    return "//"

print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)