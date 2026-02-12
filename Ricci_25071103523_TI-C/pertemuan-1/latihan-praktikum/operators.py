#Operator digunakan untuk melakukan operasi pada variabel dan nilai.
#contoh penggunaan operator aritmatika
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#operaator penugasan
x = 1 
x += 1
x -=1
x *=2 
#dan operator lainnya seperti /= **= %= //= &= |=

#operator perbandingan 
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
#Operator perbandingan mengembalikan nilai Trueatau Falseberdasarkan perbandingan tersebut

#Operator logika (and, or, not)
x = 5

print(x > 0 and x < 10) #and

x = 5

print(x < 5 or x > 10) #or

x = 5

print(not(x > 3 and x < 10))#not

'''Operator Identitas
Operator identitas digunakan untuk membandingkan objek, bukan apakah objek tersebut sama, 
tetapi apakah objek tersebut benar-benar objek yang sama, dengan lokasi memori yang sama
'''

#Operator is akan mengembalikan nilai Truejika kedua variabel menunjuk ke objek yang sama:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#Operator is notakan mengembalikan nilai Truejika kedua variabel tidak menunjuk ke objek yang sama:

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)