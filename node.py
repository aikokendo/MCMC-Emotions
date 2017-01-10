
class Node:

    def __init__(self, label):
        self.parents = None
        self.children = None
        self.probability_table = None
        self.current_state = None
        self.type = None
        self.label = label

    def add_children(self, child_nodes):
        if self.children is None:
            self.children = [child_nodes]
        else:
            self.children.append(child_nodes)
    def add_parent(self, parent_nodes):
        if self.parents is None:
            self.parents = [parent_nodes]
        else:
            self.parents.append(parent_nodes)
    def get_label(self):
        return self.label
    def get_parents_labels(self):
        _string = ""
        if self.parents != None:
            for node in self.parents:
                _string += node.get_label() + " "
        return _string
    def get_children_labels(self):
        _string = ""
        if self.children != None:
            for node in self.children:
                _string += node.get_label() + " "
        return _string

    def set_prob_table(self,table):
        self.probability_table = table

    def get_probability(self):
        #as the current value of parents
        #no parents
        if self.parents is None:
            return self.probability_table[0]['prob'][0]
        else:
            #hardcoding 4 levels
            for node in self.parents:
                if self.probability_table[0]['field'] == node.label:
                    first = int(node.current_state)
                elif self.probability_table[0]['prob'][0]['field'] == node.label:
                    second = int(node.current_state)
                elif self.probability_table[0]['prob'][0]['prob'][0]['field'] == node.label:
                    third = int(node.current_state)
                elif self.probability_table[0]['prob'][0]['prob'][0]['prob'][0]['field'] == node.label:
                    fourth = int(node.current_state)
        return self.probability_table[first]['prob'][second]['prob'][third]['prob'][fourth]['prob'][0]


    def print_node(self):
        print("node with label " + self.label + " has current state " + str(self.current_state) + " and is a " + self.type + " node.")