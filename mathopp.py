import math


class Calctest:

    def find_sqrt(self, num):
        return int(math.sqrt(num))

    def find_ceil(self, num):
        return math.ceil(num)

casio = Calctest()
print(casio.find_sqrt(9))
print(casio.find_ceil(8.76546789))