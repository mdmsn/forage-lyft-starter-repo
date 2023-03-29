import unittest
from datetime import date
from battery.batteries.spindler_battery import SpindlerBattery
from battery.batteries.nubbin_battery import NubbinBattery

class TestSplindkerBattery(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class TestNubbinBattery(unittest.TestCase):

    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()