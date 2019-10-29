l1 = {'1', '2', '3', '7', '8', '11', '12'}
l2 = {'1', '3', '11', '15'}
def search(lst1, lst2):
    l3 = {}
    for zn in lst1:
        if zn in lst2:
            l3 = set.intersection(lst1, lst2)
    return l3
print(search(l1, l2))