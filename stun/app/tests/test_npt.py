from django.test import TestCase
from models import *


class NptTest(TestCase):

    def identity(self):
        ip1 = "2001:13c7:7001:7000:f19c:6c05:a546:f373"
        is_npt = StunMeasurementManager.is_npt(ip1, ip1)
        self.assertEqual(is_npt, True)
