#coding
#menggunakan kutip tunggal atau ganda pada nilai variable tanpa input
namakampus='Universitas Bina Sarana Informatika'
namakota="Kampus Karawang"
#akses semua nilai string
print(namakampus)
print(namakota)
#akses sebagian nilai string (tampilkan Universitas saja dari variable namakampus)
print(namakampus[:11])
#menggabung String
print(namakampus+namakota)
#menggabung String+menambah spasi antar variable
print(namakampus+" "+namakota)
#menghitung panjang string
print(len(namakampus))
print(len(namakota))
#karakter escape
print("Jl. Banten No.1 Karangpawitan \n Kab. Karawang")
#format (perataan)
print("|{:<50}|".format("Jl. Banten No.1 Karangpawitan Kab. Karawang"))
print("|{:^50}|".format("Jl. Banten No.1 Karangpawitan Kab. Karawang"))
print("|{:>50}|".format("Jl. Banten No.1 Karangpawitan Kab. Karawang"))
#input nilai variable Tipe data string
nim=input("masukkan NIM Anda : ")
nama=input("masukkan Nama Anda : ")
#Cara 1 input nilai variable Tipe data Integer
nilaitugas1=input("Masukkan Nilai Tugas 1 : ")
nilaitugas1=int(nilaitugas1)
#Cara 2 input nilai variable Tipe data Integer
nilaitugas2=int(input("Masukkan Nilai Tugas 2 : "))
#Operator Aritmatika pembagian--> kemungkinan menghasilkan nilai decimal (Float)
totaltugas=(nilaitugas1+nilaitugas2)/2
#cetak nim, nama, nilaitugas1, nilaitugas2 dan total tugas
print("Nim anda adalah : ",nim)
print("Nama anda adalah : ",nama)
print("Nilai Tugas 1 anda adalah : ",nilaitugas1)
print("Nilai Tugas 2 anda adalah : ",nilaitugas2)
print("Nilai Total Tugas anda adalah : ",totaltugas)
#konversi bil. decimal ke bil. bulat
print("membulatkan hasil total nilai tugas : ",int(totaltugas))