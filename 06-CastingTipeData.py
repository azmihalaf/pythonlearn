# merubah dari satu tipe ke tipe lain 

# tipe data = int, float, str, bool

## INTEGER
print("====INTEGER====")
data_int = 9;
print("Data =", data_int,"type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan flase jika nilai int = 0
print("Data =", data_float,"type =", type(data_float))
print("Data =", data_str,"type =", type(data_str))
print("Data =", data_bool,"type =", type(data_bool))
print(" ")

## FLOAT
print("====FLOAT====")
data_float = 9.5;
print("Data =", data_float,"type =", type(data_float))

data_float = int(data_float) # akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float) # akan flase jika nilai float = 0
print("Data =", data_int,"type =", type(data_int))
print("Data =", data_str,"type =", type(data_str))
print("Data =", data_bool,"type =", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = True;
print("Data =", data_bool,"type =", type(data_bool))

data_int = int(data_bool) # akan dibulatkan kebawah
data_str = str(data_bool)
data_float = float(data_bool) # akan flase jika nilai float = 0
print("Data =", data_int,"type =", type(data_int))
print("Data =", data_str,"type =", type(data_str))
print("Data =", data_float,"type =", type(data_float))

## STRING
print("====STRING====")
data_str = "0";
print("Data =", data_str,"type =", type(data_str))

data_int = int(data_str) # akan dibulatkan kebawah
data_float = float(data_str)
data_bool = bool(data_str) # akan flase jika string kosong
print("Data =", data_int,"type =", type(data_int))
print("Data =", data_float,"type =", type(data_float))
print("Data =", data_bool,"type =", type(data_bool))