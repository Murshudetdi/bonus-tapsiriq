#FOR LOOPS
#Tapşırıq 1:Bir dövr (for loop) istifadə edərək 1-dən 10-a qədər olan bütün rəqəmlərin kvadratlarını çap edin
liste=[1,2,3,4,5,6,7,8,9]
for a in liste:
    a=a**2
    print(a)


#Tapşırıq 2:
# Verilmiş bir siyahıdakı (list) tək ədədləri taparaq onları çap edin: [3, 8, 12, 17, 24, 29, 33]
list=[3,8,12,17,24,29,33]
for tekeded in list:
    if tekeded %2==1:
        print(tekeded)


#Tapşırıq 3:
# Bir stringdəki hər bir hərfi ayrı-ayrılıqda çap edin: "Python"
pythonn="Python"
for Python in pythonn :
    print(Python)


#Tapşırıq 4:
# 0-dan 100-ə qədər olan bütün cüt rəqəmləri bir dövr ilə çap edin.
a=range(0,100)
for cut in a:
    if cut %2==0:
        print(cut)


#Tapşırıq 5:
# Verilmiş siyahıdakı bütün ədədlərin cəmini hesablayın: [5, 7, 3, 8, 10]
req=[5,7,3,8,10]
rem_cem=0
for cemi in req:
    rem_cem+=cemi
    print(rem_cem)


#Tapşırıq 6:(bu tapsiriqda hem for loopdan hemde if elif else den istifade edeceksiz) 
# Verilmiş siyahıdakı ədədlərin mənfi, müsbət və sıfır olduğunu təyin edin 
# və hər birini ayrıca qruplaşdırın: [-5, 0, 6, -8, 10, -3, 0, 7]
qarisiq=[-5,0,6,-8,10,-3,0,7]
for eded in qarisiq:
    if eded>0:
        print( f"musbet: {eded}")
    elif eded<0:
        print(f"menfi: {eded}")
    else:
        print(f"zero: {eded}")

   


