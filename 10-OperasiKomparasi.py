# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih dari >
print("\n=====LEBIH DARI (>)=====\n")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# kurang dari <
print("\n=====KURANG DARI (<)=====\n")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# lebih dari sama dengan
print("\n=====LEBIH DARI SAMA DENGAN (>=)=====\n")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# sama dengan (==)
print("\n=====SAMA DENGAN (==)=====\n")
hasil = a == 3
print(a,"==",3,"=",hasil)
hasil = b == 3
print(b,"==",3,"=",hasil)
hasil = b == 2
print(b,"==",2,"=",hasil)

# tidak sama dengan (!=)
print("\n=====TIDAK SAMA DENGAN (!=)=====\n")
hasil = a != 3
print(a,"!=",3,"=",hasil)
hasil = b != 3
print(b,"!=",3,"=",hasil)
hasil = b != 2
print(b,"!=",2,"=",hasil)

# 'is' sebagai komparasi objek identity
x = 5 # ini adalah assignmnet membuat object
y = 5
print("\n=====OBJECT IDENTITY (is)=====\n")
print("nilai x =",x,", id =", hex(id(x)))
print("nilai y =",y,", id =", hex(id(y)))
hasil = x is y
print("x is y", hasil)

x = 5 # ini adalah assignmnet membuat object
y = 5
print("nilai x =",x,", id =", hex(id(x)))
print("nilai y =",y,", id =", hex(id(y)))
hasil = x is not y
print("x is y", hasil)

x = 5 # ini adalah assignmnet membuat object
y = 6
print("nilai x =",x,", id =", hex(id(x)))
print("nilai y =",y,", id =", hex(id(y)))
hasil = x is not y
print("x is y", hasil)