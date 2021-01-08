class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance_from_origin(self):
        dist = ((self.x**2) + (self.y**2))**0.5
        print ("The distance of the point from origin is " + str(dist) + ".")

pointA = point(5,5)
pointB = point(10,10)
pointA.distance_from_origin()
pointB.distance_from_origin()