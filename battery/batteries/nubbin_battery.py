from battery.battery import Battery
from datetime import date

class NubbinBattery(Battery):
    
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if(service_threshold_date < date.today()):
            return True
        else:
            return False