
# 1 -misol
#Talaba klassi yarating: ism, familiya, yosh, guruh attributlari va tanishish() methodi bo'lsin

# class Talaba :
#     def __init__(self, ism, familiya, yosh, guruh ):
#         self . ism = ism 
#         self . familiya = familiya
#         self . yosh = yosh
#         self . guruh = guruh
#     def tanishtir (self ):
#         return ( f"salom mening ismim {self.ism}, familiyam {self. familiya}, yoshim {self.yosh}, va guruhim {self.guruh}.")


# talaba1 =  Talaba ( "Javohir","Uzoqov", "17 da" , "305- 25- ATT" )
# talaba2 =  Talaba ( "Muhriddin","Halimov", "18 da" , "305- 25- ATT" )
# talaba3 =  Talaba ( "SHohrux","Davronov", "18 da ", "305- 25- ATT" )
# print(talaba1.tanishtir())
# print(talaba2.tanishtir())
# print(talaba3.tanishtir())




    #2 - misol
#Kitob klassi yarating: nomi, muallif, narx, sahifalar_soni va malumot_berish() methodi

# class Kitoplar :
#     def __init__(self, nomi, muallif , narx , sahifalar_soni ):
#         self. nomi= nomi
#         self. muallif = muallif
#         self. narx = narx 
#         self. sahifalar_soni = sahifalar_soni
#     def malumot_berish (self):
#             return (f" bu kitobning nomi {self.nomi}, kitob muallifi {self.muallif}, kitobning narxi {self. narx}, kitobnong sahifalari soni {self. sahifalar_soni} . ")
        

# kitop1 = Kitoplar("shum bola", "G'afur Gulom ", 20000 , 200 )
# kitop2 = Kitoplar("sariq devni minib", "XUdoyberdi To'xtaboyev ", 25000 , 230 )
# print (kitop1 .malumot_berish())
# print (kitop2 .malumot_berish())


     #3-misol
#Telefon klassi yarating: marka, model, rangi, narxi va xususiyatlar() methodi
# class Telefon :
#     def __init__(self, marka, model,rangi,narxi ):
#         self.marka = marka
#         self.model= model
#         self.rangi = rangi
#         self.narxi = narxi
#     def xususiyatlari(self):
#              return( f"Bu telefonning markasi {self . marka}, modeli {self. model}, rangi {self .rangi}, narxi esa {self . narxi}")
# telefon1 = Telefon ("samsung" ,"A 11 4G" , "qora", "2million so'm"  )   
# telefon2 = Telefon ("honor" , "X 9c " ,  "ko'k nefrit" , "3 million so'm" )
# print (telefon1 . xususiyatlari())
# print (telefon2 . xususiyatlari())

    #4 - misol
#Mashina klassi yarating: marka, rangi, yili, narxi va malumot() methodi 
# class Mashina () :
#     def __init__(self , marka, rangi , yili , narxi) :
#         self. marka= marka
#         self. rangi = rangi
#         self. yili = yili
#         self. narxi = narxi
        
#     def malumot(self)  :
#        return ( f" Mashina mashina {self. marka}, rangi esa {self . rangi}, yili {self . yili}, va narxi {self. narxi} dollar") 
# mashina1 = Mashina("BYD SONG PLUS", "oq", 2024, 25000) 
# mashina2 = Mashina("Malibu 2 Premier", "qop qora", 2022 , 20000)
# print(mashina1. malumot())
# print(mashina2. malumot())                        

          
     # 5 - misol
  #Mahsulot klassi yarating: nomi, narxi, soni va umumiy_narx() hisoblovchi method 
# class Mahsulot ():
#     def __init__(self,nomi, narxi, soni):
#         self. nomi = nomi
#         self.narxi = narxi
#         self.soni = soni 

#     def umumiy_narxi(self):
#         return(f"bu mahsulot { self . nomi}, narxi {self . narxi} , soni {self . soni}")

# mahsulot1= Mahsulot( "kampyuter" ,"600 dollar", "5 ta qolgan")
# mahsulot2= Mahsulot("telefon", "200 dollar", "10 ta qolgan")
# print(mahsulot1 .umumiy_narxi())
# print(mahsulot2 .umumiy_narxi())

    #6- misol
 #Doira klassi: radius attributi, yuza() va perimetr() methodlari 
# class Doira () :
#     def __init__(self, radius) :
#         self. radius = radius
#     def yuza (self):
#        return 3.14 * self.radius * self.radius

#     def perimetr(self):
#         return 2 * 3.14 * self.radius


# r = float(input("Radiusni kiriting: "))
# d = Doira(r)

# print("Doira yuzi:", d.yuza())
# print("Doira perimetri:", d.perimetr())


   #7 -misol
#To'rtburchak klassi: uzunlik, kenglik, yuza(), perimetr(), kvadratmi() methodlari 
# class Tortburchak ():
#     def __init__(self , uzunlik , kenglik):
#         self . uzunlik = uzunlik
#         self . kenglik = kenglik
#     def yuza (self):
#         return self.uzunlik * self .kenglik  

#     def perimetr (self)  :
#         return 2* (self.uzunlik + self. kenglik)
#     def kvadratmi(self):
#         return self.uzunlik == self.kenglik


# a = float(input("Uzunlikni kiriting: "))
# b = float(input("Kenglikni kiriting: "))

# t = Tortburchak(a, b)

# print("Yuza:", t.yuza())
# print("Perimetr:", t.perimetr())
# print("Kvadratmi:", t.kvadratmi())


  # 8-misol
#BankHisob klassi: egasi, balans, pul_qoshish() va pul_yechish() methodlari 









    # 9-misol
# Harorat klassi: selsiy attributi, farengeytga() va kelvinega() o'giruvchi methodlar
class Harorat:
    def __init__(self, selsiy):
        self.selsiy = selsiy

    def farengeytga(self):
        return (self.selsiy * 9/5) + 32

    def kelvinega(self):
        return self.selsiy + 273.15


temp = float(input("Selsiy haroratni kiriting: "))
h = Harorat(temp)

print("Farengeyt:", h.farengeytga())
print("Kelvin:", h.kelvinega())