yonetici = 'recep camdali'
calisansayisi= 0
yoneticiSayisi = 0

sirketCalisanlari = ['furkan camdali','muhittin camdali','recep camdali']
for calisan in sirketCalisanlari:
    calisansayisi +=1
    ad, soyad = calisan.split()[0], calisan.split()[1]

    if calisan == yonetici:
        yoneticiSayisi+=1
        print('{0}. yoneticinin adi {1} ve Soyadi {2}'.format(yoneticiSayisi,ad,soyad))
    else:
        print('{0}. calisanin adi {1} ve Soyadi {2}'.format(calisansayisi,ad,soyad))





