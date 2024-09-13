#Tapşırıq 1: split() və join() metodları
m="menimadimMurshuddur  MenSumqayitdayasayiram Menim30yasimvar"
n=m.split()
print(n)
r=".".join(n)
print(r)

#Tapşırıq 2: strip(), lstrip(), rstrip() metodları
txt="       bu ay az vaxdim olsada        calisiram dersleri oturmeyim            "
txt_=txt.strip()
txt1=txt.lstrip()
txt2=txt.rstrip()
print(txt_)
print(txt1)
print(txt2)

#Tapşırıq 3: find() və count() metodları
find="find metodun ile tapsiriq"
print(find.find("i", 3, 17 ))
print(find.count("i"))


#Tapşırıq 4: startswith() və endswith() metodları
startswith="startswith ve endswith metodlarin mohkemledek"
print(startswith.startswith("art", 2 , 20))
print(startswith.endswith("metodlarin mohkemledek"))


#Tapşırıq 7: capitalize(), title(), və swapcase() metodları
ta="capitalize , Title , SWAPACSE"
print(ta.capitalize())
print(ta.swapcase())
print(ta.title())


#Tapşırıq 1: append(), extend(), və insert() metodları
app=['Append , extend ']
app.append("insert")
print(app)
appp=["Append ", "Extend", "insert"]
appp.insert(1,"Murshudmetod")
print(appp)
ad=['append', 'extend', 'insert']
add=["men",  "sen"]
ad.extend(add)
print(ad)


#Məsələ: Başlanğıc list-i [1, 2, 3] olaraq yaradın.Sonra:
#append() metodu ilə sona 4 əlavə edin.
#extend() metodu ilə sona [5, 6] əlavə edin.
#insert() metodu ilə 0 indeksinə 0 əlavə edin.
mes=[1,2,3]
mes.append(4)
me=[5,6]
mes.extend(me)
mes.insert(0, 0)
print(mes)


#Tapşırıq 2: remove(), pop(), və clear() metodları
az=['baki', 'ismayilli', 'samaxi', 'tovuz', 'gence']
az1=['baki', 'ismayilli', 'samaxi', 'tovuz', 'gence']
az2=['baki', 'ismayilli', 'samaxi', 'tovuz', 'gence']
print(az.clear())
az1.remove('baki')
print(az1)
az2.pop()
print(az2.pop(1))

#Məsələ: Başlanğıc list-i ["alma", "banan", "portağal", "alma"] olaraq yaradın. Sonra:
#remove() metodu ilə alma elementinin birincisini silin.
#pop() metodu ilə sonuncu elementi silin.
#clear() metodu ilə list-i tamamilə boşaldın.
mesele=["alma", "banan", "portagal", "alma"]
#mesele.remove("alma")
#print(mesele)
#mesele.pop(3)
#print(mesele)
print(mesele.clear())

#Tapşırıq 3: copy() və slice metodu ilə list-i kopyalamaq və bir hissəsini əldə etmək
#Bir list yaradın və onu kopyalayın. Kopyalanan list-dən müəyyən bir hissəni çıxarmaq üçün slicing (dilimləmə) istifadə edin.
#Nəticədə dəyişdirilmiş list-ləri ekrana çıxarın.
t=[1,2,3,4,5,6,7,8,]
d=t.copy()
print(d)
print(d[:3])
print(t[-6:4])

#Tapşırıq 1: update(), setdefault() metodları və Nested Dictionaries
set={"bmw":"e61", "mercedes":"111", "audi":"rs6", "honda":"cvic"}
set.update({"honda":"accord"})
print(set)
x=set.setdefault("bmw")
print(x)
sem={
    "Ali":"math", "qiymet":"85" ,
    "Cefer":"math","qiymet":"88",
    }
sem.update({"qiymet":"90",})
print(sem)
#cef=sem.setdefault{
    #"Ali":"math", "qiymet":"85",
    #"Cefer":"math", "qiymet":"88",
    #"cefer":"chemistry","qiyme":"76"}

#Tapşırıq 2: pop(), popitem(), və del metodu ilə elementləri silmək
mehsul={
    "alma": 1,
    "alca": 5,
    "badam": 15.8,
    "armud": 2.5,
}
mehsul.pop("alma")
print(mehsul)
xx=mehsul.popitem()
print(xx)
del mehsul ["alca"]
print(mehsul)

