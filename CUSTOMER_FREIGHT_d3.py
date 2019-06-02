
class Customer:
    def __init__(self,customer_id,customer_name,address):
        self.__customer_name=customer_name
        self.__customer_id=customer_id
        self.__address=address
    def get_customer_id(self):
        print(self.__customer_id)
    def get_customer_name(self):
        print(self.__customer_name)
    def get_address(self):
        self.__address=address
    def validate_customer_id(self):
        if self.__customer_id//1000000==0 and self.__customer_id//100000==1:
            return(True)
        else:
            return(False)
class Freight:
    counter=0
    def __init__(self,recipient_customer,from_customer,weight,distance):
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance
        self.__freight_id=0
        self.__freight_charge=0
    def get_distance(self):
        print(self.__distance)
    def get_weight(self):
        print(self.__weight)
    def get_from_customer(self):
        print(self.__from_customer)
    def get_recipient_customer(self):
        print(self.__recipient_customer)
    def get_freight_charge(self):
        print(self.__freight_charge)
    def get_freight_id(self):
        print(self.__freight_id)
    def validate_weight(self):
        if self.__weight%5==0:
            return(True)
        else:
            return(False)
    def validate_distance(self):
        if self.__distance>=500 and self.__distance<=5000:
            return(True)
        else:
            return(False)
            
    def forward_cargo(self):
        if self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id() and self.validate_distance() and self.validate_weight():
            Freight.counter+=2
            self.__freight_id+=Freight.counter
            
            self.__freight_charge=(self.__weight*150)+(self.__distance*60)
            
        else:
            print("error")
            
            
            
objj=Freight(Customer(45,"anil","main road"),Customer(56,"akash","street"),45,890)
objj.forward_cargo()
objj.get_freight_id()
objj.get_recipient_customer()
objj.get_freight_charge()
objj.get_from_customer()

            
       
