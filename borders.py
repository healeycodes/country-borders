import csv
from collections import Iterable, deque


def flatten(l):
    # flatten a nested list
    # https://stackoverflow.com/a/2158532

    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def find_shortest_path(graph, start, end):
    # breadth first search (BFS)
    # adapted from https://www.python.org/doc/essays/graphs/

    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for country in graph[at]:
            if country not in dist:
                dist[country] = [dist[at], country]
                q.append(country)

    raw_path = dist.get(end)
    return list(flatten(dist.get(end)))


country_border_graph = {}
country_code_lookup = {}

with open('borders.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for row in reader:
        country_code_lookup[row[0]] = row[1]
        country_a = row[0]
        country_b = row[2]

        if country_a in country_border_graph:
            country_border_graph[country_a].append(country_b)
        else:
            country_border_graph[country_a] = [country_b]
