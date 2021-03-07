class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls(['mushrooms','olives','onions','green pepper'])    
    @classmethod
    def matgherita(cls):
        return cls(['mozare'])
    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"

Pizza_1 = Pizza(['tomatoes','cheass '])
pizza_2 = Pizza.veg()
Pizza_3 = Pizza.matgherita()

print('Pizza number one ',Pizza_1)
print('Pizza number two',pizza_2)
