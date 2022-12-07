#!/bin/python


class Node(object):
    
    def __init__(self) -> None:
        self.name = None
        self.nodes = []
        self._data = []
        self._size = 0
        self.prev = None
    
    def find_node_by_name(self, name):
        # FIXME
        for child in range(0,len(self.nodes)):
            if (self.nodes[child].name == name):
                return self.nodes[child]
        return None
    
    def find_nodes_by_size(self, size):
        node_list = []
        
        if self._size >= size:
            node_list.append(self)
            
        if len(self.nodes) > 0:
            for child in range(0,len(self.nodes)):
                node_list.extend( self.nodes[child].find_nodes_by_size() )
       
        return node_list
    
    def prev(self):
        return self.prev
    
    def goto_root(self):
        if self.prev == None:
            return self
        else:
            return self.prev.goto_root()
    
    def add_node(self):
        # Adding a node will always push you further down that branch of the tree
        # to add multiple nodes to the same level, you will need to move back up one
        new_node = Node()
        self.nodes.append(new_node)
        new_node.prev = self
        return new_node
    
    def add_file(self, name, size):
        self._data.append( (name, size) )
        self._size += size

        # have to parse back up the tree
        # to update the sizes
        parent = self.prev
        while parent is not None:
            node = self.prev
            node._size += size
            parent = node.prev
    
    def get_node_path(self):
        
        path = []
        path.append(self.name)
        
        parent = self.prev
        path.append(parent.name)
        while parent.prev is not None:
            node = self.prev
            path.append(node.name)
            if node.prev is None:
                parent.prev = None
                
        path.reverse()
        return path
            
        



def main():

    #with open('C:\\Users\\colinmac\\Documents\\Projects\\advent-of-code-2022\\day-7\\input\\data.txt') as f:
    #    raw_input = f.read()
    
    fs = Node()
    fs.name = '/'
    fs.add_file( "test.txt",12345 )
    
    fs = fs.add_node()
    fs.name = 'child1'
    fs.add_file( "test2.txt",12345 )
    
    fs = fs.prev
    fs = fs.add_node()
    fs.name = 'child2'
    fs.add_file( "test2.2.txt", 2)

    
    print(fs.get_node_path())
    root = fs.goto_root()






    return 0

if __name__ == "__main__":
    main()