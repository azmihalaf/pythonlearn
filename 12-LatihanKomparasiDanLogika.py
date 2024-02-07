'''# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++++3---------10++++++++

inputUser = float(input("Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n: "))

# ++++++++3-------------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =",isKurangDari)

# ------------------10+++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =",isLebihDari)

# ++++++++3---------10++++++++

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)


# ------3+++++++10-------
# kasus irisan

inputUser = float(input("\nMasukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n: "))

# ------3++++++++++++++++
# lebih dair 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =", isLebihDari)

#+++++++++++++++10-------
isKurangDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

# ------3+++++++10-------
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan: ", isCorrect)'''

# ==========PR==========
# (1) -------0++++++++5--------8++++++++11--------
# (2) +++++++0--------5++++++++8--------11++++++++

# (1)
# --------0++++++++5--------
inputUser = float(input("Masukkan angka yang\nlebih dari 0\ndan\nkurang dari 5\n: "))

# Penyelesaian 1
# --------0+++++++++++++++++
isLebihDari = inputUser > 0
print("Lebih dari 0 :", isLebihDari)

# +++++++++++++++++5--------
isKurangDari = inputUser < 5
print("Kurang dari 5 :",isKurangDari)

# AND
isCorrect1 = isLebihDari and isKurangDari
print("Angka yang anda masukkan :", isCorrect1)

# Penyelesaian 2
# --------8++++++++11--------
inputUser = float(input("Masukkan angka yang\nlebih dari 8\ndan\nkurang dari 11\n: "))

# --------8+++++++++++++++++
isLebihDari = inputUser > 8
print("Lebih dari 0 :", isLebihDari)

# +++++++++++++++++11--------
isKurangDari = inputUser < 11
print("Kurang dari 5 :",isKurangDari)

# AND
isCorrect2 = isLebihDari and isKurangDari
print("Angka yang anda masukkan :", isCorrect2)

# Gabungan (or)
isCorrect3 = isCorrect1 or isCorrect2
print("Keseluruhan angka bernilai :",isCorrect3)

print("\n",10*"=","\n")
# (2)
# ++++++++0--------5++++++++
inputUser = float(input("Masukkan angka yang\nkurang dari 0\ndan\nlebih dari 5\n: "))

# Penyelesaian 1
# ++++++++0-----------------
isKurangDari = inputUser < 0
print("Kurang dari 0 :", isKurangDari)

# +++++++++++++++++5--------
isLebihDari = inputUser > 5
print("Lebih dari 5 :",isLebihDari)

# OR
isCorrect1 = isLebihDari or isKurangDari
print("Angka yang anda masukkan :", isCorrect1)

# Penyelesaian 2
# ++++++++8--------11+++++++
inputUser = float(input("Masukkan angka yang\nkurang dari 8\ndan\nlebih dari 11\n: "))

# ++++++++8-----------------
isKurangDari = inputUser < 8
print("Kurang dari 8 :", isKurangDari)

# -----------------11+++++++
isLebihDari = inputUser > 11
print("Lebih dari 11 :",isLebihDari)

# AND
isCorrect2 = isLebihDari or isKurangDari
print("Angka yang anda masukkan :", isCorrect2)

# Gabungan (or)
isCorrect3 = isCorrect1 and isCorrect2
print("Keseluruhan angka bernilai :",isCorrect3)