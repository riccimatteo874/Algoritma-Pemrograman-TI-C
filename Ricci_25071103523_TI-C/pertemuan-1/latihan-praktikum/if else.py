#Pernyataan "if" ditulis dengan menggunakan kata kunci "if" .
#contoh
a = 33
b = 200
if b > a:
  print("b is greater than a")

#ELIF
# Kata kunci elif memungkinkan Anda untuk memeriksa beberapa ekspresi untuk nilai True 
# dan mengeksekusi blok kode segera setelah salah satu kondisi bernilai True .
#Contoh
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Pernyataan else dieksekusi ketika kondisi if (dan kondisi elif lainnya ) bernilai False
# contoh
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")