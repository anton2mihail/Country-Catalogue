"""This class creates a country object with attributes that include name, population, and area"""
# Programmer: Anton Mihail Lachmaniucu
# Date: 2017-11-28

# Creation of the class and the instance variables
class Country():
    def __init__(self, name="", pop = 0, area=0.00, continent=""):
        self._name = name.title()
        self._pop = pop
        self._area = area
        self._cont = continent.title()

    # Returns the name of the current Country object
    def getName(self):
        return self._name

    # Returns the population of the current Country object
    def getPopulation(self):
        return self._pop

    # Returns the area of the current Country object
    def getArea(self):
        return round(self._area, 2)

    # Returns the continent of the current Country object
    def getContinent(self):
        return self._cont

    # Sets a new population for the current Country object
    def setPopulation(self, pop):
        self._pop = pop

    # Sets a new area for the current Country object
    def setArea(self, area):
        self._area = area

    # Sets a new continent for the current Country object
    def setContinent(self, cont):
        self._cont = cont.title()

    # Calculates and returns the population density of the current Country object
    def getPopDensity(self):
        return round(self._pop/self._area, 2)

    # Creates a string representation of the Country object
    def __repr__(self):
        nm = self._name + " (pop:" + str(self._pop) + ", size:" + str(self._area) + ") in " + self._cont
        return nm
