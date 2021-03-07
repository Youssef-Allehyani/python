import math
class Pizza:
    def __init__(self,Radius,ingredients):
        self.ingredients = ingredients
        self.Radius = Radius

    def __str__(self):
        return f"Pizza ingredients are {self.ingredients}"
    def area(self):
        area_Size = Pizza.Size_of_Pizza(self.Radius)
        Size = self.Radius

        if Size >= 4  and Size < 6 :
            return f'small size {area_Size}'
        elif Size >=6 and Size <8 :
            return f'medium size {area_Size}'
        elif  Size >= 8 and Size <10 :
            return f'large size {area_Size}'
        else:
            return f'huge size  {area_Size}'
    @staticmethod
    def Size_of_Pizza(radius):
       return radius**2 * math.pi
        


Pizza_1 = Pizza( 4 ,['tomatoes','cheass'])
pizza_2 =Pizza(6,['mushrooms','olives','onions','green pepper'])
pizza_3 = Pizza(8,['tomatoes','cheass ','green pepper'])
pizza_4 = Pizza(10,['tomatoes','cheass ','mushrooms'])

print('Pizza number one ',Pizza_1, ' and it\'s', Pizza_1.area())
print('Pizza number two ',pizza_2 , 'and it\'s', pizza_2.area())
print('Pizza number  three ',pizza_3 , 'and it\'s', pizza_3.area())
print('Pizza number foure ',pizza_4 , 'and it\'s', pizza_4.area())




    