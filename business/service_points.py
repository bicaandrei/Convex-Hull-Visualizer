from convexHull.convexHullAlghorithm import convexHull
from domain.Points import Points

class ServicePoints:

    def __init__(self, repo_points):

        self.__RepoPoints = repo_points

    def add_point(self, x, y):

        point = Points(x, y)
        self.__RepoPoints.add_point(point)

    def delete_all_points(self):

        self.__RepoPoints.delete_all_points()

    def createRandomPoints(self, n):

        self.__RepoPoints.createRandomPoints(n)

    def get_all_points(self):

        points = self.__RepoPoints.get_all_points()
        return points

    def solveHull(self):

        point_list = self.__RepoPoints.get_all_points()
        hull = convexHull(point_list, len(point_list))
        return hull