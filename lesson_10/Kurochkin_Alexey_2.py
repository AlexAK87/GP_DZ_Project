from abc import ABC, abstractmethod


class Clothing(ABC):
    @abstractmethod
    def calculation_total_tissue_cosumption(self):
        pass


class Coat(Clothing):
    def __init__(self, size):
        self.size = size

    @property
    def calculation_total_tissue_cosumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothing):
    def __init__(self, height):
        self.height = height

    @property
    def calculation_total_tissue_cosumption(self):
        return 2 * self.height + 0.3


coat = Coat(22)
costime = Costume(15)

print(coat.calculation_total_tissue_cosumption)
print(costime.calculation_total_tissue_cosumption)

