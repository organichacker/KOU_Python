import os
yeni_dosya = os.open("C:\Python\Project\Deneme\odev (1).txt",os.O_RDWR)
yeni_dosya2 = os.open("Yeni_Dosyasi.txt",os.O_RDWR|os.O_CREAT)
istatistik = os.stat(yeni_dosya).st_size
icerik = os.read(yeni_dosya,istatistik)
icerik = icerik.decode()

sayi = ["1","2","3","4","5","6","7","8","9","0"]
for i in range(len(sayi)):
    icerik = icerik.replace(sayi[i],"")
icerik = icerik.replace("(","").replace(")","").replace("*","").replace("+","")
icerik = icerik.replace("?","").replace("-","").replace("=","")
os.write(yeni_dosya2,icerik.encode())
print(icerik)
os.close(yeni_dosya)
os.close(yeni_dosya2)
