def simple(num):
    #n = int(input("n="))
    lst=[]
    for i in range(2, num+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst
    print (lst)
print(simple(num = int(input("n="))))
