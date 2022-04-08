from math import sqrt

from numpy.random import exponential, uniform


class UniformDistribution:
    def __init__(self, mean, sigma=1):
        self.mean = mean
        self.halfdiff = max((sqrt(12 * sigma)) / 2, self.mean)

    def generate(self):
        return uniform(self.mean - self.halfdiff, self.mean + self.halfdiff)


class ExponentialDistribution:
    def __init__(self, mean):
        self.mean = mean

    def generate(self):
        return exponential(self.mean)
