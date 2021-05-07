sayac = 0
liste = []
for i in range(5):
    a = int(input("Sayi:"))
    liste.append(a)
for r in liste:
    for j in range(2,r):
        if(r%j == 0):
            sayac += 1
        else:
            continue    
    if r == 1:
        print("{} sayısı asal değildir.".format(r))     
    elif r > 1 and sayac == 0:
        print("{} sayısı asaldır.".format(r))
    else:
        print("{} sayısı asal değildir.".format(r))
