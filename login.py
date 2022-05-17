kayitliKullanici="admin"
kayitliSifre="123456"
kullaniciAdi=input("Kullanıcı Adınızı Giriniz: ")
sifre=input("Şifrenizi Giriniz: ")
if(kayitliKullanici==kullaniciAdi and kayitliSifre==sifre): 
    print("Hoşgeldin %s!"%(kullaniciAdi))
else:   
    print("Kullanıcı Adı veya Şifre Hatalı!")
