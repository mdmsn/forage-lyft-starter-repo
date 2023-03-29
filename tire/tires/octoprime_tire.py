from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear_data):
        self.tire_wear_data = tire_wear_data


    def needs_service(self):
        if(sum(self.tire_wear_data)>=3):
            return True
        else:
            return False