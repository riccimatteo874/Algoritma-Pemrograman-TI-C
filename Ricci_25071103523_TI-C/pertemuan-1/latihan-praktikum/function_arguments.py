'''
Contoh berikut memiliki fungsi dengan satu argumen (fname). 
Saat fungsi dipanggil, kita meneruskan nama depan, yang digunakan di dalam fungsi untuk mencetak nama lengkap:
'''
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Parameter adalah variabel yang tercantum di dalam tanda kurung pada definisi fungsi .
#Argumen adalah nilai sebenarnya yang dikirim ke fungsi saat fungsi tersebut dipanggil .
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument