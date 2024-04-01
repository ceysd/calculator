def toplama(x,y):
    return x + y
def çıkarma(x,y):
    return x - y
def bölme(x,y):
    if y != 0:
        return x / y
def çarpma(x,y):
    return x * y
def karesinialma(x):
    return x ** 2
def karekökünüalma(x):
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

son_işlem = None

try:

    while True:

        seçim = int(input("Yapmak istediğiniz işlem numarasını giriniz(1-9):                    Programdan çıkmak için 0'ı tuşlayınız."))

        if seçim == 1:
            soru1 = float(input("Toplama işlemi için ilk sayıyı giriniz:"))
            soru2 = float(input("Toplama işlemi için ikinci sayıyı giriniz:"))
            sonuç = toplama(soru1,soru2)
            print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 2:
            soru3 = float(input("Çıkarma işlemi için ilk sayıyı giriniz:"))
            soru4 = float(input("Çıkarma işlemi için ikinci sayıyı giriniz:"))
            sonuç = çıkarma(soru3,soru4)
            print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 3:
            soru5 = float(input("Bölme işlemi işlemi ilk sayıyı giriniz:"))
            soru6 = float(input("Bölme işlemi için ikinci sayıyı giriniz:"))
            if soru6 == 0:
                print("Bir sayıyı 0'a bölemezsiniz.")
                break
            else:
                sonuç = bölme(soru5,soru6)
            print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 4:
            soru7 = float(input("Çarpma işlemi için ilk sayıyı giriniz:"))
            soru8 = float(input("Çarpma işlemi için ikinci sayıyı giriniz:"))
            sonuç = çarpma(soru7,soru8)
            print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 5:
            soru9 = int(input("Karesini almak istediğiniz sayıyı giriniz:"))
            sonuç = karesinialma(soru9)
            print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 6:
            soru10 = float(input("Karekökünü hesaplamak istediğiniz sayıyı giriniz:"))
            if soru10 < 0:
                print("Negatif sayıların karekökü alınmaz.")
            elif soru10 == 0:
                print("0'ın karekökü alınmaz.")
            else:
                sonuç = karekökünüalma(soru10)
                print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 7:
            soru11 = float(input("Yüzdesini hesaplatmak istediğiniz sayıyı giriniz:"))
            soru12 = float(input("Seçtiğiniz sayının yüzde kaçını hesaplatmak istiyorsunuz:"))
            sonuç = yüzdehesaplama(soru11,soru12)
            print("Sonuç:", sonuç)
            son_işlem = sonuç
        elif seçim == 8:
            if son_işlem is not None:
                print("Son yapılan işlem:", son_işlem)
            else:
                print("Hafıza boş.")
        elif seçim == 9:
            son_işlem = None
            print("Hafıza sıfırlandı.")
        elif seçim == 0:
            print("Sistemden çıkış yapıldı.")
            break

    else:
        print("Hata olustu lütfen tekrar deneyiniz.")

except ValueError:
    print("Lütfen bir sayı değeri giriniz.")
except ZeroDivisionError:
    print("Bir sayıyı 0'a bölemezsiniz.")

