import math


class GeometricObject:
    '''
    Class of Geometric Object.

    Parameters
    ----------
    x (float): Coordinate X; 0.0 by default.
    y (float): Coordinate Y; 0.0 by default.
    color (str): Color of geometric object.
    filled (boolean): True if geom. obj. is filled, False if is not.
    '''


    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        self.__x = x
        self.__y = y
        self.color = color
        self.filled = filled
    
    def set_coordinate(self, x, y):
        '''
        Sets new X and Y coordinates.
        '''


        self.__x = x
        self.__y = y

    def set_color(self, new_color):
        '''
        Sets new color of geom. obj.
        '''


        self.color = new_color
    
    def set_filled(self, new_filled):
        '''
        Sets filled of geom. obj.
        '''


        self.filled = new_filled

    def get_x(self):
        '''
        Returns X coordinate.
        '''
        return float(self.__x)
    
    def get_y(self):
        '''
        Returns Y coordinate.
        '''
        return float(self.__y)
    
    def get_color(self):
        '''
        Returns color of geom. obj.
        '''
        return self.color

    def is_filled(self):
        '''
        Returns filled of geom. obj.
        '''
        return self.filled
    
    def __str__(self):
        return f'({float(self.__x)}, {float(self.__y)})\ncolor: {self.color}\nfilled: {self.filled}'
    
    def __repr__(self):
        if self.filled:
            return f'({self.__x}, {self.__y}) {self.color} filled'
        else:
            return f'({self.__x}, {self.__y}) {self.color} no filled'
        
class Circle(GeometricObject):
    '''
    Class of Circle. Inherits a class GeometricObject.

    Parameters
    ----------
    x (float), y (float), color (str), filled (boolean) gets from the class GeometricObject.
    radius (float): Circles radius, 0.0 by default.
    '''


    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if radius > 0:
            self.__radius = radius
        else:
            self.__radius = 0.0
    
    @property
    def radius(self):
        '''
        Returns radius of circle.
        '''
        return float(self.__radius)
    
    @radius.setter
    def radius(self, new_radius):
        '''
        Sets new radius of circle if it is more than 0.
        '''
        if new_radius > 0:
            self.__radius = new_radius
        else:
            None

    def get_area(self):
        '''
        Returns circles area.
        '''
        return math.pi * self.__radius**2
    
    def get_perimetr(self):
        '''
        Returns circles perimetr.
        '''
        return 2 * math.pi * self.__radius
    
    def get_diametr(self):
        '''
        Returns circles diametr.
        '''
        return 2 * self.__radius
    
    def __str__(self):
        return f'radius: {float(self.__radius)}\n({self.get_x()}, {self.get_y()})\ncolor: {self.color}\nfilled: {self.filled}'
    
    def __repr__(self):
        if self.filled:
            return f'radius: {self.__radius} ({int(self.get_x())}, {int(self.get_y())}) {self.color} filled'
        else:
            return f'radius: {self.__radius} ({int(self.get_x())}, {int(self.get_y())}) {self.color} no filled'

class Rectangle(GeometricObject):
    '''
    Class of Rectangle. Inherits a class GeometricObject.

    Parameters
    ----------
    x (float), y (float), color (str), filled (boolean) gets from the class GeometricObject.
    width (float): Rectangles width, 0.0 by default.
    height (float): Rectangles height, 0.0 by default.
    '''


    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):
        super().__init__(x, y, color, filled)
        if width > 0:
            self.width = width
        else:
            self.width = 0.0

        if height > 0:
            self.height = height
        else:
            self.height = 0.0

    def set_width(self, new_width):
        '''
        Sets new rectangles width if it is more than 0.
        '''
        if new_width > 0:
            self.width = new_width
        else:
            None

    def set_height(self, new_height):
        '''
        Sets new rectangles height if it is more than 0.
        '''
        if new_height > 0:
            self.height = new_height
        else:
            None

    def get_width(self):
        '''
        Returns rectangles width.
        '''
        return float(self.width)
    
    def get_height(self):
        '''
        Returns rectangles height.
        '''
        return float(self.height)
    
    def get_area(self):
        '''
        Returns rectangles area.
        '''
        return float(self.width * self.height)
    
    def get_perimetr(self):
        '''
        Returns rectangles perimetr.
        '''
        return float(self.width * 2 + self.height * 2)
    
    def __str__(self):
        return f'width: {self.get_width()}\nheight: {self.get_height()}\n({self.get_x()}, \
{self.get_y()})\ncolor: {self.color}\nfilled: {self.filled}'
    
    def __repr__(self):
        if self.filled:
            return f'width: {self.width} height: {self.height} ({int(self.get_x())}, \
{int(self.get_y())}) {self.color} filled'
        else:
            return f'width: {self.width} height: {self.height} ({int(self.get_x())}, \
{int(self.get_y())}) {self.color} no filled'
