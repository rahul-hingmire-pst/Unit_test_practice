import unittest
from unittest.mock import Mock
import practice


class Testpractice(unittest.TestCase):
    practice.speed = Mock()
    # def test_alert_normal(self):
    #     practice.speed = Mock()
    #     practice.speed.return_value = 70
    #     self.assertFalse(practice.alert())

    # def test_alert_overspeed(self):
    #     practice.speed = Mock()
    #     practice.speed.return_value = 100
    #     self.assertFalse(practice.alert())

    # def test_alert_underspeed(self):
    #     practice.speed = Mock()
    #     practice.speed.return_value = 59
    #     self.assertTrue(practice.alert())