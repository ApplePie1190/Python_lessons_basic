class Road:
    unit_weight = 25
    depth = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self):
        return int(self._length * self._width * self.unit_weight * self.depth / 1000)


road_1 = Road(20, 5000)
print(road_1.road_weight())
road_2 = Road(10, 8000)
print(road_2.road_weight())
