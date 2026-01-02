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

class Xodim():
    def __init__( self, ism, maosh ) :
        self.ism = ism 
        self.maosh = maosh
    def malumot (self):
       print (f" xodimning ismi {self.ism } , maoshi esa {self. maosh }")
class Dasturchi(Xodim) :
   def ish_qil(self ):
      print ("dasturchi kod yozmoqda")
class Menejer(Xodim) :
    def ish_qil(self):
      print("menejer ishlamoqda ")   
class Dizayner(Xodim):
    def ish_qil(self):
       print ("diazyner dizayn yaratmoqda ")
def  kiritish(klass):
     ism = input("xodim ismini kiriting ")
     maosh = int(input("xodim oladigan maoshni kiriting" ))
     return klass ( ism , maosh)
print(" 1- dasturchi ", " 2- menejer " , " 3- dizayner ")
tanlov = input ("tanlang : ")
if tanlov == "1" :
    t=kiritish(Dasturchi)
if tanlov == "2" :
    t=kiritish(Menejer)
if tanlov == "3" :
    t=kiritish(Dizayner)    

t.malumot()
t.ish_qil()

