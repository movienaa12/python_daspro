import pandas as pd

def garis():
    print("--------------------------------------------")
    
nomor=[]
nominal=[]
hargajual=[]
harga=[]

a = (30/100)
b = (4/100)

ulang = 2

for i in range(ulang):
  print("Data Ke-"+str(i+1))
  nomor.append(input("Masukan Nomor Telepon : "))
  nominal.append((input("Masukan nominal : ")))

for i in range(ulang):
    total= harga + (harga*0.3)
    hargajual.append(total)

    if nominal[i] == 5 :
        harga = 5000*a
    elif nominal[i] == 10 :
        harga = 10000*a
    elif nominal[i] == 25 :
        harga = 25000*b
    elif nominal[i]== 50 :
        harga = 50000*b
    else :
        harga = 100000*b

data = {
    "NOMOR TLP" : nomor,
    "NOMINAL"   : nominal, 
    "HARGA"     : harga,
    }

datapulsa = pd.DataFrame(data)

garis()
garis()
print(datapulsa)
garis()
garis()