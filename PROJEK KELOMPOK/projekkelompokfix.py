nama = input("Masukkan Nama Anda : ")

print('Hi,', nama)

kode_barang= input("Masukkan Kode Barang [AC/TV/KA/KK]")
merk= input("Masukkan merek : ")
jmlbrg= int(input("Masukkan Jumlah barang : "))

if      kode_barang=="K" or kode_barang=="k" :
        barang="KULKAS"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan=40
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan=50
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan=45
        else :
            harga_satuan=0  
elif     kode_barang=="MC" or kode_barang=="mc" :
        barang="MESIN CUCI"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan=20
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan=30
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan=25
        else :
            harga_satuan=0
elif     kode_barang=="TV" or kode_barang=="tv" :
        barang="TELEVISI"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan=35
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan=45
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan=40
        else :
            harga_satuan=0
elif     kode_barang=="AC" or kode_barang=="ac" :
        barang="PENDINGIN RUANGAN"
        if  merk=="LG" or merk=="Lg" or merk=="lg" :
            harga_satuan=30
        elif merk=="SAMSUNG" or merk=="Samsung" or merk=="samsung" :
            harga_satuan=40
        elif merk=="PANASONIC" or merk=="Panasonic" or merk=="panasonic" :
            harga_satuan=35
        else :
            harga_satuan=0
else :
    barang="ERROR"
    merk=="ERROR"
    harga_satuan=0