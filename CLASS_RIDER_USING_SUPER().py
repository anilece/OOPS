
#Start writing your code here
'''
Rider
- experience
- trained_status
__init__( trained_status, experience)
+ rides_vehicle()
BikeRider
- race_license
+ rides_in_dome()
__init__( trained_status, experience, race_license)
CycleRider

+ rides_blindfolded()
'''
class Rider:
    def __init__(self,trained_status,experience):
        self.__trained_status=trained_status
        self.__experience=experience
    def rides_vehicle(self):
        print("riding vehicle")
        
class BikeRider(Rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(trained_status,experience)
        self.__race_license=race_license
    def rides_in_dome(self):
        print("bike rider riding")
class CycleRider(Rider):
    def rides_blindfolded(self):
        print("CycleRider riding")
        
r=BikeRider(True,9,True)
c=CycleRider("yes",8)
c.rides_blindfolded()
r.rides_in_dome()









