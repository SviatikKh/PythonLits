sd = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
def sort_dic(sd_dic):
    new = {value: key for key, value in sd.items()}
    return new
print(sort_dic(sd))
