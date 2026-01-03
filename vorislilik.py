    #1-misol
#     Asosiy Hayvon klassi yarating (ism, yosh). Undan Mushuk, It, Qush klasslarini hosil qiling. 
#   Har biri o'zining ovoz_chiqar() metodiga ega bo'lsin. 

# class Hayvon():

#     def __init__(self , ism , yosh) :
#      self.ism = ism 
#      self.yosh= yosh

#     def malumot(self):
#         print("Ismi:", self.ism)
#         print("Yoshi:", self.yosh)



# class mushuk(Hayvon):
#    def ovoz_chiqar(self):
#       print("miyov" , "miyov")

# class it(Hayvon):
#    def ovoz_chiqar(self):
#       print("vov vov")    

# class qush(Hayvon):
#    def ovoz_chiqar(self):
#       print("chip chip")

# tur =input("hayvon turini kiriting mushuk &  it  &  qush : ")
# ism=input("hayvon ismini kiriting : ")
# yosh= int(input("hayvon yoshini kiriting: "))
 
# if tur == "mushuk" :
#      hayvon = mushuk( ism,  yosh)
# elif tur =="It" :
#    hayvon = it (ism , yosh ) 
# elif    tur == "Qush" :
#    hayvon = qush (ism , yosh)
# else :
#    print ("notogri turdagi hayvon kiritildi")
#    exit ()    

# print ("\n hayvon malumotlari : ")
# hayvon.malumot () 
# hayvon.ovoz_chiqar()
     


# 2-misol
#ransport klassi (rang, narx, yil). Undan Mashina, Mototsikl, Velosiped yarating. Har birida harakatlan() metodi bo'lsin. 


# class Transport():
#     def __init__(self, rang, narx, yil):
#       self.rang= rang 
#       self.narx = narx
#       self.yil=yil 
#     def malumot(self):
#       print(f"  transport rangi {self.rang} , narxi esa {self.narx} va uning  ishlab chiqarilgan yili {self.yil} ")
# class Mashina(Transport):
#     def harakatlan (self):
#        print("mashina yo'lida davom etmoqda" )
# class Mototsikl(Transport):
#    def harakatlan(self):
#        print("matatsikl harakatlanmoqda")
# class Velosiped(Transport):
#    def harakatlan (self):
#       print("velosiped yo'lida davom etmoqda ")

# def  kiritish(klas)  :
#    rang = input ("transport rangini kirirting:  ")
#    narxi= input("transport  narxini kiriting:  ")
#    yili= input ("transport  yilini kiriting:   ")
#    return  klas (rang ,narxi, yili)
# print (" 1- mashina",  "2- mototsikl" , "3-velosiped")
# tanlov =input ("tanlang :" )
# if tanlov == "1": 
#     t = kiritish(Mashina)
# elif tanlov == "2":
#     t = kiritish(Mototsikl)
# else:
#     t = kiritish(Velosiped)                                   


# t.malumot()
# t.harakatlan()
  


#  3- misol 
# Xodim klassi (ism, maosh). Dasturchi, Menejer, Dizayner klasslarini yarating.
# Har birida ish_qil() metodi bo'lsin. 

# class Xodim():
#     def __init__( self, ism, maosh ) :
#         self.ism = ism 
#         self.maosh = maosh
#     def malumot (self):
#        print (f" xodimning ismi {self.ism } , maoshi esa {self. maosh } so'm ")
# class Dasturchi(Xodim) :
#    def ish_qil(self ):
#       print ("dasturchi kod yozmoqda")
# class Menejer(Xodim) :
#     def ish_qil(self):
#       print("menejer ishlamoqda ")   
# class Dizayner(Xodim):
#     def ish_qil(self):
#        print ("diazyner dizayn yaratmoqda ")
# def  kiritish(klass):
#      ism = input("xodim ismini kiriting:  ")
#      maosh = int(input("xodim oladigan maoshni kiriting ( so'mda ): " ))
#      return klass ( ism , maosh)
# print(" 1- dasturchi ", " 2- menejer " , " 3- dizayner ")
# tanlov = int(input ("tanlang : "))
# if tanlov == 1:
#     t=kiritish(Dasturchi)
# elif tanlov == 2 :
#     t=kiritish(Menejer)
# elif tanlov == 3 :
#     t=kiritish(Dizayner) 

# else :
#     print  ( "matn kiritmang yoki 4 dan kichik butun son kiriting ")   
#     exit()
# t.malumot()
# t.ish_qil()



# 4- misol 
# Shakl klassi yarating. Undan Doira, Tortburchak, Uchburchak hosil qiling. Har birida 
# yuza() va perimetr() metodlari bo'lsin. 
class Shakl():
    def __init__(self, nom):
        self.nom = nom

    def malumot(self):
        print("Shakl nomi:", self.nom)


class Doira(Shakl):
    def __init__(self, nom, r):
        self.nom = nom
        self.r = r

    def yuza(self):
        print("Yuza:", 3.14 * self.r * self.r)

    def perimetr(self):
        print("Perimetr:", 2 * 3.14 * self.r)


class Tortburchak(Shakl):
    def __init__(self, nom, a, b):
        self.nom = nom
        self.a = a
        self.b = b

    def yuza(self):
        print("Yuza:", self.a * self.b)

    def perimetr(self):
        print("Perimetr:", 2 * (self.a + self.b))


class Uchburchak(Shakl):
    def __init__(self, nom, a, b, c):
        self.nom = nom
        self.a = a
        self.b = b
        self.c = c

    def yuza(self):
        print("Yuza:", (self.a * self.b) / 2)

    def perimetr(self):
        print("Perimetr:", self.a + self.b + self.c)


def kiritish(klass):
    nom = input("Shakl nomini kiriting: ")

    if klass == Doira:
        r = int(input("Radiusni kiriting: "))
        return klass(nom, r)

    if klass == Tortburchak:
        a = int(input("a ni kiriting: "))
        b = int(input("b ni kiriting: "))
        return klass(nom, a, b)

    if klass == Uchburchak:
        a = int(input("a ni kiriting: "))
        b = int(input("b ni kiriting: "))
        c = int(input("c ni kiriting: "))
        return klass(nom, a, b, c)


print("1- Doira", "2- To‘rtburchak", "3- Uchburchak")
tanlov = int(input("Tanlang: "))

if tanlov == 1:
    s = kiritish(Doira)
elif tanlov == 2:
    s = kiritish(Tortburchak)
elif tanlov == 3:
    s = kiritish(Uchburchak)
else:
    print("Noto‘g‘ri tanlov!")
    exit()

s.malumot()
s.yuza()
s.perimetr()

                 