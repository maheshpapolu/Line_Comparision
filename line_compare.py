import logging
import math

logging.basicConfig(filename="line_comp.log", filemode="w")


class Line:
    """
    initialising the coordinates of line and finding the length
    """

    def __init__(self, x1, y1, x2, y2):
        """
        Initialize the attribute
        :param x1:coordinates of x-axis for the 1st point
        :param x2:coordinates of x-axis for the 2nd point
        :param y1:coordinates of y-axis for the 1st point
        :param y2:coordinates of y-axis for the 2nd point
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_length(self):
        """
        finding the length
        :return:
        """
        try:
            length = math.sqrt((self.x2 - self.x1) ^ 2 + (self.y2 - self.y1) ^ 2)
            return length
        except ValueError:
            logging.exception("something went wrong")

    @staticmethod
    def check_equality(line_1, line_2):
        """
        create a function name as check_equality for check the line length based on end points
        :param line_1:
        :param line_2:
        :return:
        """
        if line_1 == line_2:
            return True
        else:
            return False


if __name__ == "__main__":
    # Creating object for Line class and calling calculation function
    try:
        line_1 = Line(2, 5, 6, 7)
        line_2 = Line(2, 5, 6, 7)
        print(line_1.calculate_length())
        print(line_2.calculate_length())
        print(line_1.check_equality(line_1.calculate_length(), line_2.calculate_length()))

    except ValueError:
        logging.exception("please enter integer value")
