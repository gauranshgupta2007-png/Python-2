class vehicle:
    def move(self):
        print ("Vehicles are Driven.")

class Car(vehicle):
    def move(self):
        print ("Cars are Driven on the road.")

class Bicycle(vehicle):
    def move(self):
        print ("Bicycles are ridden on road.")

vehicle = [vehicle(),Car(),Bicycle()]

for S in vehicle :
    S.move()