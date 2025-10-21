import os

users = {
    "ridho": {"password": "ridho105", "role": "admin"},
    "bayangan": {"password": "bayangan0", "role": "pengguna"}
}

album_perunggu = {
    "Pendar": {
        "tahun": 2020,
        "lagu": ["Menyala", "Jenuh kan Kutelan", "Rencana Usang"]
    },
    "Memorandum": {
        "tahun": 2022,
        "lagu": [
            "Tarung Bebas", "Canggih", "Pastikan Riuh Akhiri Malammu",
            "Membelah Belantara", "Haru Paling Biru", "Ini Abadi",
            "Biang Lara", "Per Hari Ini", "Kalibata, 2012", "Prematur (ft. hara)", "33x"
        ]
    },
    "Dalam Dinamika": {
        "tahun": 2025,
        "lagu": [
            "Tapi", "Amalan Baik", "Gemilang", "Pikiran Yang Matang",
            "Biarkan Ia Tumbuh", "Berita Buruk", "Aku Ada Untukmu", "Berhasil", "Abu"
        ]
    }
}

os.system("cls")
print("""
=======================================================
|        SELAMAT DATANG DI LIST ALBUM PERUNGGU        |
|     Login / Register untuk mengakses data album.    |
=======================================================
""")

login_berhasil = False

while True:
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu (1/2/3): ")

    if pilih == "1":
        os.system("cls")
        for percobaan in range(3):
            print("=========== LOGIN USER ===========")
            username_in = input("Masukkan username: ")
            password_in = input("Masukkan password: ")

            if username_in in users and users[username_in]["password"] == password_in:
                role = users[username_in]["role"]
                login_berhasil = True
                break
            else:
                print("Login gagal! Coba lagi.\n")

        if not login_berhasil:
            print("Kesempatan login habis. Program keluar.")
            exit()
        else:
            break

    elif pilih == "2":
        os.system("cls")
        print("============ REGISTER AKUN ============")
        username_baru = input("Masukkan username baru: ")
        if username_baru in users:
            print("Username sudah digunakan!\n")
        else:
            password_baru = input("Masukkan password: ")
            role_baru = input("Masukkan role (admin/pengguna): ").lower()
            if role_baru not in ["admin", "pengguna"]:
                print("Role tidak valid, default = pengguna.")
                role_baru = "pengguna"
            users[username_baru] = {"password": password_baru, "role": role_baru}
            os.system("cls")
            print("Akun berhasil dibuat! Silakan login.\n")

    elif pilih == "3":
        print("Terima kasih telah menggunakan program ini!")
        exit()

    else:
        print("Pilihan tidak valid!\n")

os.system("cls")
print(f"Selamat datang, {username_in.upper()}! Anda login sebagai {role.upper()}.\n")

if role == "admin":
    while True:
        print("""
================= AKUN ADMIN ==================
1. Tampilkan Semua Album
2. Tambah Album Baru
3. Ubah Album
4. Hapus Album
5. Keluar
===============================================
""")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            os.system("cls")
            print("=== DAFTAR ALBUM PERUNGGU ===")
            for i, (judul, data) in enumerate(album_perunggu.items(), start=1):
                print(f"\nAlbum ke-{i}")
                print(f"Judul : {judul}")
                print(f"Tahun : {data['tahun']}")
                print("Lagu  :")
                for lagu in data["lagu"]:
                    print(f" - {lagu}")

        elif pilih == "2":
            os.system("cls")
            judul = input("Masukkan judul album baru: ")
            tahun = input("Masukkan tahun rilis: ")
            lagu_input = input("Masukkan lagu-lagu (pisahkan dengan koma): ")
            lagu_baru = [lagu.strip() for lagu in lagu_input.split(",")]
            album_perunggu[judul] = {"tahun": tahun, "lagu": lagu_baru}
            os.system("cls")
            print("Album baru berhasil ditambahkan!")

        elif pilih == "3":
            os.system("cls")
            print("=== DAFTAR ALBUM TERSEDIA ===")
            for judul in album_perunggu:
                print(f"- {judul}")
            print("=============================")
            ubah = input("\nMasukkan judul album yang ingin diubah: ")

            if ubah in album_perunggu:
                print("Album ditemukan.")
                judul_baru = input("Masukkan judul baru: ")
                tahun_baru = input("Masukkan tahun baru: ")
                lagu_input = input("Masukkan daftar lagu baru (pisahkan koma): ")
                album_perunggu[judul_baru] = {
                    "tahun": tahun_baru,
                    "lagu": [lagu.strip() for lagu in lagu_input.split(",")]
                }
                if judul_baru != ubah:
                    del album_perunggu[ubah]
                os.system("cls")
                print("Album berhasil diperbarui!")
            else:
                print("Album tidak ditemukan.")

        elif pilih == "4":
            os.system("cls")
            print("=== DAFTAR ALBUM TERSEDIA ===")
            for judul in album_perunggu:
                print(f"- {judul}")
            print("=============================")
            hapus = input("\nMasukkan judul album yang ingin dihapus: ")

            if hapus in album_perunggu:
                del album_perunggu[hapus]
                print("Album berhasil dihapus!")
            else:
                print("Album tidak ditemukan.")

        elif pilih == "5":
            os.system("cls")
            print("Terima kasih, Admin!")
            break
        else:
            print("Pilihan tidak valid!")

else:
    while True:
        print("""
================== AKUN PENGGUNA =================
1. Lihat Daftar Album
2. Lihat Lagu dari Album
3. Keluar
==================================================
""")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            os.system("cls")
            print("=== DAFTAR ALBUM PERUNGGU ===")
            for judul, data in album_perunggu.items():
                print(f"- {judul} ({data['tahun']})")

        elif pilih == "2":
            os.system("cls")
            print("=== DAFTAR ALBUM TERSEDIA ===")
            for judul in album_perunggu:
                print(f"- {judul}")
            print("=============================")
            cari = input("\nMasukkan judul album: ")

            if cari in album_perunggu:
                print(f"\nLagu-lagu dalam album {cari}:")
                for lagu in album_perunggu[cari]["lagu"]:
                    print(f" - {lagu}")
            else:
                print("Album tidak ditemukan.")

        elif pilih == "3":
            os.system("cls")
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid!")