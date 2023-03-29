from car_factory import CarFactory
from datetime import date

#    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):

glissade = CarFactory.create_glissade(
    date.today().replace(year=date.today().year-1),
    date.today(),
    60000,
    3)  
print(f'Glissade needs service: {glissade.needs_service()}')

calliope = CarFactory.create_calliope(
    date.today().replace(year=date.today().year-1),
    date.today(),
    30000,
    3)  
print(f'Calliope needs service: {calliope.needs_service()}')

palindrome = CarFactory.create_palindrome(
    date.today().replace(year=date.today().year-1),
    date.today(),
    True)  
print(f'Pallindrome needs service: {palindrome.needs_service()}')

rorschach = CarFactory.create_rorschach(
    date.today().replace(year=date.today().year-3),
    date.today(),
    60000,
    0)  
print(f'Rorschach needs service: {rorschach.needs_service()}')

thovex = CarFactory.create_thovex(
    date.today().replace(year=date.today().year-3),
    date.today(),
    30000,
    0)  
print(f'Thovex needs service: {thovex.needs_service()}')