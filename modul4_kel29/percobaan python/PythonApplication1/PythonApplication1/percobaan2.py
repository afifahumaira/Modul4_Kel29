class contoh_method:
    #init method
  def __init__(self, afifa, dheyan):
    self.afifa = afifa
    self.dheyan  = dheyan

    #self parameter
  def mulai(self):
    print(f"Selamat Datang di Percobaan 2 {self.afifa} dan {self.dheyan}")

    #method dengan parameter
  def selesai(self, waktu):
    print("Percobaan akan selesai dalam :")
    while waktu > 0:
      print(waktu)
      waktu -= 1

        