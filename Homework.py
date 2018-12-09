class Plants:
    pass


plants = Plants()


print(plants)
print(isinstance(plants, Plants))
print(isinstance(plants, object))


class BreedingPlants(Plants):
    pass


class WildPlants(Plants):
    pass


breedingPlants = BreedingPlants()
wildPlants = WildPlants()

print(breedingPlants)
print(isinstance(breedingPlants, BreedingPlants))
print(isinstance(breedingPlants, Plants))
print(isinstance(breedingPlants, object))

print(wildPlants)
print(isinstance(wildPlants, WildPlants))
print(isinstance(wildPlants, Plants))
print(isinstance(wildPlants, object))

print(isinstance(wildPlants, BreedingPlants))
print(isinstance(breedingPlants, WildPlants))


class Wheat(BreedingPlants):
    pass


class Rye(BreedingPlants):
    pass


wheat = Wheat()
rye = Rye()

print(wheat)
print(isinstance(wheat, Wheat))
print(isinstance(wheat, BreedingPlants))
print(isinstance(wheat, WildPlants))
print(isinstance(wheat, Plants))
print(isinstance(wheat, object))

print(rye)
print(isinstance(rye, Rye))
print(isinstance(rye, BreedingPlants))
print(isinstance(rye, WildPlants))
print(isinstance(rye, Plants))
print(isinstance(rye, object))


class BlueBerries(WildPlants):
    pass


class BlackBerries(WildPlants):
    pass


blueBerries = BlueBerries()
blackBerries = BlackBerries()

print(blueBerries)
print(isinstance(blueBerries, BlueBerries))
print(isinstance(blueBerries, BreedingPlants))
print(isinstance(blueBerries, WildPlants))
print(isinstance(blueBerries, Plants))
print(isinstance(blueBerries, object))

print(blackBerries)
print(isinstance(blackBerries, BlackBerries))
print(isinstance(blackBerries, BreedingPlants))
print(isinstance(blackBerries, WildPlants))
print(isinstance(blackBerries, Plants))
print(isinstance(blackBerries, object))
