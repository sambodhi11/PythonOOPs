class car:
  
    def intro(self):
        print("Cars")

    def speed(self):
        print("Car have high speed.")

class Honda(car):
  
    def speed(self):
        print("speed show be slow.")

class Hyundai(car):

    def speed(self):
        print("Hyundai has great speed.")

obj_car= car()
obj_hon = Honda()
obj_hyn= Hyundai()

obj_car.intro()
obj_car.speed()

obj_hon.intro()
obj_hon.speed()

obj_hyn.intro()
obj_hyn.speed()
