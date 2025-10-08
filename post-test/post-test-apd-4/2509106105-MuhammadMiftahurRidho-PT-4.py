USERNAME = "MUHAMMAD MIFTAHUR RIDHO"
PASSWORD = "2509106105"

for i in range(3):
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Berhasil!\n")
        break
    else:
        if i <2:
            print("Login Gagal, Silahkan Coba Lagi.\n")
else:
    print("Login Gagal.")
    exit()

while True:
    print("=== MENU PEMBELIAN TIKET BIOSKOP XX0 ===")
    print("1. Tiket Reguler : Rp 50.000)")
    print("2. Tiket VIP     : Rp 100.000)")
    print("3. Tiket VVIP    : Rp 150.000)")
    print("4. Keluar")
    
    pilihan = input("Pilih opsi tiket (1-4): ")

    if pilihan not in ["1","2","3","4"]:
        print("Pilihan tidak valid! Silakan masukkan angka 1-4.\n")
        continue
    if pilihan == "4":
        print("Kamu keluar dari menu pembelian, Terima kasih!")
        break

    if pilihan == "1":
             harga = 50000
             jenis = "Reguler"
    elif pilihan == "2":
             harga = 100000
             jenis = "VIP"
    elif pilihan == "3":
             harga = 150000
             jenis = "VVIP"

    jumlah_tiket = input("Masukkan jumlah tiket yang ingin dibeli: ")

    if all(char in "0123456789" for char in jumlah_tiket):
        jumlah = int(jumlah_tiket)
    else:
        print("Jumlah tiket harus berupa angka")
        continue
    
    total_bayar = 0 

    for i in range(jumlah):
        total_bayar += harga
    else:
        print("\n=== STRUK PEMBELIAN ===")
        print(f"Jenis Tiket  : {jenis}")
        print(f"Jumlah Tiket : {jumlah_tiket}")
        print(f"Total Bayar  : Rp {total_bayar:,}")

    if total_bayar >= 300000:
        potongan = total_bayar * 0.12
    elif total_bayar >= 200000:
        potongan = total_bayar * 0.08
    elif total_bayar >= 150000:
        print("kamu dapat poster film ekslusif.")
        break

    total_akhir = total_bayar - potongan
    print(f"Potongan     : Rp {potongan:,}")
    print(f"Total Akhir  : Rp {total_akhir:,}")
    break