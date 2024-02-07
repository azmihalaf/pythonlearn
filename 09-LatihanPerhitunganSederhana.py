# latihan konversi satuan temperature

# program konversi celscius ke satuan lain

'''print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah : ", celcius, "Celcius")

# reamur 
# (4/5)*C
reamur = (4/5) * celcius
print("Suhu dalam reamur : ", reamur, "Reamur")

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print("Suhu dalam fahrenheit : ", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin : ", kelvin, "kelvin")'''

# Mengkonversi fahrenheit ke kelvin
# konversi fahrenheit ke celcius > celcius ke kelvin
fahrenheit2 = float(input("Masukkan suhu dalam F : "))
celcius2 = (5/9) * (fahrenheit2-32)
kelvin2 = celcius2 + 273.15
print("Suhu dalam K :", kelvin2)

# Mengkonversi kelvin ke fahrenheit
kelvin3 = float(input("Masukkan suhu dalam K : "))
celcius3 = kelvin3 - 273.15
fahrenheit3 = (9/5 * celcius3) + 32
print("Suhu dalam F : ", fahrenheit3)