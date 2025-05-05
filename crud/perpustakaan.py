import json
import os

from buku import Buku

class Perpustakaan:
    def __init__(self, filename="buku.json"):
        self.daftar_buku = []
        self.filename = filename
        self.load()

    def simpan(self):
        with open(self.filename, "w") as f:
            json.dump([buku.to_dict() for buku in self.daftar_buku], f)
        print("data disimpan ke file\n")
    
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.daftar_buku = [Buku.from_dict(d) for d in data]
            print("data buku dimuat")

    def tambah_buku(self):
        judul = input("masukan judul buku: ")
        penulis = input("masukan nama penulis: ")
        self.daftar_buku.append(Buku(judul, penulis))
        print("buku berhasil ditambahkan")

    def tampil_buku(self):
        if not self.daftar_buku:
            print("belum ada buku")
            return
        print("daftar buku:")
        for i, buku in enumerate(self.daftar_buku, 1):
            print(f"{i}. ", end="")
            buku.tampil()
        print()