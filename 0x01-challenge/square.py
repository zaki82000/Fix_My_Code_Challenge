class Square:
    """
    A class representing a square.

    Attributes:
    - width (int): The width of the square.
    - height (int): The height of the square.

    Methods:
    - __init__(width=0, height=0): Initializes the Square object with the specified width and height.
    - area_of_my_square(): Calculates and returns the area of the square.
    - perimeter_of_my_square(): Calculates and returns the perimeter of the square.
    - __str__(): Returns a string representation of the Square object in the format 'width/height'.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Square object with the specified width and height.

        Parameters:
        - width (int): The width of the square.
        - height (int): The height of the square.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates and returns the perimeter of the square.

        Returns:
        - int: The perimeter of the square.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the Square object in the format 'width/height'.

        Returns:
        - str: A string representation of the Square object.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print("Square:", s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
