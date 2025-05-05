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

    def hapus_buku(self):
        judul = input("masukan judul yang akan dihapus: ")
        awal = len(self.daftar_buku)
        self.daftar_buku = [b for b in self.daftar_buku if b.judul != judul]
        if len(self.daftar_buku) < awal:
            print("buku berhasil dihapus")
        else:
            print("buku tidak ditemukan")

    def edit_buku(self):
        judul = input("masukan judul yang mau diedit: ")
        for buku in self.daftar_buku:
            if buku.judul == judul:
                new_judul = input("masukan judul baru: ")
                new_penulis = input("masukan nama penulis baru: ")
                if new_judul:
                    buku.judul = new_judul
                if new_penulis:
                    buku.penulis = new_penulis
                print("data buku berhasil dirubah")
                return
        print("judul tidak ditemukan")