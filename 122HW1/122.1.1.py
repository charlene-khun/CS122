def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

print(gcd(8,12))
print(gcd(20,24))