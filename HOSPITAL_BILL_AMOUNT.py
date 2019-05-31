class Bill:
    def __init__(self,bill_id,patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name
        self.__bill_amount=0
        
        
    def calculate_bill_amount(self,consultation_fees, quantity_list, price_list):
        self.__bill_amount=consultation_fees
        for i in range(0,len(quantity_list)):
            self.__bill_amount+=(quantity_list[i]*price_list[i])
        self.__bill_amount=self.__bill_amount    
        
    def get_bill_amount(self):
        print(self.__bill_amount)
    def get_bill_id(self):
        print(self.__bill_id)
    def get_patient_name(self):
        print(self.__patient_name)
        
        
pat1=Bill(12,"james")
quantity_list=[12.35, 3.96, 154, 65]
price_list=[5, 1, 2, 1]
pat1.calculate_bill_amount(150,quantity_list,price_list)
pat1.get_bill_id()
pat1.get_patient_name()
pat1.get_bill_amount()
