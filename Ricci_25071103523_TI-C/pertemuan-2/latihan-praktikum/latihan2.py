def rata_rata(nilai):
  if len(nilai) != 0:
    jumlah = 0
    for x in nilai:
      jumlah += x
    return jumlah / len(nilai)
  else:
    print("Data kosong")

list1 = [80, 75, 90, 60, 85]
print(f'Rata rata nilai mahasiswa adalah = {rata_rata(list1)} ')


#NO2
def bilangan_prima(n):
  list2 = []
  for x in range(1,n):
    if x < 2:
      pass
    elif x == 2:
      list2.append(x)
    elif x > 2:
      for i in range(2,x):
        if x % i == 0:
          break
      else:
        list2.append(x) 
  return list2

print(bilangan_prima(50))

#NO3
def jumlah_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlah_digit(n // 10)

print(jumlah_digit(1234))


#NO4
def pangkat_rekursif(a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat_rekursif(a, b - 1)
    
print(pangkat_rekursif(2, 5))


import math

def jarak(x1, y1, x2, y2):
  selisih_x = x2-x1
  selisih_y = y2-y1
  d = math.sqrt(math.pow(selisih_x, 2) + math.pow(selisih_y, 2))
  return d

print(f'jarak = {jarak(1, 2, 3, 4)}')



