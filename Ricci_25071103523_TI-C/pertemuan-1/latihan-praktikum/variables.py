#VARIABEL
'''
Python tidak memiliki perintah untuk mendeklarasikan variabel.
Sebuah variabel tercipta saat pertama kali Anda memberikan nilai padanya.
'''
#CONTOH
x = 5
y = "John"

#Jika Anda ingin menentukan tipe data suatu variabel, ini dapat dilakukan dengan melakukan casting.
#Contoh
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Nama variabel peka terhadap huruf besar dan kecil.

'''
Aturan untuk variabel Python:
Nama variabel harus diawali dengan huruf atau karakter garis bawah.
Nama variabel tidak boleh diawali dengan angka.
Nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (Az, 0-9, dan _).
Nama variabel peka terhadap huruf besar dan kecil (age, Age, dan AGE adalah tiga variabel yang berbeda).
Nama variabel tidak boleh berupa kata kunci Python apa pun .
'''

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Python memungkinkan Anda untuk menetapkan nilai ke beberapa variabel dalam satu baris

x = y = z = "Orange"
print(x)
print(y)
print(z)
#juga dapat menetapkan satu nilai untuk beberapa variabel