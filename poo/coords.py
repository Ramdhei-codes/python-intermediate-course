import math

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coord):
        try:
            diff_x = (self.x - other_coord.x )**2
            diff_y = (self.y - other_coord.y)**2
        except:
            print('Eso no es una coordenada')

        return math.sqrt(diff_x + diff_y)


coord_1 = Coordinate(20, 5.5)
coord_2 = Coordinate(30, 123.2)

print(coord_1.distance(coord_2))