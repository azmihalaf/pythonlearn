data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
  1. Dengan menggunakan single quote '...'
  2. Dengan menggunakan double quote '...'

'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo apa kabar"')
print("'Halo apa kabar'")
print("Ini adalah hari Jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')

# backslash
print("C:\\User\\Udin")

# tab
print("Udin\totong")

# backspace 
print("udin \botong, lagi baikkan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unic, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> comodere, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> windows

# 3. String literal atau raw

# hati - hati
print('C:\\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\New Folder')

# multiline literal string
print("""
Nama  : Udin
Kelas : 2KA32
""")

# multiline literal string dan raw
print(r"""
Nama    : Udin
Kelas   : 2KA32
Website : www.udinkarbu.com/indexID
""")