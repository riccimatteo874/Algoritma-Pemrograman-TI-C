class Vehicle:
  def __init__(self, jenis, merk, tahun_rilis):
    self.jenis = jenis
    self.merk = merk
    self.tahu_rilis = tahun_rilis
  
  def sound(self):
    return("suara")

class Mobil(Vehicle):
  def __init__(self, jenis, merk, tahun_rilis, warna):
    self.__warna = warna
  
  def get_warna(self):
    return self.__warna
  
class Motor(Vehicle):
  def __init__(self, jenis, merk, tahun_rilis, tampang):
    self.__tampang = tampang
  def set_tampang(self, tampang):
    self.__tampang = tampang

p1 = Vehicle('bagus', 'anu', 2017)
print(p1.sound())

p2 = Mobil('avanza', 'ana', 2018, 'hitam')
print(p2.get_warna())

p3 = Motor('mio', 'una', 2019, 'petak')
print(p3.set_tampang(2))