# Başlanğıc dictionary-ni {"alma": 1.5, "banan": 0.9, "portağal": 1.2, "armud": 2.0} olaraq yaradın.
# pop() metodu ilə "alma" məhsulunu silin və silinən məhsulun qiymətini ekrana çıxarın.
# popitem() metodu ilə sonuncu elementi silin və ekrana çıxarın.
# del metodu ilə "banan" məhsulunu silin.
pop={"alma": 1.5, "banan": 0.9, "portağal": 1.2, "armud": 2.0}
# pop.pop("alma")
# print(pop)
print(pop.pop("alma"))
popitem=pop.popitem()
print(popitem)
del pop ["banan"]
print(pop)

# Tapşırıq 3: keys(), values(), və items() metodları ilə açarları, dəyərləri və cütləri əldə etmək
# Bir dictionary yaradın və ona bir neçə kitab və onların müəlliflərini daxil edin.
# Bu dictionary-dən keys(), values(), və items() metodları ilə məlumatları çıxarın və ekrana çıxarın.
key={
    "Elxan E": "Elekecmez yaquar" ,
    "Cek London": "Martin Iden" ,
    "Ilyas Efendiyev": "Soyudlu arx",
    "Elxan Elatli": "Qan lekesi"
}
values=key.values()
keys=key.keys()
items=key.items()
# print(items)
# print(values)
# print(keys)
print("values", values, "\nkeys", keys, "\nitems", items)

# Başlanğıc dictionary-ni {"Dəli Kür": "İsmayıl Şıxlı", "Əli və Nino": "Qurban Səid", "Yeddi Gözəl": "Nizami Gəncəvi"} olaraq yaradın.
# keys() metodu ilə bütün kitab adlarını ekrana çıxarın.
# values() metodu ilə bütün müəllif adlarını ekrana çıxarın.
# items() metodu ilə hər bir kitab-müəllif cütünü ekrana çıxarın.
kitab={
    "Deli Kur": "Ismayil Sixli",
    "Eli ve Nino": "Qurban Seid",
    "Yeddi Gozel": "Nizami Gencevi"
}
kitab_a=kitab.keys()
muellifler=kitab.values()
kitab_muellif=kitab.items()
print("kitab_a" , kitab_a, "\nmuellifler", muellifler, "\nkitab_muellif", kitab_muellif)
#print(kitab_a)
#print(muellifler)
#print(kitab_muellif)


# Tapşırıq 4: List-ləri dəyərlər kimi istifadə edərək Dictionary yaratmaq
# Bir neçə tələbənin adını və onların aldığı qiymətləri bir dictionary-də saxlayın. 
# Daha sonra bu dictionary-də hər bir tələbənin qiymətlərinin ortalamasını tapın və ekrana çıxarın.
telebe={"Tural": [90, 85, 78],
        "Aytca": [95, 88, 92],
        "Vusal": [70, 80, 65] }
Tural=sum(telebe["Tural"])
Tural_=len(telebe["Tural"])
ortalama=Tural/Tural_
print(ortalama)
print(sum(telebe["Aytca"])/len(telebe["Aytca"]))
print(sum(telebe["Vusal"])/len(telebe["Vusal"]))

# Tuples
# Tapşırıq 1: Tuple içərisində Nested Tuples yaratmaq və onlarla işləmək
# Bir tuple yaradın və daxilində nested tuples saxlayın.
# Daha sonra bu nested tuples-lərdə olan məlumatlarla işləyin.
# Başlanğıc tuple-i ((1, 2, 3), ("a", "b", "c"), (True, False, True)) olaraq yaradın.
# Bu tuple-dən hər bir nested tuple-i çıxarın və fərqli dəyişənlərə təyin edin.
# İkinci nested tuple-dəki "b" elementinin indeksini tapın.
# Üçüncü nested tuple-dəki True dəyərlərinin sayını tapın.
tuplee=((1, 2, 3) ,("a","b","c"), (True, False, True))
reqemler=tuplee[0]
abc=tuplee[1]
boolens=tuplee[2]
print("reqemler", reqemler , "\nabc" , abc , "\nboolens" , boolens)
print(abc.index("b"))
print(boolens.count(True))

# Tapşırıq 2: Tuple-ləri bir-biri ilə birləşdirmək və yeni tuple yaratmaq
# İki fərqli tuple yaradın və onları bir-biri ilə birləşdirin. Birləşdirilmiş tuple-də müəyyən bir hissəni çıxarın
# və yeni bir tuple yaradın.
birincituple=(1,2,3)
ikincituple=(6,5,4)
birlesmis=birincituple+ikincituple
birlesmis_list=list(birlesmis)
silinen=birlesmis_list[2:]
print(birlesmis)
print(birlesmis_list)
print(sorted(birlesmis_list))
print(silinen)

