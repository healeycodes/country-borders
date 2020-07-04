import graph
from borders import country_border_graph, country_code_lookup, find_shortest_path

france = country_border_graph["FR"]
france_names = [country_code_lookup[code] for code in france]
print(f'France is connected to {len(france_names)} countries.')
print(f'They are {", ".join(france_names)}.')

path = find_shortest_path(country_border_graph, 'FR', 'CN')
path_names = [country_code_lookup[code] for code in path]
print(f'The shortest path from France to China is: {" -> ".join(path_names)}.')

from_verts = []
to_verts = []
for i in range(0, len(france)):
    from_verts.append('FR')
    to_verts.append(country_border_graph['FR'][i])

graph.show(from_verts, to_verts)
