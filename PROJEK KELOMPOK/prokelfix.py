import pandas as pd

def garis():
    print("--------------------------------------------")
    
nomor=[]
nominal=[]
harga=[]

a = (30/100)
b = (3/100)

ulang = 2

for i in range(ulang):
  print("Data Ke-"+str(i+1))
  nomor.append(input("Masukan Nomor Telepon : "))
  nominal.append(input("Masukan nominal : "))


if nominal[i] == "5" :
        harga = (5000)
elif nominal[i] == "10" :
        harga = (10000)
elif nominal[i] == "25" :
        harga = (25000)
elif nominal[i]== "50" :
        harga = (50000)
else :
        harga = (100000)

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