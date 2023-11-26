class Personne:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age 


    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name = name
        
    def getage(self):
        return self.__age
    
    def setage(self,age):
        self.__age = age
        
    def getcount(self):
        return self.__count
    
    def afficheInfo(self):
        print("name :", self.__name)
        print("age :", self.__age)

class Stagiaire(Personne):
    def __init__(self,name,age,note):
      Personne.__init__(self,name,age)
      self.__note = note

    def afficheInfo(self):
        print(self.__note)

    def afficheInfo(self):
        Personne.afficheInfo(self)
        print("la note est :", self.__note)

    
    
P1= Personne("sara",12)
P1.setname("hafssa") 
P1.afficheInfo()
print(P1.getname())
S1 = Stagiaire("kawtar",15,16)
S1.setage(19)
S1.afficheInfo()
print(S1.getage())
    