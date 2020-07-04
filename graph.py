import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def show(from_verts, to_verts):
    df = pd.DataFrame(
        {'from': from_verts, 'to': to_verts})
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    # TODO: check https://stackoverflow.com/a/54876985 for why the graph is squished
    nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="o",
            linewidths=4, font_size=25, font_color="grey", font_weight="bold", width=4, edge_color="grey", dpi=1000)
    plt.show()
