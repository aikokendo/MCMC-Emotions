import node
import random

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

    def graph_size(self):
        return len(self.nodes)

    def fill_nodes(self,e):
        mNodes = []
        for node in self.nodes:
            nodeLabel = self.nodes[node].label
            if nodeLabel in e:
                self.nodes[node].type = 'E'
                self.nodes[node].current_state = e[nodeLabel]
            else:
                self.nodes[node].type = 'M' #montecarlo
                self.nodes[node].current_state = random.sample([True,False],1)[0]
                mNodes.append(node)
        return mNodes

    def get_prob(self,node):
        return self.nodes[node].get_probability()

    def get_prob_children(self,node):
        prob = 1
        if self.nodes[node].children is not None:
            for node in self.nodes[node].children:
                prob = prob * node.get_probability()
        return prob

    def set_state(self,state,node):
        self.nodes[node].current_state = state

    def print_nodes(self):
        for node in self.nodes:
            self.nodes[node].print_node()

    def get_x_node(self,x):
        for node in self.nodes:
            if self.nodes[node].label == x:
                return node

    def add_prob_table(self,z,table):
        for node in self.nodes:
            if self.nodes[node].label == z:
                self.nodes[node].set_prob_table(table)