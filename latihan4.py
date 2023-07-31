#input
nama            = input("Masukkan Nama Anda : ")
nis             = input("Masukkan NIS Anda : ")
kode_jurusan    = input("Masukkan Kode Jurusan yang akan Anda pilih [SI/SIA] : " )

#proses
if kode_jurusan=="SI" :
    nama_jurusan="Sistem Informasi"
    harga=2400000
elif kode_jurusan=="SIA" :
    nama_jurusan="Sistem Informasi Akuntansi"
    harga=2000000
else :
    nama_jurusan="Kode yang anda masukkan salah"
    harga=0

#Cetak Hasil
print("------------------------------------")
print(" PENDAFTARAN MAHASISWA ")
print(" BARU ")
print("------------------------------------")
print("Nama Anda                    : "+(nama))
print("NIS                          : "+(nis))
print("Kode Jurusan yang dipilih    : "+(kode_jurusan))
print("Jurusan yang dipilih         : "+(nama_jurusan))
print("Harga                        : Rp"+str(harga))