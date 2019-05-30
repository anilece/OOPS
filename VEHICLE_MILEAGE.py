'''
ClassName:Vehicle
Attributes mileage fuel_left
Methods __init__() identify_distance_travelled(initial_fuel) identify_distance_that_can_be_travelled()
'''
fuel=0
class Vehicle:
    def __init__(self):
        self.mileage=None
        self.fuel_left=None
        self.initial_fuel=None
        self.fuel=None
        
        
    def identify_distance_travelled(self,initial_fuel):
        self.initial_fuel=initial_fuel
        self.fuel=self.initial_fuel-self.fuel_left
        return(self.fuel*self.mileage)
    def identify_distance_that_can_be_travelled(self):
        
        if self.fuel_left<=5:
            return (0)
        else:
            return((self.fuel_left-5)*self.mileage)
ak=Vehicle()
ak.mileage=20
ak.fuel_left=12

print(ak.identify_distance_travelled(60))
print(ak.identify_distance_that_can_be_travelled())
