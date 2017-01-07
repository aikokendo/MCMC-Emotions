
class Node:

    def __init__(self, label):
        self.parents = None
        self.children = None
        self.probability_table = None
        self.current_state = None
        self.label = label

    def add_children(self, child_nodes):
        if self.children == None:
            self.children = [child_nodes]
        else:
            self.children.append(child_nodes)
    def add_parent(self, parent_nodes):
        if self.parents == None:
            self.parents = [parent_nodes]
        else:
            self.parents = self.parents.append(parent_nodes)
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
