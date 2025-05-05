from perpustakaan import Perpustakaan

perpus = Perpustakaan()

while True:
    print("=== Menu Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Edit Buku")
    print("4. Hapus Buku")
    print("5. Simpan ke File")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        perpus.tambah_buku()
    elif pilihan == "2":
        perpus.tampil_buku()
    elif pilihan == "3":
        perpus.edit_buku()
    elif pilihan == "4":
        perpus.hapus_buku()
    elif pilihan == "6":
        perpus.simpan()
        print("keluar dari program")
        break