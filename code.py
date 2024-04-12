import dgl
import torch
import numpy as np
from dgl.data import DGLDataset
import matplotlib.pyplot as plt
import networkx as nx

class TreeDataset(DGLDataset):
    def __init__(self):
        super().__init__(name='random_trees')

    def process(self):
        self.graphs = []
        self.labels = []

        for _ in range(10):  # 10 arbres
            g, labels = self.generate_tree()
            self.graphs.append(g)
            self.labels.append(labels)

    def generate_tree(self):
        num_nodes = sum([3**i for i in range(4)])  # Sum of nodes per level up to depth 4
        edges = []
        node_features = []
        labels = []

        current_node = 0
        for level in range(3):  # Up to the penultimate level
            start_node = current_node
            end_node = start_node + 3**level
            for parent_node in range(start_node, end_node):
                num_children = np.random.randint(0, 4)  # Between 0 and 3 children
                for i in range(num_children):
                    if current_node + 1 + i < num_nodes:
                        edges.append((parent_node, current_node + 1 + i))
                current_node += 1

        # Fill with leaf data
        for i in range(num_nodes):
            if i >= current_node:
                node_features.append(np.random.rand(5))  # Leaf with random vector
                labels.append(np.random.randint(0, 2))  # Binary random label
            else:
                node_features.append(np.zeros(5))  # Not a leaf

        g = dgl.graph((np.array([e[0] for e in edges]), np.array([e[1] for e in edges])))
        g.ndata['feat'] = torch.tensor(node_features, dtype=torch.float32)
        return g, torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.graphs)

    def __getitem__(self, idx):
        return self.graphs[idx], self.labels[idx]

# Create the dataset
dataset = TreeDataset()

# Function to plot the tree using NetworkX
def plot_tree(g):
    nx_g = g.to_networkx()
    pos = nx.spring_layout(nx_g)
    nx.draw(nx_g, pos, with_labels=True, node_color=[[.7, .7, .7]])
    plt.show()

# Display two trees from the dataset
plot_tree(dataset[0][0])
plot_tree(dataset[1][0])
