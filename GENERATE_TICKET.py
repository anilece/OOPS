class Ticket:
    counter=0
    def __init__(self,source,destination,passenger_name):
        self.__ticket_id=None
        self.__source=source.upper()
        self.__destination=destination.upper()
        self.__passenger_name=passenger_name
    def get_passenger_name(self):
        print(self.__passenger_name)
    def get_destination(self):
        print(self.__destination)
    def get_source(self):
        print(self.__source)
    def get_ticket_id(self):
        print(self.__ticket_id)
        
    def validate_source_destination(self):
        if self.__source=="DELHI" and self.__destination in ["CHENNAI","MUMBAI","PUNE","KOLKATA"]:
            return (True)
        else:
            return(False)
    def generate_ticket(self):
        self.validate_source_destination()
        
            
        if self.validate_source_destination():
                Ticket.counter+=1
                if Ticket.counter<=9:
                    ticket=self.__source[:1]+self.__destination[:1]+"0"+str(Ticket.counter)
                else:
                    
                    ticket=self.__source[:1]+self.__destination[:1]+str(Ticket.counter)
                
                self.__ticket_id=ticket
                
                self.get_ticket_id()
                
        else:
            self.__ticket_id=None
            Ticket.counter+=1
            self.get_ticket_id()
            
tic_obj=Ticket("Delhi","Chennai","anil")
tic_obj.generate_ticket()
tic_obj.get_passenger_name()
tic_obj.get_source()
tic_obj.get_destination()
