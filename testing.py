from catalogue import *

zim = CountryCatalogue("continent.txt", "data.txt")
print(zim.findCountry("China"))
print(zim.setAreaOfCountry("Chna", 4343346))
print(zim.getCountriesByPopulation())
print(zim.getCountriesByArea("Asia"))
print(zim.findMostPopulousContinent())
print(zim.deleteCountry("China"))
print(zim.filterCountriesByPopDensity(-100, -1))
print(zim.saveCountryCatalogue("bob.txt"))
