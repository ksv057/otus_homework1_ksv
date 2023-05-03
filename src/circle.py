from src.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Expected radius > 0, got {radius}')
        self.radius = radius
        self.name = 'Circle'

    def get_area(self):
        return round(3.14 * self.radius ** 2)

    def get_perimeter(self):
        return round(2 * 3.14 * self.radius)
