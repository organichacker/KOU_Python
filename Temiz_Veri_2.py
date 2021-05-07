def TemizVeri():
    ilk_string = "Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string = "Ha3K5a1n"
    Birlesmis_Deger = (ilk_string.replace("5", "").replace("4","")).capitalize() + "-" + (ikinci_string.replace("9", "").replace("4","")).capitalize() + "-" + (ucuncu_string.replace("3", "").replace("5", "").replace("1","")).capitalize()
    return Birlesmis_Deger
print(TemizVeri())
