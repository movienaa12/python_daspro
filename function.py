import pandas as pd
#fungsi garis
def garis():
  print("****************************************************")

#variable yg berulang menggunakan List/matriks
list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]
list_grade=[]
list_keterangan=[]

namadosen=input("Masukkan Nama Dosen : ")
kelas=input("masukkan Kelas : ")
mk=input("Matakuliah :")


ulang=2
for i in range(ulang):
    print ("data Ke - " + str(i+1))
    list_nim.append(input("Masukkan Nim anda : "))
    list_uts.append(int(input("Masukkan Nilai UTS anda :")))
    list_uas.append(int(input("Masukkan Nilai UAS : ")))

#proses
for i in range(ulang):
    total=(list_uas[i] + list_uts[i]) / 2
    list_total.append(total)

    if list_total[i]>= 80:
        list_grade.append("A")
        list_keterangan.append("Lulus")
    else:
        list_grade.append("B")
        list_keterangan.append("Gagal")
    
#membuat Dataframe
Data= {
    "Nim" : list_nim,
    "Nilai UTS" : list_uts,
    "Nilai UAS" : list_uas,
    "Total" : list_total,
    "Grade" : list_grade,
    "Keterangan" : list_keterangan
    }    

datanilai=pd.DataFrame(Data)
#Cetak
print("Nama Dosen : ", namadosen)
print("Kelas      : ",kelas)
print("Matakuliah : ",mk)
garis()
print("Daftar Nilai")
garis()
print(datanilai)
garis()