class Kendaraan:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info(self):
        print(f"mobil berwarna {self.warna}, bermerk {self.merk}, tahun {self.tahun}")