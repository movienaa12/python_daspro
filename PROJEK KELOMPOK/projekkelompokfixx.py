import pandas as pd

def garis():
    print("=======================================================")

nomor=[]
operator=[]
kd_nominal=[]
nominal=[]
harga=[]

ulang = 2

for i in range(ulang):
  print("Data Ke-"+str(i+1))
  nomor.append(input("Masukan Nomor Telepon : "))
  operator.append(input("Masukan operator : "))
  kd_nominal.append(int(input("Masukan nominal : ")))

for i in range(ulang) :
    if kd_nominal[i] == 5 :
        nominal.append(5000)
        harga.append(6500)
    elif kd_nominal[i] == 10 :
        nominal.append(10000)
        harga.append(11500)
    elif kd_nominal[i] == 25 :
        nominal.append(25000)
        harga.append(27000)
    elif kd_nominal[i]== 50 :
        nominal.append(50000)
        harga.append(52000)
    else :
        nominal.append(100000)
        harga.append(103000)

import time

localtime=time.asctime(time.localtime(time.time()))

data = {
    "NOMOR TLP"     : nomor,
    "OPERATOR"      : operator,
    "KODE NOMINAL"  : kd_nominal,
    "NOMINAL"       : nominal,
    "HARGA"         : harga
    }

datapulsa = pd.DataFrame(data)

garis()
print("Data hari ini, " ,localtime)
garis()
print(datapulsa)
garis()