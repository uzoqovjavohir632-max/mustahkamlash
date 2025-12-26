    #1-misol
#Asosiy Hayvon klassi yarating (ism, yosh). Undan Mushuk, It, Qush klasslarini hosil qiling. Har biri o'zining ovoz_chiqar() metodiga ega bo'lsin. 

class Hayvon():
    def __init__(self , ism , yosh) :
     self.ism = ism 
     self.yosh= yosh

    def malumot(self):
        print("Ismi:", self.ism)
        print("Yoshi:", self.yosh)



class mushuk(Hayvon):
   def ovoz_chiqar(self):
      print("miyov" , "miyov")

class it(Hayvon):
   def ovoz_chiqar(self):
      print("vov vov")    

class qush(Hayvon):
   def ovoz_chiqar(self):
      print("chip chip")

tur =input("hayvon turini kiriting mushuk &  it  &  qush : ")
ism=input("hayvon ismini kiriting : ")
yosh= int(input("hayvon yoshini kiriting: "))

if tur == "mushuk" :
     hayvon = mushuk( ism,  yosh)
elif tur =="It" :
   hayvon = it (ism , yosh ) 
elif    tur == "Qush" :
   hayvon = qush (ism , yosh)
else :
   print ("notogri turdagi hayvon kiritildi")
   exit ()    

print ("\n hayvon malumotlari : ")
hayvon.malumot () 
hayvon.ovoz_chiqar()
     
      
   
     
