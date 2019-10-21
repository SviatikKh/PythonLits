print('Please input your e-mail: ')
e1 = input()
e11 = e1.lower().strip()
print('Please repeat your e-mail: ')
e2 = input()
e22 = e2.lower().strip()
if '@' in e11 and e22 and e11 == e22:
    print('Ok!')
else:
    print('Your e-mails do not match or this is not an email')