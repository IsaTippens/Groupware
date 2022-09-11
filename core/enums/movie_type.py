from enum import Enum

class MovieType(Enum):
    BASIC2D = 1
    BASIC3D = 2
    IMAX2D = 3
    IMAX3D = 4

    def __str__(self):
        if (self.value == 1):
            return "2D"
        elif (self.value == 2):
            return "3D"
        elif (self.value == 3):
            return "IMAX 2D"
        elif (self.value == 4):
            return "IMAX 3D"
        return "INVALID"