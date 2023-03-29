import unittest
from tire.tires.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):

    def test_tire_module_exists(self):
        arr = [1,2,3,4]
        tire = OctoprimeTire(arr)
    
    def test_needs_service_returns_a_value(self):
        arr = [1,2,3,4]
        tire = OctoprimeTire(arr)
        service_due = tire.needs_service()
        self.assertIsNotNone(service_due)

    def test_needs_service_returns_true_correctly(self):
        arr = [1,2,3,4]
        tire = OctoprimeTire(arr)
        service_due = tire.needs_service()
        self.assertTrue(service_due)
    
    def test_needs_service_returns_false_correctly(self):
        arr = [0.1,0.2,0.3,0.4]
        tire = OctoprimeTire(arr)
        service_due = tire.needs_service()
        self.assertFalse(service_due)