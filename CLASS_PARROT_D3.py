
'''
ClassName:Parrot
Attributes: counter->static,color,unique_number,name
Methods:__init__(name,color)'''
class Parrot:
    __counter=7000
    def __init__(self,name,color):
        self.__color=color
        self.__name=name
        Parrot.__counter+=1
        self.__unique_number=Parrot.__counter
        
    def get_name(self):
        print(self.__name)
    def get_color(self):    
        print(self.__color)
    def get_unique_number(self):
        print(self.__unique_number)
    
        
   

    
pa1=Parrot("chickoo","green")

pa1.get_unique_number()
pa1.get_color()
pa1.get_name()
pa1.get_unique_number()
pa1.get_unique_number()
pa2=Parrot("anku","blue")

pa2.get_unique_number()
