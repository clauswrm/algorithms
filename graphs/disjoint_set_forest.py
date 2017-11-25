class Node:
    """ Class that represents a node in a tree """

    i = 0  # Class vaiable used to uniquely name each node

    def __init__(self, x, y):
        """ Constructs a node from the cell at coordinates (x, y) """
        self.coord = (x, y)
        self.parent = self
        self.rank = 0
        self.name = chr((Node.i % 26) + 65)  # Names start at ASCII 65 = 'A'
        Node.i += 1

    def find_set(self):
        """ Finds the parent of the node, thereby flattening the tree structure """
        if self.parent != self:
            self.parent = self.parent.find_set()
        return self.parent

    @staticmethod
    def link(own_parent, other_parent):
        """ Joins two trees by making one parent the parent of the other based on their rank """
        if own_parent.rank > other_parent.rank:
            other_parent.parent = own_parent
        else:
            own_parent.parent = other_parent
            if own_parent.rank == other_parent.rank:
                other_parent.rank += 1

    def union(self, other):
        """ Finds the parent of both nodes and joins their trees """
        if self.parent != other.parent:
            self.link(self.find_set(), other.find_set())

    def __bool__(self):
        """ Used in make_set_forest to make sure there is a node """
        return True

    def __str__(self):
        """ Returns the name of the parent node """
        return self.parent.name

    def __repr__(self):
        return '<Node: name=' + self.name + ' rank=' + str(self.rank) + '>'
