nama_asli = "Muhammad Miftahur Ridho"
nim_asli = 2509106105

print("LOGIN AKUN")
nama = input("Masukkan nama ")
nim = int(input("Masukkan nim : " ))
if nama == nama_asli and nim == nim_asli:
    print("LOGIN BERHASIL")
    print("MENU PILIHAN PAKET LANGGANAN")
    print("1 Paket Bronze: Biaya administrasi 1%, akses dasar ke lagu-lagu populer")
    print("2 Paket Silver: Biaya administrasi 3%, akses lagu premium dan playlist kustom")
    print("3 Paket Gold: Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline")
    print("4 Paket Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")

    biaya_langganan = 1500000
    pilihan = input("SILAHKAN PILIH MENU PAKET LANGGANAN KAMU (1/2/3/4): ")

    if pilihan == "1":
        biaya_admin = 0.01
        paket = "Bronze: akses dasar ke lagu-lagu populer"
    elif pilihan == "2":
        biaya_admin = 0.03
        paket = "Silver: akses lagu premium dan playlist kustom"
    elif pilihan == "3":
        biaya_admin = 0.05
        paket = "Gold: akses lagu premium, playlist kustom, dan mode offline"
    elif pilihan == "4":
        biaya_admin = 0.07
        paket = "Platinum: akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"

    print("TOTAL PEMBAYARAN")
    Totalbayar = biaya_langganan + (biaya_langganan * biaya_admin)
    print(Totalbayar)
else:
    print("LOGIN GAGAL")