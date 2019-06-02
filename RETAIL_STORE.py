
class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity
    def get_price_per_quantity(self):
        return(self.__price_per_quantity)
    def get_description(self):
        return(self.__description)
    def get_item_id(self):
        return(str(self.__item_id))
class  Bill:
    counter=1000
    def __init__(self):
        self.__bill_id=None
        self.__bill_amount=0
        Bill.counter+=1
    def get_bill_amount(self):
        return(self.__bill_amount)
    def get_bill_id(self):
        
        return(self.__bill_id)
    def generate_bill_amount(self,items,item_quantity):
        
        self.__bill_id="B"+str(Bill.counter)
        for i in item_quantity.keys():
            item_quantity[i.upper()]=item_quantity.pop(i)
        print(item_quantity)    
    
        for i in items:
            w=i.get_item_id().upper()
            if w in item_quantity.keys():
                
                self.__bill_amount+=(item_quantity[w]*i.get_price_per_quantity())
            
class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None
    def pays_bill(self,bill):
        
        self.__payment_status="Paid"
        
        print(self.__customer_name)
        print(bill.get_bill_amount())
        print(bill.get_bill_id())
    def get_customer_name(self):
        print(self.__customer_name)
    def get_payment_status(self):
        print(self.__payment_status)
items=[Item("12R987","rice",67),Item("45r","wheat",90),Item("78r","pulses",100)]
item_quantity={"12R987":4,"45R":5,"78r":3}

b=Bill()
b.generate_bill_amount(items,item_quantity)

Customer_1=Customer("anil")

Customer_1.get_customer_name()
Customer_1.pays_bill(b)
Customer_1.get_payment_status()

