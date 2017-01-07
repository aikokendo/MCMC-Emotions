import node

class Graph:
    def __init__(self,nodes,edges):
        temp = dict()
        for node_val in nodes:
            temp[node_val] = (node.Node(node_val))
        for edge_val in edges:
            temp[edge_val[0]].add_children(temp[edge_val[1]])
            temp[edge_val[1]].add_parent(temp[edge_val[0]])
        self.nodes = temp

    def print_graph(self):
        for node in self.nodes:
            print("Node " + self.nodes[node].get_label() + " Children: " + self.nodes[node].get_children_labels() + " Parents: " + self.nodes[node].get_parents_labels())
