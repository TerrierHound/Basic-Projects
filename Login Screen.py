print("Welcome to Heaven !!!")

Kullanici_adi = "John"
Parola = "johndoe123"

Gecerli_Kullanici = input("Kullanici adi: ")
Gecerli_Parola = input("Parola: ")

if Gecerli_Kullanici == Kullanici_adi and Gecerli_Parola == Parola:
    print("Girdiginiz bilgiler gereçlidir. Giriş yaptınız ! Tebrikler !")
else:
    print("Kullanici adi veya Parola yanlış")