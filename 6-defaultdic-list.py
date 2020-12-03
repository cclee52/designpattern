from collections import defaultdict


num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])
d = defaultdict(tuple_counter)
d['1'][1].append('A')
d['2'][1].append('B')
d['3'][1].append('C')
d['4'][1].append('D')
print(d)