# operasi logika atau boolean

# not, or, and, xor

# NOT
print("====NOT====")
a = True
c =  not a
print("Data a =",a)
print("--------------NOT")
print("Data c =",c)

# OR (Jika salah satu True, maka hasilnya akan True)
print("====OR====")
a = False
b = False
c =  a or b
print(a, "OR", b, "=", c)
a = False
b = True
c =  a or b
print(a, "OR", b, " =", c)
a = True
b = False
c =  a or b
print(a, " OR", b, "=", c)
a = True
b = True
c =  a or b
print(a, " OR", b, " =", c)

# AND (Akan True jika keduanya True)
print("====AND====")
a = False
b = False
c =  a and b
print(a, "AND", b, "=", c)
a = False
b = True
c =  a and b
print(a, "AND", b, " =", c)
a = True
b = False
c =  a and b
print(a, " AND", b, "=", c)
a = True
b = True
c =  a and b
print(a, " AND", b, " =", c)

# XOR (akan True jika salah satu True, sisanya False)
print("====XOR====")
a = False
b = False
c =  a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c =  a ^ b
print(a, "XOR", b, " =", c)
a = True
b = False
c =  a ^ b
print(a, " XOR", b, "=", c)
a = True
b = True
c =  a ^ b
print(a, " XOR", b, " =", c)