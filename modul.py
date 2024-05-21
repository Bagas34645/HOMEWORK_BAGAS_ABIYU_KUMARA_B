data_stok_barang = []

def tambah_data_barang():
    nama_barang = input("Masukkan nama barang: ")
    stok = input("Masukkan stok: ")
    data_stok_barang.append({'nama_barang': nama_barang, 'stok': stok})
    print("Data barang berhasil ditambahkan")

def hapus_data_barang():
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
    found = False
    for barang in data_stok_barang:
        if barang['nama_barang'] == nama_barang:
            data_stok_barang.remove(barang)
            print(f"Data barang {nama_barang} berhasil dihapus")
            found = True
            break
    if not found:
        print(f"Data barang {nama_barang} tidak ditemukan")

def tampilkan_data_barang():
    for indeks, barang in enumerate(data_stok_barang):
        print(f"{indeks+1}. Nama Barang: {barang['nama_barang']}, Stok: {barang['stok']}")

def cek_stok_kosong():
    print("+"+"-"*49+"+")
    print("|"+" "*19+"Data Gudang"+19*" "+"|")
    print("+"+"-"*49+"+")
    if not data_stok_barang:
        print("Data stok barang kosong")

def tampilkan_jumlah_data():
    jumlah_data = len(data_stok_barang)
    print(f"Jumlah data barang yang tersimpan: {jumlah_data}")

def cari_data_berdasarkan_nama():
    nama_barang = input("Masukkan nama barang yang ingin dicari: ")
    hasil_pencarian = []
    for barang in data_stok_barang:
        if nama_barang.lower() in barang['nama_barang'].lower():
            hasil_pencarian.append(barang)

    if hasil_pencarian:
        for barang in hasil_pencarian:
            print(f"Nama Barang: {barang['nama_barang']}, Stok: {barang['stok']}")
    else:
        print("Barang tidak ditemukan.")
         
def edit_data_berdasarkan_indeks():
    try:
        indeks = int(input("Masukkan indeks barang yang ingin diedit: "))
        if indeks < 0 or indeks >= len(data_stok_barang):
            print("Indeks di luar jangkauan")
            return
        
        nama_barang_baru = input("Masukkan nama barang baru: ")
        stok_baru = input("Masukkan stok baru: ")
        
        data_stok_barang[indeks]['nama_barang'] = nama_barang_baru
        data_stok_barang[indeks]['stok'] = stok_baru
        print(f"Data barang pada indeks {indeks} berhasil diupdate")
    except ValueError:
        print("Indeks harus berupa angka")
