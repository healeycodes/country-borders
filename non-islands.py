import graph
from borders import country_border_graph

from_verts = []
to_verts = []
for country in country_border_graph:
    for i in range(0, len(country_border_graph[country])):
        if country_border_graph[country][0] == '':
            # skip islands
            continue
        from_verts.append(country)
        to_verts.append(country_border_graph[country][i])

graph.show(from_verts, to_verts)
