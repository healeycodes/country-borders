# country-borders

> My blog post: https://healeycodes.com/practical-intro-to-graphs/

<br>

Calculating the path between two countries with the least border crossings.

<br>

This repository shows some examples of:

- Consuming CSV data and building multiple graphs
- Displaying graphs with `networkx`/`matplotlib.pyplot`
- Finding the shortest path (Breadth-First Search) between vertices (e.g. France to China)
- Building a graph of all the non-islands of the world

<br>

### The shortest path between France and China

`fr-to-cn.py` builds multiple graphs and dynamically outputs:

```
France is connected to 8 countries.
They are Andorra, Belgium, Germany, Italy, Luxembourg, Monaco, Spain, Switzerland.
The shortest path from France to China is: France -> Germany -> Poland -> Russian Federation -> China.
```

and displays:

![A line of nodes, FR-DE-PL-RU-CN](https://github.com/healeycodes/country-borders/blob/master/fr-to-cn.png)

<br>

### The non-islands of the world

`non-islands.py` builds the same graphs, culls the islands, and displays:

![A networked graph of all the non-islands](https://github.com/healeycodes/country-borders/blob/master/squished-non-islands.png)

<br>

### License

MIT.

_This site or product includes Country Borders data available from https://www.geodatasource.com_
