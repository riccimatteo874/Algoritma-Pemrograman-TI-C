#Anda dapat menampilkan literal string dengan print()
print('hello world')
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) #Anda dapat menetapkan string multi-baris ke variabel dengan menggunakan tiga tanda kutip

a = "Hello, World!"
print(len(a)) #untuk mendapatkan panjang sebuah string, gunakan len()

b = "Hello, World!"
print(b[2:5]) #Anda dapat mengembalikan rentang karakter dengan menggunakan sintaks slice.
#Tentukan indeks awal dan indeks akhir, dipisahkan oleh titik dua, untuk mendapatkan sebagian dari string

a = "Hello, World!"
print(a.upper()) #Metode ini upper()mengembalikan string dalam huruf besar
a = "Hello, World!"
print(a.lower())#Metode ini lower()mengembalikan string dalam huruf kecil
a = "Hello, World!"
print(a.replace("H", "J"))
#Metode ini replace()mengganti sebuah string dengan string lain
