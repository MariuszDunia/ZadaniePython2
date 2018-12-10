#!/usr/bin/env python3

class Cake():
    pass

cake = Cake()

print(cake)
print(isinstance(cake, Cake))
print(isinstance(cake, object))


class BathBun(Cake):
    pass

bath_bun = BathBun()

print(bath_bun)
print(isinstance(bath_bun, BathBun))
print(isinstance(bath_bun, Cake))
print(isinstance(bath_bun, object))

class Yeast(BathBun):
    pass

class Raisin(BathBun):
    pass

yeast = Yeast()
raisin = Raisin()

print(yeast)
print(isinstance(yeast, Yeast))
print(isinstance(yeast, BathBun))
print(isinstance(yeast, object))

print(raisin)
print(isinstance(raisin, Raisin))
print(isinstance(raisin, BathBun))
print(isinstance(raisin, object))

print(isinstance(raisin, Yeast))
print(isinstance(yeast, Raisin))