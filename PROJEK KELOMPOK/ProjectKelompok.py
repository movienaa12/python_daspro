import pandas as pd

nama = []
jumlah = []
harga = []
totalharga = []

ulang = 2
for i in range (ulang) :
    print("Data Barang Ke - : "+str(i+1))
    nama.append(input("Masukkan Nama Barang : "))
    jumlah.append(int(input("Masukkan Jumlah Barang : ")))
    harga.append(int(input("Harga Barang : ")))

for i in range (ulang) :
    if nama[i] == "KULKAS 2 PINTU" :
        harga.append(1000000)

    elif nama[i] == "Televisi LED" :
        harga.append(3000000)
    else : 
        nama[i] == "AC"
        harga.append(3500000)
    
for i in range(ulang) :
    totalharga.append((harga[i]*jumlah[i]))


data = {
    "NAMA BARANG" : nama,
    "JUMLAH BARANG" : jumlah,
    "HARGA" : harga,
    "TOTAL" : totalharga,
}

databarang = pd.DataFrame(data)

def garis () :
    print("=====================================================")



garis()
print("DATA PERSEDIAAN BARANG ELEKTRONIK")
garis()
garis()
print(databarang)
garis()
garis()
garis()