import pandas as pd

def garis():
  print("------------------------------------------")

list_jumlah=[]
list_barang=[]
list_merk=[]
list_satuan=[]

#input

nama=input("Masukkan nama Anda : ")

ulang=2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_jumlah.append(int(input("Banyaknya barang : ")))
    list_barang.append(input("Jenis barang :"))
    list_merk.append(input("Nama merek :"))
    list_satuan.append(int(input("Harga satuan :")))
  
jml_harga = list_jumlah.append*list_satuan.append

#Dataframe
Data= {
    "Banyaknya" : list_jumlah,
    "Jenis Barang" : list_barang,
    "Merek" : list_merk,
    "Harga Satuan" : list_satuan,
    "Jumlah Harga" : jml_harga,
  }    

data=pd.DataFrame(Data)

#Cetak
garis()
print("Persediaan Barang Hari ini")
garis()
print("Nama          : ",nama)
garis()
print(data)
garis()