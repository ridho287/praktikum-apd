# # # # # # # # listNama = ["dapupu", "bambang", "ucup", "otong"]

# # # # # # # # print(listNama[1])

# # # # # # # # Membuat set
# # # # # # # # buah = {"apel", "jeruk", "mangga", "apel"}
# # # # # # # # print(buah)

# # # # # # # angka_ganjil = {1, 3, 5, 7, 9}
# # # # # # # for angka in angka_ganjil:
# # # # # # #     print(angka)

# # # # # # # angka_ganjil.discard(11)
# # # # # # # print(angka_ganjil)

# # # # # # Daftar_buku = {
# # # # # #     "Buku1" : "Bumi Manusia",
# # # # # #     "Buku2" : "Laut Bercerita",
# # # # # #     "Buku3" : "Anak Semua Bangsa"
# # # # # # # }

# # # # # # # print()
# # # # # # # print(Daftar_buku)
# # # # # # # for attol in Daftar_buku.items():
# # # # # # #     print(attol)
# # # # # # #     print("")

# # # # # Biodata = {
# # # # #     "Nama" : "Ananda Daffa Harahap",
# # # # #     "NIM" : 2409106050,
# # # # #     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data",
# # # # #              "Jaringan Komputer","Sistem Operasi"],
# # # # #     "Mahasiswa_Aktif" : True,
# # # # #     "Social Media" : {"Instagram" : "daffahrhap"
# # # # #     }
# # # # # }

# # # # # print(f"nama saya adalah {Biodata["mahasigma"]}")
# # # # # print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# # # # # print(f"nama saya adalah {Biodata.get("Nama")}")
# # # # # print(Biodata.get("mahasigma"))

# # # # # # print(Biodata["Nama"])
# # # # # print(Biodata["KRS"][1:5])

# # # # # list_nama= dict(mahasiswa1="Dapupu", mahasiswa2="Bambang",
# # # # #                 mahasiswa3="Ucup", mahasiswa4="Otong")
# # # # # print(list_nama)

# # # # Film = {
# # # # "Avenger Endgame" : "Action",
# # # # "Sherlock Holmes" : "Mystery",
# # # # "The Conjuring" : "Horror"
# # # # }
# # # # #Sebelum Ditambah
# # # # print(Film)
# # # # Film["The Conjuring"] = "Comedy"
# # # # # Film.update({"Hours" : "Thriller"})
# # # # #Setelah Ditambah
# # # # print(Film)

# # # data = {
# # # "Nama" : "Daffa",
# # # "Umur" : 19,
# # # "Jurusan" : "Informatika"
# # # }

# # # #Sebelum Dihapus
# # # print(data)
# # # cache = data.pop("Nama")
# # # #Setelah dihapus
# # # print(cache)
# # # print(data)
# # # #memanggil data yang telah dihapus pada dictionary
# # # print(data.get("Nama"))
# # # #memanggil data yang telah dihapus pada variabel cache
# # # print(cache)

# # data = {
# #     "Nama" : "Daffa",
# #     "Umur" : 19,
# #     "Jurusan" : "Informatika"
# # }

# # print("Jumlah Data = ", len(data))

# buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# pinjam = buku.copy()
# pinjam['Buku2'] = "Anak Semua Bangsa"
# print(pinjam)
# print(buku)

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for penyanyi, album in Musik.items():
    print(f"Musik milik {penyanyi} adalah : ")
    print(album)
    print("")