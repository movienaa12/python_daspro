jamker          = int(input("Masukkan jumlah jam kerja anda : "))
t3              = 3500

if  jamker>8 :
    lembur= jamker - 8
    tunjangan3=str(lembur*t3)

print("Honor Lembur                 : " +str(tunjangan3))