class Buku:
    def __init__(self, penulis, judul):
        self.judul = judul
        self.penulis = penulis

    def tampil(self):
        print(f"buku {self.judul} ditulis oleh {self.penulis}")

    def to_dict(self):
        return{'judul':self.judul, 'penulis':self.penulis}   

    @staticmethod
    def from_dict(data):
        return Buku(data["judul"], data["penulis"])