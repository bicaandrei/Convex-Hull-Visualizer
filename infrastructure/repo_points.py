from domain.Points import Points
import random

class RepoPoints:

    def __init__(self):

        self.__point_list = []

    def add_point(self, point):

        self.__point_list.append(point)

    def delete_all_points(self):

        self.__point_list.clear()

    def createRandomPoints(self, n):

        for i in range(0, n):
            point_x = random.randint(100, 700)
            point_y = random.randint(100, 700)
            point = Points(point_x, point_y)
            self.__point_list.append(point)

    def get_all_points(self):

        points = []
        for point in self.__point_list:
            points.append(point)
        return points