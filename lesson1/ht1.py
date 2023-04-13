class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist(self):
        distance_from_origin = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        print("Расстояние между заданной точкой и началом координат = " +
              str(distance_from_origin))


Point1 = Point(9, 3)
Point1.dist()
