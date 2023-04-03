def likes(name):
    if len(name) == 0:
        print("no one likes this")
    elif len(name) == 1:
        print("{} likes this".format(name[0]))
    elif len(name) == 2:
        print("{} and {} like this".format(name[0], name[1]))
    elif len(name) == 3:
        print("{}, {} and {} like this".format(name[0], name[1], name[2]))
    elif len(name) >3:
        print("{}, {} and {} others like this".format(name[0], name[1], (len(name)-2)))

likes([])
likes(["Peter"])
likes(["Jacob", "Alex"] )
likes(["Max", "John", "Mark"] )
likes(["Alex", "Jacob", "Mark", "Max"] )

#######################################
# def likes(names):
#     n = len(names)
#     return {
#         0: 'no one likes this',
#         1: '{} likes this', 
#         2: '{} and {} like this', 
#         3: '{}, {} and {} like this', 
#         4: '{}, {} and {others} others like this'
#     }[min(4, n)].format(*names[:3], others=n-2)
