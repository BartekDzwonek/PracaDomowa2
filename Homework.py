class Wizzards:
    pass


wizzards = Wizzards()


print(wizzards)
print(isinstance(wizzards, Wizzards))
print(isinstance(wizzards, object))


class GoodWizzards(Wizzards):
    pass


class BadWizzards(Wizzards):
    pass


goodWizzards = GoodWizzards()
badWizzards = BadWizzards()

print(goodWizzards)
print(isinstance(goodWizzards, GoodWizzards))
print(isinstance(goodWizzards, Wizzards))
print(isinstance(goodWizzards, object))

print(badWizzards)
print(isinstance(badWizzards, BadWizzards))
print(isinstance(badWizzards, Wizzards))
print(isinstance(badWizzards, object))

print(isinstance(badWizzards, GoodWizzards))
print(isinstance(goodWizzards, BadWizzards))


class Gandalf(GoodWizzards):
    pass


class Merlin(GoodWizzards):
    pass


gandalf = Gandalf()
merlin = Merlin()

print(gandalf)
print(isinstance(gandalf, Gandalf))
print(isinstance(gandalf, GoodWizzards))
print(isinstance(gandalf, BadWizzards))
print(isinstance(gandalf, Wizzards))
print(isinstance(gandalf, object))

print(merlin)
print(isinstance(merlin, Merlin))
print(isinstance(merlin, GoodWizzards))
print(isinstance(merlin, BadWizzards))
print(isinstance(merlin, Wizzards))
print(isinstance(merlin, object))


class Saruman(BadWizzards):
    pass


class Baltazar(BadWizzards):
    pass


saruman = Saruman()
baltazar = Baltazar()

print(saruman)
print(isinstance(saruman, Saruman))
print(isinstance(saruman, GoodWizzards))
print(isinstance(saruman, BadWizzards))
print(isinstance(saruman, Wizzards))
print(isinstance(saruman, object))

print(baltazar)
print(isinstance(baltazar, Baltazar))
print(isinstance(baltazar, GoodWizzards))
print(isinstance(baltazar, BadWizzards))
print(isinstance(baltazar, Wizzards))
print(isinstance(baltazar, object))
