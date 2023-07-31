#input
nama=input("Masukkan nama Anda : ")

list_jumlah=[]
harga_satuan=[]
kode_barang=[]
merk=[]

ulang=2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_jumlah.append(int(input("Banyaknya barang : ")))
    kode_barang = input("Kode jenis barang [K/MC/TV/AC] : ")
    merk        = input("Nama merek : ")
    
if      kode_barang=="K" or kode_barang=="k" :
        barang="KULKAS"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan.append(40)
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan.append(50)
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan.append(45)
        else :
            harga_satuan.append=0  
elif     kode_barang=="MC" or kode_barang=="mc" :
        barang="MESIN CUCI"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan.append(20)
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan.append(30)
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan.append(25)
        else :
            harga_satuan.append(0)
elif     kode_barang=="TV" or kode_barang=="tv" :
        barang="TELEVISI"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan.append(35)
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan.append(45)
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan.append(40)
        else :
            harga_satuan.append(0)
elif     kode_barang=="AC" or kode_barang=="ac" :
        barang="PENDINGIN RUANGAN"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan.append(30)
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan.append(40)
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan.append(35)
        else :
            harga_satuan.append(0)
else :
    barang="ERROR"
    merk=="ERROR"
    harga_satuan.append(0)
    
jml_harga=list_jumlah*harga_satuan

#Pandas
import pandas as pd

#Dataframe
Data= {
    "Banyaknya"     : list_jumlah,
    "Jenis Barang"  : barang,
    "Merek"         : merk,
    "Harga Satuan"  : harga_satuan,
    "Jumlah Harga"  : jml_harga
  }    

data=pd.DataFrame(Data)

#Function
def garis():
  print("------------------------------------------")

#Output
garis()
print("Persediaan Barang Hari ini")
garis()
print("Nama Karyawan    : ",nama)
garis()
print(data)
garis()