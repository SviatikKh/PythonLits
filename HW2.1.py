num = int(input())
if num >= 1000:
    print('Number greater then or equal 1000')
else:
    b = bin(num)
    o = oct(num)
    d = num
    h = hex(num)
print("{:>10} {:>10} {:>10} {:>10}".format("bin", "oct", "dec", "hex"))
#print("{[2:>10]} {[2:>10]} {:>10} {[2:>10]}".format(b, o, d, h))
print("     ", b[2:], "      ", o[2:], "       ", d, "        ", h[2:])



