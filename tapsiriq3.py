# Tapşırıq 1: İstifadəçinin yaşı
# Bir istifadəçidən yaşını soruşan bir proqram yazın. if, elif, və else operatorları vasitəsilə aşağıdakı qaydalara əsasən mesajlar göstərin:

# Əgər yaş 18-dən kiçikdirsə, "Siz hələ azyaşlısınız" mesajı verilsin.
# Əgər yaş 18-dən böyük və ya bərabərdirsə, amma 65-dən kiçikdirsə, "Siz yetkinsiniz" mesajı verilsin.
# Əgər yaş 65-dən böyük və ya bərabərdirsə, "Siz təqaüdçüsünüz" mesajı verilsin.
# İstifadəçinin yaşını soruş
yas =int(input("yasinizi qeyd edin:"))
if yas<18:
    print("sizin hele azyaslisiniz")
elif 18 <=yas <65:
    print("siz yetkinsiniz")
else :
    print("siz teqaudcusunuz")

# Tapşırıq 2: İmtahan nəticəsi
# İstifadəçidən imtahan balını soruşan proqram yazın. if, elif, və else ilə aşağıdakı kriteriyalara əsasən qiymətləndirin:
# 90 və daha yuxarı bal: "A" qiyməti.
# 80-dən 89-a qədər bal: "B" qiyməti.
# 70-dən 79-a qədər bal: "C" qiyməti.
# 60-dan 69-a qədər bal: "D" qiyməti.
# 60-dan aşağı bal: "F" qiyməti.
bal=int(input("imtahanda yigilan bal:"))
if 90<=bal<=100:
    print("A")
elif 80<bal<=89:
    print("B")
elif 70<bal<=79:
    print("C")
elif 60<bal<=69:
    print("D")
elif 50<bal<69:
    print("F")
elif 0<bal<=49:
    print("kesilmisiz")
else:
    print("bu qeder bal yigmaq olmur")

#Tapşırıq 3: Havanın temperaturu
# İstifadəçidən havanın temperaturunu soruşan bir proqram yazın və bu məlumatlara əsaslanaraq mesaj göstərin:
# Temperatur 0-dan azdırsa, "Çox soyuqdur" mesajı verin.
# Temperatur 0 ilə 20 arasında olarsa, "Sərin hava" mesajı verin.
# Temperatur 20 ilə 30 arasında olarsa, "Mülayim hava" mesajı verin.
# Temperatur 30-dan böyükdürsə, "Çox istidir" mesajı verin.
Tempratur=int(input("havanin tempratur:"))
if Tempratur<0:
    print("cox soyuqdur")
elif 0<Tempratur<20:
    print("serin hava hiss olunur")
elif 20<Tempratur<30:
    print("mulayim hava")
else :
    print("cox istidir") 


#Tapşırıq 4: Ədədin müsbət və mənfiliyini yoxlama
# İstifadəçidən bir ədəd daxil etməsini tələb edən proqram yazın və if, elif, else ilə aşağıdakıları yoxlayın:
# Əgər ədəd müsbətdirsə, "Ədəd müsbətdir" mesajını verin.
# Əgər ədəd mənfidirsə, "Ədəd mənfidir" mesajını verin.
# Əgər ədəd sıfırdırsa, "Ədəd sıfırdır" mesajını verin.
yoxlama=int(input("bir eded elave edin:"))
if yoxlama>0:
    print("bu musbet ededdir")
elif yoxlama==0:
    print("eded '0'-dir")
else:
    print("eded menfidir")


#Tapşırıq 5: İstifadəçi adı və parol
# İstifadəçidən istifadəçi adı və parol daxil etməsini tələb edən proqram yazın. Şərtlər aşağıdakı kimidir:

# Əgər istifadəçi adı "admin" və parol "12345" olarsa, "Sistemə uğurla daxil oldunuz" mesajı verilsin.
# Əgər istifadəçi adı səhv olarsa, "İstifadəçi adı yanlışdır" mesajı verilsin.
# Əgər parol səhv olarsa, "Parol yanlışdır" mesajı verilsin.
isdifadeci_adi=input("istifadece adiniz:")
parol=input("parol daxil edin")
if isdifadeci_adi=="admin" and parol=="12345":
    print("ugurlua daxil oldunuz")
elif isdifadeci_adi!="admin":
    print("isdifadeci adiniz sehvdir")
elif parol!="12345":
    print("parolunuz yalnisdir")
else:
    print("her ikisi yalnisdir")

#Tapşırıq 6: İstifadəçi seçimləri
# Bir proqram yazın, istifadəçiyə menyu təqdim edin və istifadəçinin seçiminə uyğun mesaj göstərin:
# 1 seçilirsə, "Menyu 1 seçildi" mesajı verilsin.
# 2 seçilirsə, "Menyu 2 seçildi" mesajı verilsin.
# 3 seçilirsə, "Menyu 3 seçildi" mesajı verilsin.
# Əgər başqa bir ədəd daxil edilərsə, "Yanlış seçim" mesajı verilsin.
menyu1="menyu1"
menyu2="menyu2"
menyu3="menyu3"
print("menyu1", "\nmenyu2","\nmenyu3") 
secim=int(input("hansi menyunu secirsiz?:"))
if secim==1:
    print("siz 1. menyunu secdiniz")
elif secim==2:
    print("siz 2 ci menyunu secdiniz")
elif secim==3:
    print("siz 3. menyunu secdiz")
else:
    print("bele bir menyu novu yoxdur")

#Tapşırıq 7: Həftə günləri
# Bir proqram yazın, istifadəçidən həftənin günlərini təmsil edən bir ədəd daxil etməsini tələb edin və bu ədədə uyğun həftə gününü göstərin. Məsələn:
# 1 daxil edilərsə, "Bazar ertəsi"
# 2 daxil edilərsə, "Çərşənbə axşamı"
# 7 daxil edilərsə, "Bazar"
# Əgər 1-dən 7-yə qədər bir rəqəm daxil edilməzsə, "Yanlış rəqəm" mesajı verilsin.
hefte=int(input("heftenin her hansi bir gunun daxil edin:"))
if hefte==1:
    print("Bazar ertesi")
elif hefte==2:
    print("cersenbe axsami")
elif hefte==3:
    print("cersenbe")
elif hefte==4:
    print("cume axsami")
elif hefte==5:
    print("cume")
elif hefte==6:
    print("senbe")
elif hefte==7:
    print("Bazar")
else:
    print("zehmet olmazsa dogru reqem")


#Tapşırıq 8: Müddəti təyin etmə
# İstifadəçidən saatı və dəqiqəni daxil etməsini tələb edən bir proqram yazın və şərtlərə əsasən günün hansı hissəsini göstərsin:
# Əgər saat 6 ilə 12 arasındadırsa, "Səhər" mesajı verilsin.
# Əgər saat 12 ilə 18 arasındadırsa, "Günorta" mesajı verilsin.
# Əgər saat 18 ilə 24 arasındadırsa, "Axşam" mesajı verilsin.
# Əgər saat 0 ilə 6 arasındadırsa, "Gecə" mesajı verilsin.
saat=int(input("saat:"))
deqiqe=int(input("deqiqe:"))
if 6<=saat<12:
    print("seher")
elif 12<=saat<18 :
    print("gunorta")
elif 18<=saat<24:
    print("axsam")
elif 0<=saat<6:
    print("gece")
else:
    print("duzgun daxiledin")