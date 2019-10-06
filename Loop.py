giriş = """

(1)topla
(2)çıkar
(3)çarp
(4)böl
(5)karesini hesapla
(6)karekököünü al

"""
print(giriş)

anahtar = 1

while anahtar == 1:
    soru = input("Lutfen yapmak istediğiniz işlemi seçiniz: (cıkmak için q ya basınız): ")
    
    if soru == "q":
        print("Çıkış yaptınız")
        anahtar = 0 
    
    elif soru == "1":
        sayi1 = int(input("Toplama işlemi için ilk sayiyi giriniz: "))
        sayi2 = int(input("Toplama işlemi için ikinci sayiyi giriniz: "))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2 )

    elif soru == "2":
        sayi3 = int(input("Çıkarma işlemi için sayi giriniz: "))
        sayi4 = int(input("Çıkarma işlemi için diğer sayiyi giriniz: "))
        print(sayi3, "-", sayi4, "=", sayi3 - sayi4 )

    elif soru == "3":
        sayi5 = int(input("Çarpma işlemi için sayi giriniz: "))
        sayi6 = int(input("Çarpma işlemi için ikinci sayiyi giriniz: "))
        print(sayi5, "x", sayi6, "=", sayi5 * sayi6 )   

    elif soru == "4":
        sayi7 = int(input("Bolme işlemi için sayi giriniz: "))
        sayi8 = int(input("Bolme işlemi için ikinci sayiyi giriniz: "))
        print(sayi7, "/", sayi8, "=", sayi7 / sayi8 )

    elif soru == "5":
        sayi9 = int(input("Karesini almak istediginiz sayiyi giriniz: "))
        print(sayi9, "sayinin karesi:", sayi9 ** 2)

    elif soru == "6":
        sayi10 = int(input("Karekokunu almak istediginiz sayiyi giriniz: "))
        print(sayi10, "Sayinin karekökü:", sayi10 ** 0.5)

    else:
          print("Yanliş giriş") 
          print("Lütfen aşağıdaki seçeneklerden giriniz: ", giriş )  