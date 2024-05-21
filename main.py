import modul

def main_menu():
    while True:
        print("\n+"+"-"*49+"+")
        print("| Selamat datang di program Manajemen Stok Barang |")
        print("+"+"-"*49+"+")
        print("| Pilihan:                                        |")
        print("| 1. Tambah Data Barang                           |")
        print("| 2. Edit Data Barang                             |")
        print("| 3. Hapus Data Barang                            |")
        print("| 4. Cari Data Barang                             |")
        print("| 5. Tampilkan Data Barang                        |")
        print("| 6. Tampilkan Jumlah Data                        |")
        print("| 7. Keluar                                       |")

        print("+"+"-"*49+"+")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            modul.tambah_data_barang()
        elif pilihan == "2":
            modul.edit_data_berdasarkan_indeks()
        elif pilihan == "3":
            modul.hapus_data_barang()
        elif pilihan == "4":
            modul.cari_data_berdasarkan_nama()
        elif pilihan == "5":
            modul.cek_stok_kosong() 
            modul.tampilkan_data_barang()
        elif pilihan == "6":
            modul.tampilkan_jumlah_data()
        elif pilihan == "7":
            break
        else:
            print("Pilihan tidak valid")

main_menu()