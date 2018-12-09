#!/usr/bin/env python3

class Cake:
    pass

cake = Cake()

print(cake)
print(isinstance(cake, Cake))
print(isinstance(cake, object))


class Bath_bun(Cake):
    pass

bath_bun = Bath_bun()

print(bath_bun)
print(isinstance(bath_bun,Bath_bun))
print(isinstance(bath_bun, Cake))
print(isinstance(bath_bun, object))

class Yeast(Bath_bun):
    pass

class Raisins(Bath_bun):
    pass

yeast = Yeast()
raisins = Raisins()

print(yeast)
print(isinstance(yeast, Yeast))
print(isinstance(yeast, Bath_bun))
print(isinstance(yeast, object))

print(raisins)
print(isinstance(raisins, Raisins))
print(isinstance(raisins, Bath_bun))
print(isinstance(raisins, object))

print(isinstance(raisins, Yeast))
print(isinstance(yeast, Raisins))