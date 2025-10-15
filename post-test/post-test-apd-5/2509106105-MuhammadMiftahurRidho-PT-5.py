import os

users = [
    ["admin", "admin123", "admin"],
    ["ridho", "ridho321", "pengguna"],
]

# =======================================
# |     List Album Lagu Perunggu        |
# =======================================
album_perunggu = [
    ["Pendar", 2020, ["Menyala", "Jenuh kan Kutelan", "Rencana Usang"]],
    ["Memorandum", 2022, [
        "Tarung Bebas", "Canggih", "Pastikan Riuh Akhiri Malammu",
        "Membelah Belantara", "Haru Paling Biru", "Ini Abadi",
        "Biang Lara", "Per Hari Ini", "Kalibata, 2012", "Prematur (ft. hara)", "33x"
    ]],
    ["Dalam Dinamika", 2025, [
        "Tapi", "Amalan Baik", "Gemilang", "Pikiran Yang Matang",
        "Biarkan Ia Tumbuh", "Berita Buruk", "Aku Ada Untukmu", "Berhasil", "Abu"
    ]]
]

os.system("cls")
print("""
=======================================================
|        SELAMAT DATANG DI LIST ALBUM PERUNGGU        |
|          Login untuk mengakses data album.          |
=======================================================
""")

# ================
# |  Login User  |
# ================
login_berhasil = False
for percobaan in range(3):
    print("============ LOGIN USER ============")
    username_in = input("Masukkan username: ")
    password_in = input("Masukkan password: ")

    for user in users:
        if user[0] == username_in and user[1] == password_in:
            role = user[2]
            login_berhasil = True
            break

    if login_berhasil:
        break
    else:
        print("Login gagal! Coba lagi.\n")

if not login_berhasil:
    print("Kesempatan login habis. Program keluar.")
    exit()

os.system("cls")
print(f"Selamat datang, {username_in.upper()}! Anda login sebagai {role.upper()}.\n")

# ==================
# |   Akun Admin   |
# ==================
if role == "admin":
    while True:
        print("""
==================== AKUN ADMIN =====================
1. Tampilkan Semua Album
2. Tambah Album Baru
3. Ubah Album
4. Hapus Album
5. Keluar
======================================================
""")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            os.system("cls")
            print("=== DAFTAR ALBUM PERUNGGU ===")
            for i in range(len(album_perunggu)):
                print(f"\nAlbum ke-{i+1}")
                print(f"Judul : {album_perunggu[i][0]}")
                print(f"Tahun : {album_perunggu[i][1]}")
                print("Lagu  :")
                for lagu in album_perunggu[i][2]:
                    print(f" - {lagu}")

        elif pilih == "2":
            os.system("cls")
            judul = input("Masukkan judul album baru: ")
            tahun = input("Masukkan tahun rilis: ")
            lagu_input = input("Masukkan lagu-lagu (pisahkan dengan koma): ")
            lagu_baru = lagu_input.split(",")
            album_perunggu = album_perunggu + [[judul, tahun, lagu_baru]]
            os.system("cls")
            print("Album baru berhasil ditambahkan!")

        elif pilih == "3":
            os.system("cls")
            ubah = input("Masukkan judul album yang ingin diubah: ")
            ditemukan = False
            for i in range(len(album_perunggu)):
                if album_perunggu[i][0].lower() == ubah.lower():
                    ditemukan = True
                    print("Album ditemukan.")
                    album_perunggu[i][0] = input("Masukkan judul baru: ")
                    album_perunggu[i][1] = input("Masukkan tahun baru: ")
                    lagu_input = input("Masukkan daftar lagu baru (pisahkan koma): ")
                    album_perunggu[i][2] = lagu_input.split(",")
                    os.system("cls")
                    print("Album berhasil diperbarui!")
                    break
            if not ditemukan:
                print("Album tidak ditemukan.")

        elif pilih == "4":
            os.system("cls")
            hapus = input("Masukkan judul album yang ingin dihapus: ")
            baru = []
            ditemukan = False
            for a in album_perunggu:
                if a[0].lower() != hapus.lower():
                    baru += [a]
                else:
                    ditemukan = True
            album_perunggu = baru
            if ditemukan:
                print("Album berhasil dihapus!")
            else:
                print("Album tidak ditemukan.")

        elif pilih == "5":
            os.system("cls")
            print("Terima kasih, Admin!")
            break
        else:
            print("Pilihan tidak valid!")

# =========================
# |     Akun Pengguna     |
# =========================
else:
    while True:
        print("""
==================== AKUN PENGGUNA ===================
1. Lihat Daftar Album
2. Lihat Lagu dari Album
3. Keluar
======================================================
""")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            os.system("cls")
            print("=== DAFTAR ALBUM PERUNGGU ===")
            for i in range(len(album_perunggu)):
                print(f"- {album_perunggu[i][0]} ({album_perunggu[i][1]})")

        elif pilih == "2":
            os.system("cls")
            cari = input("Masukkan judul album: ")
            ditemukan = False
            for album in album_perunggu:
                if album[0].lower() == cari.lower():
                    print(f"\nLagu-lagu dalam album {album[0]}:")
                    for lagu in album[2]:
                        print(f" - {lagu}")
                    ditemukan = True
            if not ditemukan:
                print("Album tidak ditemukan.")

        elif pilih == "3":
            os.system("cls")
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid!")