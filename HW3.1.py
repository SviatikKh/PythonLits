def max_el(list_n, n = 1):
    list_n.sort(reverse = True)
    list_max = list_n[0:n]
    return(list_max)

err = [1, 6, 8, 5, 4, 7]
print(max_el(err, 3))
