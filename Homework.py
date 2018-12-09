class Plant:
    pass


plant = Plant()


print(plant)
print(isinstance(plant, Plant))
print(isinstance(plant, object))


class BreedingPlant(Plant):
    pass


class WildPlant(Plant):
    pass


breedingPlant = BreedingPlant()
wildPlant = WildPlant()

print(breedingPlant)
print(isinstance(breedingPlant, BreedingPlant))
print(isinstance(breedingPlant, Plant))
print(isinstance(breedingPlant, object))

print(wildPlant)
print(isinstance(wildPlant, WildPlant))
print(isinstance(wildPlant, Plant))
print(isinstance(wildPlant, object))

print(isinstance(wildPlant, BreedingPlant))
print(isinstance(breedingPlant, WildPlant))


class Wheat(BreedingPlant):
    pass


class Rye(BreedingPlant):
    pass


wheat = Wheat()
rye = Rye()

print(wheat)
print(isinstance(wheat, Wheat))
print(isinstance(wheat, BreedingPlant))
print(isinstance(wheat, WildPlant))
print(isinstance(wheat, Plant))
print(isinstance(wheat, object))

print(rye)
print(isinstance(rye, Rye))
print(isinstance(rye, BreedingPlant))
print(isinstance(rye, WildPlant))
print(isinstance(rye, Plant))
print(isinstance(rye, object))


class BlueBerries(WildPlant):
    pass


class BlackBerries(WildPlant):
    pass


blueBerries = BlueBerries()
blackBerries = BlackBerries()

print(blueBerries)
print(isinstance(blueBerries, BlueBerries))
print(isinstance(blueBerries, BreedingPlant))
print(isinstance(blueBerries, WildPlant))
print(isinstance(blueBerries, Plant))
print(isinstance(blueBerries, object))

print(blackBerries)
print(isinstance(blackBerries, BlackBerries))
print(isinstance(blackBerries, BreedingPlant))
print(isinstance(blackBerries, WildPlant))
print(isinstance(blackBerries, Plant))
print(isinstance(blackBerries, object))
