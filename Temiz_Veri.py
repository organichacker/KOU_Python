def TemizVeri():
    ilk_string = "Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string = "Ha3K5a1n"
    sayilar = ["1","2","3","4","5","6","7","8","9","0"]
    Birlesmis_Deger = ""
    Birlesmis_Deger2 = []
    for i in ilk_string:
        if i in sayilar:
            continue
        print(i,end="") 
    print("-",end="")
    for j in ikinci_string:
        if j in sayilar:
            continue
        print(j,end="")
    print("-",end="")
    for k in ucuncu_string:
        if k in sayilar:
            continue
        print(k,end="")
    print("\n")

    return Birlesmis_Deger

TemizVeri()
