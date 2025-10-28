# # # # # # # def perkenalan():
# # # # # # #     print("Halo aku Ridho")

# # # # # # # perkenalan()

# # # # # # def salam():
# # # # # #     print ('Halo, Ridho')
# # # # # # def kali():
# # # # # #     x = 5*5
# # # # # #     print(x)

# # # # # # salam()
# # # # # # salam()
# # # # # # salam()
# # # # # # kali()
# # # # # # kali()
# # # # # # kali()

# # # # # def luas_persegi_panjang(panjang, lebar):
# # # # # luas = panjang * lebar
# # # # # print ('luas persegi panjang adalah ', luas)

# # # # # luas_persegi_panjang(4, 5)

# # # # def luas_persegi(sisi):
# # # #     luas = sisi * sisi
# # # #     return luas

# # # # print ('Luas persegi :', luas_persegi(8))

# # # Nama1 = "Hambali"
# # # Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # # def info():
# # #     Nama = "Informatika"
# # #     Mata_Kuliah1 = "Logika Informatika"
# # #     print("Prodi:", Nama)
# # #     print("Mata Kuliah:", Mata_Kuliah)

# # # print(Mata_Kuliah)
# # # info()

# # def faktorial(n):
# #     if n == 1 or n == 0:
# #          return 1

# #     else:
# #         return n * faktorial(n - 1)

# # hasil = faktorial(5)
# # print(f"Hasil dari 5! adalah: {hasil}")

# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(film)):
#         print(indeks, "|", film[indeks])
    
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")

# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
# menu = input("PILIH MENU> ")
# print ("\n")

# if menu == "1":
#     show_data()
# elif menu == "2":
#     insert_data()
# elif menu == "3":
#     edit_data()
# elif menu == "4":
#     delete_data()
# elif menu == "5":
#     exit()
# else:
#     print ("Salah pilih!")

# angka = int(input('Masukkan Angka : '))
# print(angka) #input 'Hai'

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')
# finally :
#     print('Blok Try Selesai')

try:
    usn = input('Username yang diinginkan : ')
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)   