from car import Car
from engine.engines.capulet_engine import CapuletEngine
from engine.engines.willoughby_engine import WilloughbyEngine
from engine.engines.sternman_engine import SternmanEngine
from battery.batteries.spindler_battery import SpindlerBattery
from battery.batteries.nubbin_battery import NubbinBattery


class CarFactory(Car):      

    def create_calliope(last_service_date, current_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car_battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, car_battery) 


    def create_glissade(last_service_date, current_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, car_battery)


    def create_palindrome(last_service_date, current_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        car_battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, car_battery)


    def create_rorschach(last_service_date, current_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, car_battery)


    def create_thovex(last_service_date, current_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        car_battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, car_battery)