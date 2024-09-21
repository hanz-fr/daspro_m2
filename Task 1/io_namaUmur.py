from datetime import date

tgl_sekarang = date.today()

nama = input("Masukkan nama anda : ")
tahun_lahir = int(input("Tahun lahir : "))
tahun_sekarang = tgl_sekarang.year
umur = tahun_sekarang - tahun_lahir

print(f"Selamat datang {nama}, umur kamu {umur} tahun")