import collections
import itertools

def solution(orders, course):
    collection_list = []
    result = []
    orders = collections.Counter(orders)
    for order, value in orders.items():
        if value >= 2:
            collection_list += [order for i in range(value)]
        else:
            collection_list += [order for order2 in orders.keys() if all( char in order2 for char in order)]
    result = {key:value for key, value in collections.Counter(collection_list).items() if value in course}
    

    print(result)
    return sorted(result)


def solution1(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)
        most_ordered = collections.Counter(order_combinations).most_common()
        print(collections.Counter(order_combinations))
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	
course = [2,3,5]	
solution1(orders, course)


