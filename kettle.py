# encapculation example with cigarrets and process lighting up the cigarette or kettle

class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def swith_on(self):
        self.on = True

# Two line space after class definition

kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

phillips = Kettle("Phillips", 18.99)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, phillips.make, phillips.price))
# Models: Kenwood = 12.75, Phillips = 18.99

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood,phillips))

# Class is the template for creating objects
# Object is the instance of the Class
# Method a function defined in the class
# Attribute a variable bound to an insance of a class

# States on and off swith_on method involved
print(phillips.on)
phillips.swith_on()
print(phillips.on)

Kettle.swith_on(kenwood)
print(kenwood.on)

print("*" * 20)

kenwood.power = 1.5
print(kenwood.power)
# print(phillips.power)

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"

print(kenwood.power_source)
print(phillips.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(phillips.__dict__)
"""
{'__module__': '__main__', 'power_source': 'atomic', '__init__': <function Kettle.__init__ at 0x031F9420>, 'swith_on': <function Kettle.swith_on at 0x031F9468>, '__dict__': <attribute '__dict__' of 'Kettle' objects>, '__weakref__': <attribute '__weakref__' of 'Kettle' objects>, '__doc__': None}
{'make': 'Kenwood', 'price': 12.75, 'on': True, 'power': 1.5, 'power_source': 'gas'}
{'make': 'Phillips', 'price': 18.99, 'on': True}
"""

# Finish at 113 class attributes, next methods part 1