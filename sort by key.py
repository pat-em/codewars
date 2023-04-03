
def sum_points(name):
    points = len(name)
    points += 10 if name.startswith('A') or name.endswith('o') else 0
    return points


def sort_by_points(name_list):
    sorted_list = sorted(name_list, key=sum_points, reverse=True)
    return sorted_list

name_list = ['Ania', 'Tomek', 'Tymon', 'Bruno', 'Konstancja']
print(sort_by_points(name_list))