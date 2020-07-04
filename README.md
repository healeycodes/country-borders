# country-borders

A fun experiment with networked graphs and country land borders.

<br>

This repository shows some examples of:

- Displaying graphs with `networkx`/`matplotlib.pyplot`
- Finding the shortest path (BFS) between vertices (e.g. France to China)
- Building a graph of all the non-islands of the world

<br>

### All the countries that France touches

`france.py` builds a graph and dynamically outputs:

```
France is connected to 8 countries.
They are Andorra, Belgium, Germany, Italy, Luxembourg, Monaco, Spain, Switzerland.
The shortest path from France to China is: France -> Germany -> Poland -> Russian Federation -> China.
```

and displays:

![A networked graph of all the countries that France touches](https://github.com/healeycodes/country-borders/blob/master/france-connections.png)

<br>

### The non-islands of the world

`non-islands.py`

![A networked graph of all the non-islands -- it's a little squished together](https://github.com/healeycodes/country-borders/blob/master/squished-non-islands.png)

<br>

### License

MIT.

_This site or product includes Country Borders data available from https://www.geodatasource.com_
