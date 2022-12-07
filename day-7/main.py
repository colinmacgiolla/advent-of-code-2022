#!/bin/python


class Node(object):
    
    def __init__(self) -> None:
        self.name = None
        self.nodes = []
        self.data = []
        self.prev = None
    
    def find_node(self, name):
        for child in range(0,len(self.nodes)):
            if (self.nodes[child].name == name):
                return self.nodes[child]
        return None
    
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
    fs.data.append( ("test.txt",12345) )
    
    fs = fs.add_node()
    fs.name = 'child1'
    fs.data.append( ("test2.txt",12345) )

    
    print(fs.get_node_path())
    root = fs.goto_root()


    return 0

if __name__ == "__main__":
    main()