# Məsələ:
# Başlanğıc tuple-ləri (1, 2, 3) və ("a", "b", "c") olaraq yaradın.
# Bu iki tuple-i birləşdirin.
# Birləşdirilmiş tuple-dən son 3 elementi çıxarın və yeni bir tuple yaradın.

tuple1=(1,2,3)
tuplea=("a","b","c")
tuple1a=tuple1+tuplea
azs=tuple1a[:3]
print(azs)

# Məsələ:
# Başlanğıc tuple-i (5, 3, 1, 4, 2) olaraq yaradın.
# Bu tuple-dəki rəqəmləri artan sırada sıralayın və nəticəni yeni bir tuple olaraq yaradın.
# Başlanğıc tuple-i ("apple", "banana", "cherry") olaraq yaradın.
# Bu tuple-dəki sözləri əlifba sırasına görə sıralayın və nəticəni yeni bir tuple olaraq yaradın.

qarisiq=(5,3,1,4,2,8,13)
qarisiq_list=list(qarisiq)
artansira=sorted(qarisiq_list)
print(artansira)
yenilendi=tuple(artansira)
print(yenilendi)
sozlertuple=("apple", "banana","cherry")
sozlertuple_list=list(sozlertuple)
elifbasira=sorted(sozlertuple_list)
yenituplee=tuple(elifbasira)
print(yenituplee)

# Tapşırıq 4: Tuple-də Nested Tuple-dən Dəyərləri Düzgün Çıxarmaq
# Bir tuple yaradın və daxilində nested tuple saxlayın. 
# Bu nested tuple-dən müəyyən dəyərləri çıxarın və yeni tuple yaradın.
m=(1,2,3,(3,4,5,6,7),5,)
yeni_m=m[3][-2:]
yeni_tm=tuple(yeni_m)
print(yeni_tm)

# Başlanğıc tuple-i (("a", "b", "c"), (1, 2, 3), (True, False, True)) olaraq yaradın.
# Bu tuple-dən "b" və 2 dəyərlərini çıxarıb yeni bir tuple yaradın.
bas=(("a", "b","c",), (1,2,3), (True, False, True))
tuple_b=bas[0][1]
tuple_2=bas[1][1]
print("tuple_b", tuple_b , "\ntuple_2",tuple_2)

# Tapşırıq 1: Set-də Elementləri Tapmaq və Onları Çıxarmaq
# Bir set yaradın və müəyyən elementlərin set-də olub olmadığını yoxlayın. Bu elementləri yeni bir set-dən çıxarın.
set1={1,2,3,4,5,6,7,4}
set2={3,4,7,9}
set1_2=set1-set2
print(set1_2)

# Məsələ:
# Başlanğıc set-i {1, 2, 3, 4, 5} olaraq yaradın.
# Bu set-dən {2, 4} elementlərini çıxarın. Nəticədəki set-i ekrana çıxarın.

set12={1,2,3,4,5,}
set24={2,4}
print(set12-set24)

# Məsələ:
# Başlanğıc set-ləri {1, 2, 3} və {3, 4, 5} olaraq yaradın.
# Bu iki set-də ortaq olan elementləri tapın.Nəticədə yalnız ortaq elementləri saxlayan yeni bir set yaradın.
set123={1,2,3,8}
set345={3,4,5,8}
intersection=set123.intersection(set345)
unikal=set345.symmetric_difference(set123)
print(intersection)
print(unikal)

# Məsələ:
# Başlanğıc set-i {1, 2, 3, 4, 5} olaraq yaradın.
# Bu set-də 3 və 6 elementlərinin mövcudluğunu yoxlayın və nəticəni booleans dəyəri ilə çıxarın.
set36={1,2,3,4,5}
burdavar3= 3 in set36
burdavar6= 6 in set36
print("burdavar3", burdavar3,  "\nburdavar6" , burdavar6)

# Məsələ:
# Başlanğıc set-ləri {1, 2, 3, 4} və {3, 4, 5, 6} olaraq yaradın.
# Bu set-lərdə hər iki set-də olan elementləri tapın.
# Nəticədə ortaq elementlərdən ibarət yeni bir set yaradın.
birinciset={1,2,3,4}
ikinciset={3,4,5,6}
heriki=birinciset.intersection(ikinciset)
print(heriki)
