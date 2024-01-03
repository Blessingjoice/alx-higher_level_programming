#!/usr/bin/python3
"""defines a class square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of the sides of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the Square
        Args:
            size (int): size of sides of square
            position iof the new square
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the square's area

        Returns:
            Area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """getter of size
        Returns:
           The size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size
        Args:
            value (int): The size of the sides of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """
        Gets the current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets the position of the square
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square

        Returns:
            None
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
