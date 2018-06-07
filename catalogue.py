"""This is a Class that creates an instance of country objects and can perform miscellaneous tasks on them"""
# Programmer: Anton Mihail Lachmaniucu
# Date: 2017-11-28
# Begin by importing the Country class
from country import *


class CountryCatalogue():
    # Creation of class Variables
    countryCat = []
    cDictionary = dict()

    def __init__(self, namesFile, infoFile):
        f1 = open(namesFile, "r")
        line1 = f1.readline()
        line1 = f1.readline()
        while line1 != "":
            cun, con = line1.split(",")
            cun = cun.strip("\n")
            con = con.strip("\n")
            # Fill Country/Continent Dictionary
            CountryCatalogue.cDictionary.update({cun: con})
            line1 = f1.readline()
        f2 = open(infoFile, "r")
        line2 = f2.readline()
        line2 = f2.readline()
        while line2 != "":
            country, pop, area = line2.split("|")
            pop = int(pop.replace(',' , ''))
            area = float(area.replace(',' , ''))
            tempCountry = Country(country , pop, float(area), str(CountryCatalogue.cDictionary[country]))
            # Fill Country Catalogue of Country objects
            CountryCatalogue.countryCat.append(tempCountry)
            line2 = f2.readline()

    # Defines the lookup of a country by name
    def findCountry(self, countName):
        temp = ""
        for x in CountryCatalogue.countryCat:
            if x.getName() == countName:
                temp = x
        if temp != "":
            return temp
        else:
            return None

    # Allows for the setting of a new population for a country by name
    def setPopulationOfCountry(self, countName, newPop):
        for i in CountryCatalogue.countryCat:
            if i.getName() == countName:
                i.setPopulation(newPop)
                return True
        return False

    # Allows for setting of the area of a country also by name
    def setAreaOfCountry(self, countName, newArea):
        for i in CountryCatalogue.countryCat:
            if i.getName() == countName:
                i.setArea(newArea)
                return True
        return False

    # Defines the addition of a country object to the instance
    def addCountry(self, countName, pop, area, continent):
        for i in CountryCatalogue.countryCat:
            if i.getName() == countName:
                return False
        new = Country(countName, pop, area, continent)
        CountryCatalogue.countryCat.append(new)
        CountryCatalogue.cDictionary.update({countName:continent})
        return True

    # Allows for the removal of a country object from the instance
    def deleteCountry(self, countName):
        found = False
        for i in CountryCatalogue.countryCat:
            if i.getName() == countName:
                CountryCatalogue.countryCat.remove(i)
        for x in CountryCatalogue.cDictionary:
            if x == countName:
               found = True
        if found:
            del CountryCatalogue.cDictionary[countName]

    # Prints out all the country objects in the Catalogue
    def printCountryCatalogue(self):
        print([x for x in CountryCatalogue.countryCat])

    # Returns the countries that are found in a specific continent
    def getCountriesByContinent(self, continent):
        countryMatches = []
        for i in CountryCatalogue.cDictionary:
            if i == continent:
                countryMatches.append(i)
        return countryMatches

    # Returns a list of countries and their populations from biggest pop to smallest pop in one continent
    def getCountriesByPopulation(self, continent=""):
        countPopList = []
        if continent == "":
            def getKey(item):
                return item[1]
            for i in CountryCatalogue.countryCat:
                countPopList.append((i.getName(), i.getPopulation()))
            countPopList = sorted(countPopList, key=getKey, reverse=True)
            return countPopList
        if continent != "":
            conts = CountryCatalogue.cDictionary.values()
            if continent in conts:
                for x in CountryCatalogue.countryCat:
                    if x.getContinent() == continent:
                        countPopList.append((x.getName(), x.getPopulation()))
            if len(countPopList) != 0:
                def getKey(item):
                    return item[1]
                countPopList = sorted(countPopList, key=getKey, reverse=True)
                return countPopList
            else:
                return countPopList

    # Returns a list of countries and their areas from biggest area to smallest area in one continent
    def getCountriesByArea(self, continent=""):
        countAreaList = []
        if continent == "":
            def getKey(item):
                return item[1]
            for i in CountryCatalogue.countryCat:
                countAreaList.append((i.getName(), i.getArea()))
            countAreaList = sorted(countAreaList, key=getKey, reverse=True)
            return countAreaList
        if continent != "":
            conts = CountryCatalogue.cDictionary.values()
            if continent in conts:
                for x in CountryCatalogue.countryCat:
                    if x.getContinent() == continent:
                        countAreaList.append((x.getName(), x.getArea()))
            if len(countAreaList) != 0:
                def getKey(item):
                    return item[1]
                countAreaList = sorted(countAreaList, key=getKey, reverse=True)
                return countAreaList
            else:
                return countAreaList

    # Returns the name of the continent with the highest population and the population of that continent
    def findMostPopulousContinent(self):
        new = CountryCatalogue.cDictionary.values()
        new = set(new)
        contPop = []
        for x in new:
            tempPop = 0
            for i in CountryCatalogue.countryCat:
                if i.getContinent() == x:
                    tempPop = tempPop + i.getPopulation()
            contPop.append((tempPop, x))
        contPop.sort(reverse=True)
        high = [(x, tempPop) for tempPop, x in contPop]
        return high[0]

    # Returns a list of countries and their population densities if they lie within the given range
    def filterCountriesByPopDensity(self, low, high):
        popDensity = []
        for i in CountryCatalogue.countryCat:
            tempPopDen = 0
            if float(high) >= i.getPopDensity() >= float(low):
                    popDensity.append((i.getPopDensity(), i.getName()))
        popDensity = sorted(popDensity, reverse=True)
        newPopDensity = [(name, popDen) for popDen,name in popDensity]
        return newPopDensity

    # Saves all the info of the Country objects in this instance to a file
    def saveCountryCatalogue(self, fileName):
        names = sorted([x.getName() for x in CountryCatalogue.countryCat])
        allCountriesList = []
        print(names)
        for i in names:
            for x in CountryCatalogue.countryCat:
                if x.getName() == i:
                    allCountriesList.append(x)
        saveFile = open(fileName, "w")
        saveFile.write("Name|Continent|Population|AreaSize|PopulationDensity\n")
        for i in allCountriesList:
            saveFile.write(i.getName()+"|"+str(i.getPopulation())+"|"+str(i.getArea())+"|"+str(i.getPopDensity())+"\n")
        count = -1
        saveFile.close()
        checkFile = open(fileName, "r")
        for i in checkFile.readlines():
            count += 1
        checkFile.close()
        if count > 0:
            return count
        else:
            return -1

