
'''
ClassName Vehicle
Vehicles are of two types – "Two Wheeler" and "Four Wheeler". Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheelers and 6% of the vehicle cost for four wheelers. Calculate the premium amount and display the vehicle details.
Attributes vehicle_id vehicle_cost vehicle_type premium_amount
Methods __init__() calculate_premium() display_vehicle_details()'''
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_cost=None
        self.__vehicle_type=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def set_vehicle_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
    def get_premium_amount(self):
        print(self.__premium_amount)
        
    def get_vehicle_type(self):
        print(self.__vehicle_type)
    def get_vehicle_id(self):
        print(self.__vehicle_id)
    def get_vehicle_cost(self):
        print(self.__vehicle_cost)
    def set_premium_amount(self,premium_amount):
            self.__premium_amount=premium_amount
    def calculate_premium(self):
        
        if (self.__premium_amount!=None):
            self.__premium_amount=(self.__vehicle_cost*self.__premium_amount)
            self.__vehicle_cost+=self.__premium_amount
        else:
            print("wrong vehicle_type")
    def display_vehicle_details(self):
        self.get_vehicle_id()
        self.get_vehicle_type()
        self.get_vehicle_cost()
        self.get_premium_amount()
customer=Vehicle()
s="Two Wheeler"
customer.set_vehicle_type(s)
customer.set_vehicle_cost(9000)
customer.set_vehicle_id(12)
if (s=="Two Wheeler"):
    premium_amount=0.02
    customer.set_premium_amount(premium_amount)
    customer.calculate_premium()
    customer.display_vehicle_details()
elif(s=="Four Wheeler"):
    premium_amount=0.06
    customer.set_premium_amount(premium_amount)
    customer.calculate_premium()
    customer.display_vehicle_details()
else:
    print("wrong vehicle type")
    customer.set_premium_amount()
    customer.calculate_premium()
    customer.display_vehicle_details()
