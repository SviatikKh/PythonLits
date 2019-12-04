class Roman():
  def roman2arabic(self, roman):
      digit = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
      arabic = 0
      for d in roman:
          try:
              if digit[d]<=digit[roman[roman.find(d)+1]]:
                  arabic-=digit[d]
              else:
                  arabic+=digit[d]
          except IndexError:
              arabic+=digit[d]
      return arabic

class RomanNumber(Roman):
  def __init__(self, arabic):
    super().__init__(arabic)
    arabic.__oct__(self)
    return arabic
    print(arabic)

  def __init__(self, arabic):
    arabic.__hex__(self)
    return arabic
    print(arabic)

  def __init__(self, arabic):
    arabic.__bin__(self)
    return arabic
    print(arabic)

  def plus(self, arabic):
    arabic.__add__(self, arabic)
    print(arabic)

  def minus(self, arabic):
    arabic.__sub__(self, arabic)
    print(arabic)

  def mnozh(self, arabic):
    arabic.__mul__(self, arabic)
    print(arabic)

  def dil(self, arabic):
    arabic.__truediv__(self, arabic)
    print(arabic)

  


class Result(RomanNumber):
  def checkio(self, arabic):
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    thous = ["","M","MM","MMM","MMMM"]
  
    t = thous[arabic // 1000]
    h = hunds[arabic // 100 % 10]
    te = tens[arabic // 10 % 10]
    o = ones[arabic % 10]
    return t+h+te+o
    


p = Roman()
print(p.roman2arabic('X'))
p1 = RomanNumber()
print(p1.RomanNumber())
p2 =  Result()
print(p2.checkio())
