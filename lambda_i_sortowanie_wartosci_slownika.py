#map(), która przyjmuje dwa argumenty. Pierwszym jest nazwa funkcji. 
#Pamiętaj, że przy podawaniu funkcji jako argumentu, podajesz tylko samą nazwę bez nawiasów (). 
#Drugim argumentem jest obiekt iterowalny. 
#Tak najprościej mówiąc map() iteruje po obiekcie podanym jako argument i na każdym  
#elemencie wykonuje funkcję podaną jako pierwszy argument.

def my_func(n):
    return n*(n-1)
numbers = [1,5,12,30]
with_func = list(map(my_func, numbers))
with_lambda = list(map(lambda a: a*(a-1), numbers))
print(with_func, with_lambda)

#Key przyjmuje funkcję, według której ma posortować sekwencję.
#Na przykład chcielibyśmy posortować wyrazy w zdaniu alfabetycznie ignorując to,
#czy wyraz zaczyna się od dużej czy małej litery:

print(sorted("Alicja Kot ma psa ale nie ma kota".split(), key=str.lower))
#>>>['ale', 'Alicja', 'Kot', 'kota', 'ma', 'ma', 'nie', 'psa']

print("_"*30, 'analityk.edu.pl')
things = {'a': 11, 'b': 2, 'c': 0, 'd': 33}
print(sorted(things)) #['a', 'b', 'c', 'd']
print(sorted(things.values())) #[0, 2, 11, 33]
print(sorted(things.items())) #[('a', 11), ('b', 2), ('c', 0), ('d', 33)]
print(sorted(things.items(), key=lambda x: x[1])) #[('c', 0), ('b', 2), ('a', 11), ('d', 33)]
