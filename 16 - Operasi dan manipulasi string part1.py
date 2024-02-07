# operasi dan manipulasi string

# 1. Menyambung string (concatenate)

nama_pertama = "Udin"
nama_tengah = "The"
nama_akhir = "Creator"

nama_lengkap = nama_pertama + " " +nama_pertama + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari string

panjang = len(nama_lengkap)
print("Panjanga dari "+ nama_lengkap + " = "+ str(panjang))

# 3. Operator untuuk string

# Mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print(3*"WK")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-[2:5]:" + nama_lengkap[2:5])
print("index ke-[0,2,4,6,8]:" + nama_lengkap[0:8:2])


# item paling kecil
print("Paling kecil : " + min(nama_lengkap))
# item paling besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 118
print("Char untuk ASCII 118 adalah " + chr(data))

# 4. Operator dalam bentuk method
data = "udin harahap hutagalung"
jumlah = data.count("u")
print("Jumlah u pada " + data + " = " + str(jumlah))