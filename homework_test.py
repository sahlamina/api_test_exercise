import pytest
import unittest2

from mathopp import *
class Sqrt_Test(unittest2.TestCase):

    casio = Calctest()
    def test_sqrt(self):
        self.assertEqual(self.casio.find_sqrt(9), 3)

    def test_ceil(self):
        self.assertEqual(self.casio.find_ceil(8.76546789), 9)