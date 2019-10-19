# n = input()
# n1 = n*2
# print(n1)
# n2 = n*3
# print(n2)
# print(int(n)+int(n1)+int(n2))

v = input()

if '.' in v:
    print("Float")
elif  v.isdigit:
    print('Int')
else:
    print("Str")
