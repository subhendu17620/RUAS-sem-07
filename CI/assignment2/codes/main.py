import random
import operator
import math
import matplotlib.pyplot as plt

from ACO import ACO, Graph


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
                      color='m', length_includes_head=True)

    plt.xlim(0, max(x) * 1.1)
    plt.ylim(0, max(y) * 1.1)
    plt.show()


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


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


def main(n_cities=10, n_ants=10, alpha=1, beta=5, rho=0.5, q=1, max_iter=100, strategy=0):

    cities, points = create_cities(n_cities)
    plot(points, [], False)
    cost_matrix = []
    rank = len(cities)

    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)

    aco = ACO(n_ants, max_iter, alpha, beta, rho, q, strategy)
    # aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 1)

    graph = Graph(cost_matrix, rank)
    path, cost, bests = aco.solve(graph)
    print('cost: {}, path: {}'.format(cost, path))
    plot(points, path)

    #  plotting best cost of each generation vs iteration
    plt.plot(bests)
    plt.show()


main(50, 20,  1.0, 10.0, 0.5, 10, 150, 1)
