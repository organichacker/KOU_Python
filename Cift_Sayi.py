sayi = float(input("Sayıyı Giriniz: "))
if sayi % 2 == 0:
    if sayi > 0:
        print("{} sayısı çift sayıdır.".format(sayi))
    else:
        print("{} sayısı tek sayıdır.".format(sayi))
