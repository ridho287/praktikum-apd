print("Customer ingin membeli laptop di toko elektronik")
print("Masukkan nama")
nama = input()
print("Masukkan nim")
nim = int(input())
print("Pilih laptop apa yang mau dibeli")
print("1.Acer")
print("2.Asus")
print("3.Lenovo")
print("Masukkan harga laptop")
hargaLaptop = int(input())
diskonAcer = hargaLaptop * float(5) / 100
diskonAsus = hargaLaptop * float(7) / 100
diskonLenovo = hargaLaptop * float(10) / 100
hargaAkhirAcer = hargaLaptop - diskonAcer
hargaAkhirAsus = hargaLaptop - diskonAsus
hargaAkhirLenovo = hargaLaptop - diskonLenovo
print("Selamat datang customer " + nama + " dengan nim " + str(nim) + " anda ingin cari laptop apa? ")
print("Ini harga laptop Acer setelah diskon " + str(hargaAkhirAcer))
print("Ini harga laptop Asus setelah diskon " + str(hargaAkhirAsus))
print("Ini harga laptop Lenovo setelah diskon " + str(hargaAkhirLenovo))