import modulfathan

#input
kodebarang = input("Masukkan Kode Barang [B01/B02] : ")
jmlbeli    = int(input("Masukkan Jumlah Beli : "))

if kodebarang   == "B01" or kodebarang == "b01" :
    kodebarang  = "B01"
    nama        = "Tas"
    harga       = 150000
elif kodebarang == "B02" or kodebarang == "b02" :
    kodebarang  = "B02"
    nama        = "Sepatu"
    harga       = 200000
else :
    kodebarang  = "ERROR"
    nama        = "ERROR"
    harga       = 0

totalharga = harga*jmlbeli

if totalharga >= 500000 :
    diskon = totalharga*0.2
else :
    diskon = 0

totalbayar = totalharga-diskon

#output
modulfathan.garis()
print("Data Penjualan")
modulfathan.garis()
print("Kode barang Anda adalah   : ",kodebarang)
print("Nama Barang               : " ,nama)
print("Jumlah beli               : " ,jmlbeli)
print("Total                     : Rp." ,int(totalharga))
print("Diskon                    : Rp." ,diskon)
modulfathan.garis()
print("Total bayar               : Rp." ,totalbayar)
uangbayar = int(input("Uang yang Anda bayarkan   : Rp. "))
print("Uang kembali              : Rp." ,modulfathan.kembalian(totalbayar,uangbayar))