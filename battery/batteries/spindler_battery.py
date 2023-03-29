from battery.battery import Battery
from datetime import date

class SpindlerBattery(Battery):

    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # once every 2 years
        threshold_year = self.last_service_date.year + 2
        service_threshold_date = self.last_service_date.replace(year=threshold_year)
        if(service_threshold_date < date.today()):
            return True
        else:
            return False