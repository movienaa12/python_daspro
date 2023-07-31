#input
nama            = input("Masukkan Nama Anda : ")
jabatan         = input("Masukkan Golongan Jabatan Anda [Golongan 1/2/3] : ")
pendidikan      = input("Masukkan pendidikan terakhir Anda [SMA/D1//D3/S1] : ")
jamker          = int(input("Masukkan jumlah jam kerja anda : "))

#proses

gaji = 300000

pg1 = (5/100)
pg2 = (10/100)
pg3 = (15/100)

pp1 = (2.5/100)
pp2 = (5/100)
pp3 = (20/100)
pp4 = (30/100)

honor_lembur = 3500

if      jabatan=="Golongan 1" or jabatan=="golongan 1" or jabatan=="1":
        tunjangan1=int(gaji*pg1)
elif    jabatan=="Golongan 2" or jabatan=="golongan 2" or jabatan=="2":
        tunjangan1=int(gaji*pg2)
elif    jabatan=="Golongan 3" or jabatan=="golongan 3" or jabatan=="3":
        tunjangan1=int(gaji*pg3)
else :
        tunjangan1=0

if      pendidikan=="SMA" or pendidikan=="sma":
        tunjangan2=int(gaji*pp1)
elif    pendidikan=="D1" or pendidikan=="d1":
        tunjangan2=int(gaji*pp2)
elif    pendidikan=="D3" or pendidikan=="d3":
        tunjangan2=int(gaji*pp3)
elif    pendidikan=="S1" or pendidikan=="s1":
        tunjangan2=int(gaji*pp4)
else :
        tunjangan2=0

if      jamker > 8 :
        lembur = jamker - 8
        tunjangan3=int(lembur*honor_lembur)
else :
        tunjangan3=0

total = tunjangan1+tunjangan2+tunjangan3+gaji

#Cetak Hasil

print("-------------------------------------")
print("Karyawan yang bernama        : "+nama)
print("Honor yang diterima..." )
print("Tunjangan Jabatan            : Rp" +str(tunjangan1))
print("Tunjangan Pendidikan         : Rp" +str(tunjangan2))
print("Honor Lembur                 : Rp" +str(tunjangan3))
print("Total Gaji                   : Rp" +str(total))