import pandas as pd
#fungsi garis
def garis():
  print("****************************************************")

#variable yg berulang menggunakan List/matriks
list_nomor=[]
list_nominal=[]
list_total=[]
harga=[]

tanggal=input("Masukkan tanggal : ")

ulang=2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nomor.append(input("Masukkan nomor anda : "))
    list_nominal.append(int(input("Masukkan nominal :")))

if list_nominal== 5 :
    harga(5000)
elif list_nominal== 10 :
    harga(10000)
else :
    harga(0)


#proses
for i in range(ulang):
    total=harga + 1500
    list_total.append(total)

    
#membuat Dataframe
Data= {
    "Nomor" : list_nomor,
    "Nominal" : list_nominal,
    "Total" : list_total,
    "Harga" : harga
    }    

datanilai=pd.DataFrame(Data)
#Cetak

garis()
print("Data hari ini, " ,tanggal)
garis()
print(datanilai)
garis()