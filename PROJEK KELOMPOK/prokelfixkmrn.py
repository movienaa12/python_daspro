import pandas as pd

def garis():
    print("--------------------------------------------")
    
nomor=[]
nominal=[]
harga=[]

ulang = 2

for i in range(ulang):
  print("Data Ke-"+str(i+1))
  nomor.append(input("Masukan Nomor Telepon : "))
  nominal.append(int(input("Masukan nominal : ")))
  harga.append(int(input("Masukkan harga : ")))

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