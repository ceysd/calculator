import time
import math
def toplama(x,y):
    return x + y
def çıkarma(x,y):
    return x - y
def bölme(x,y):
    if y == 0:
        print("Bir sayıyı 0'a bölemezsiniz!")
    else:
        return x / y
def çarpma(x,y):
    return x * y
def karesinialma(x):
    return x ** 2
def karekökünüalma(x):
    if x < 0:
        print("Negatif sayıların karekökü alınamaz!")
    else:
        return x ** 0.5
def yüzdehesaplama(x,y):
    return (x * y) / 100


ekran = """
(1) toplama
(2) çıkarma
(3) bölme
(4) çarpma
(5) karesini alma
(6) karekökünü alma
(7) yüzdesini hesaplama
(8) genel toplam
(9) hesap makinesini sıfırla
(0) çıkış"""

son_işlem = 0

print("\n*************************************** UYARI *************************************** \n")
print("\n  *** Son işlem üzerinden hesaplama yapmak isterseniz, ikinci sayiyi girmeden enter tuşuna basabilirsiniz! *** \n ")
print("\n******************************************************************************\n")

while True:
    try:
        
        print(ekran)
       
        seçim = int(input("Yapmak istediğiniz işlem numarasını giriniz(1-9) (Programdan çıkmak için 0'ı tuşlayınız.) : "))

        if seçim == 1:
            sayı1 = input("Toplama işlemi için ilk sayıyı giriniz:")
            sayı2 = input("Toplama işlemi için ikinci sayıyı giriniz:")

            if (sayı2.isnumeric()):
                sonuç = toplama(float(sayı1),float(sayı2))
                son_işlem = sonuç
            else:
                son_işlem += float(sayı1)


        elif seçim == 2:
            sayı3 = input("Çıkarma işlemi için ilk sayıyı giriniz:")
            sayı4 = input("Çıkarma işlemi için ikinci sayıyı giriniz:")

            if (sayı4.isnumeric()):
                sonuç = çıkarma(float(sayı3),float(sayı4))
                son_işlem = sonuç
            else:
                son_işlem -= float(sayı3)

        elif seçim == 3:
            sayı5 = input("Bölme işlemi işlemi ilk sayıyı giriniz:")
            sayı6 = input("Bölme işlemi için ikinci sayıyı giriniz:")

            if (sayı6.isnumeric()):
                
                if float(sayı6) == 0:
                    print("Bir sayıyı 0'a bölemezsiniz.")
                    continue
                else:
                    sonuç = bölme(float(sayı5),float(sayı6))
            else:
                son_işlem /= float(sayı5)
        
            
        elif seçim == 4:
            sayı7 = input("Çarpma işlemi için ilk sayıyı giriniz:")
            sayı8 = input("Çarpma işlemi için ikinci sayıyı giriniz:")

            if (sayı8.isnumeric()):
                sonuç = çarpma(float(sayı7),float(sayı8))
                son_işlem = sonuç

            else:
                son_işlem *= float(sayı7)

        elif seçim == 5:
            sayı9 = int(input("Karesini almak istediğiniz sayıyı giriniz:"))
            sonuç = karesinialma(sayı9)
            son_işlem = sonuç

        elif seçim == 6:
            sayı10 = float(input("Karekökünü hesaplamak istediğiniz sayıyı giriniz:"))
            if sayı10 < 0:
                print("Negatif sayıların karekökü alınmaz.")
            elif sayı10 == 0:
                print("0'ın karekökü alınmaz.")
            else:
                sonuç = karekökünüalma(sayı10)
            son_işlem = sonuç

        elif seçim == 7:
            sayı11 = float(input("Yüzdesini hesaplatmak istediğiniz sayıyı giriniz:"))
            sayı12 = float(input("Seçtiğiniz sayının yüzde kaçını hesaplatmak istiyorsunuz:"))
            sonuç = yüzdehesaplama(sayı11,sayı12)
            son_işlem = sonuç
            
        elif seçim == 8:
            if son_işlem == 0:
                print("Hafıza boş")
            else:
                print(son_işlem)
            
            
        elif seçim == 9:
            son_işlem = 0
            print("Hafıza sıfırlandı.")
            
        elif seçim == 0:
            print("Sistemden çıkış yapılıyor...")
            time.sleep(1)
            print( "\nSistemden çıkış yapıldı.")
            break
    
        else:
            print("Hata olustu lütfen tekrar deneyiniz.")

        print("\n **** \n İşlem Sonucu:", son_işlem, "\n ****")

    except ValueError:
        print("Bilinmeyen karakter girildi! Lütfen girdiğiniz sayıları kontrol edin! ")
    
