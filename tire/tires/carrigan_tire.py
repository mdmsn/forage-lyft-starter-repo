from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_wear_data):
        self.tire_wear_data = tire_wear_data


    def needs_service(self):
        if(max(self.tire_wear_data)>=0.9):
            return True
        else:
            return False