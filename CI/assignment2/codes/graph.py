import random
import operator
import matplotlib.pyplot as plt


class Graph(object):
    def __init__(self, cost_matrix: list, rank: int):
        """
        :param cost_matrix:
        :param rank: rank of the cost matrix
        """
        self.matrix = cost_matrix
        self.rank = rank
        self.pheromone = [[1 / (rank * rank)
                           for j in range(rank)] for i in range(rank)]


def create_cities(n_cities):
    cities = []
    points = []
    for i in range(n_cities):
        x = random.uniform(0, 1000)
        y = random.uniform(0, 1000)
        cities.append(dict(index=i+1, x=x, y=y))
        points.append((x, y))
    points.append(points[0])
    return cities, points


def plot(points, path: list, showPath=True):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    y = list(map(operator.sub, [max(y) for i in range(len(points))], y))
    plt.plot(x, y, 'co')
    if showPath:
        for _ in range(1, len(path)):
            i = path[_ - 1]
            j = path[_]
            plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i],
                      color='r', length_includes_head=True)

    plt.xlim(0, max(x) * 1.1)
    plt.ylim(0, max(y) * 1.1)
    plt.show()


def main():

    cities, points = create_cities(40)
    plot(points, [], False)


main()
