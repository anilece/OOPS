
'''
Flower Name	Level(in Kgs)
Orchid	15
Rose	25
Jasmine	40
'''
class Flower:
    def __init__(self):
       self.__flower_name=None
       self.__price_per_kg=None
       self.__stock_available=None
       self.required_quantity=None
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name.lower()
    def set_price_per_kg(self,price_per_kg ):
        self.__price_per_kg=price_per_kg
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
    def get_flower_name(self):
        print(self.__flower_name)
    def get_price_per_kg(self):
        print(self.__price_per_kg)
    def get_stock_available(self):
        print(self.__stock_available)
        
    def validate_flower(self):
        if self.__flower_name in ["orchid","rose","jasmine"]:
            return(True)
        else:
            return(False)
    def validate_stock(self,required_quantity):
        if required_quantity<=self.__stock_available:
            self.required_quantity=required_quantity
            return (True)
        else:
            return(False)
            
    def sell_flower(self,required_quantity):
        self.required_quantity=required_quantity
        if self.validate_stock(required_quantity) and self.validate_flower():
            self.__stock_available-=self.required_quantity
            print(self.__stock_available,"Are avaialbe")
            
    def check_level(self):
        if self.__flower_name=="orchid":
            if self.__stock_available<15:
                return(True)
            else:
                return(False)
        elif(self.__flower_name=="rose"):
            if self.__stock_available<25:
                return(True)
            else:
                return(False)
        elif(self.__flower_name=="jasmine"):
            if (self.__stock_available<40):
                return(True)
            else:
                return(False)
        else:
            return(False)
            
            
boquet=Flower()
boquet.set_flower_name("Rose")
boquet.set_stock_available(9)
boquet.set_price_per_kg(90)
boquet.sell_flower(7)
boquet.check_level()
            
                
                
                
                
                
                
                
                
    
    
    
    
