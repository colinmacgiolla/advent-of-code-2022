#!/bin/python


class Node(object):
    
    def __init__(self) -> None:
        self.name = None
        self.nodes = []
        self._data = []
        self._size = 0
        self._dir_names = []
        self.prev = None
    
    def find_nodes_by_size(self, size):
        node_list = []
        
        if self._size <= size:
            node_list.append(self)
            
        if len(self.nodes) > 0:
            for child in range(0,len(self.nodes)):
                node_list.extend( self.nodes[child].find_nodes_by_size(size) )
        return node_list
    
    def list_node_sizes(self):
        node_list = []
        node_list.append( (self.name,self._size) )
            
        if len(self.nodes) > 0:
            for child in range(0,len(self.nodes)):
                node_list.extend( self.nodes[child].list_node_sizes() )
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
            parent._size += size
            # then we need to move up a tier
            parent = parent.prev
    

def main():

    with open('C:\\Users\\colinmac\\Documents\\Git Projects\\advent-of-code-2022\\day-7\\input\\data.txt') as f:
        raw_input = f.read()
    
    fs = None
    
    for line in raw_input.split('\n'):
        if line.startswith("$"):
            if "cd .." in line:
                # move up a node
                fs = fs.prev
                pass
            elif "cd /" in line:
                if fs is None:
                    fs = Node()
                    fs.name = '/'
                else:
                    fs = fs.goto_root()
            elif "cd" in line:
                fs = fs.add_node()
                fs.name = line.split()[2]
            else:
                # should be ls so do nothing
                pass

            
        else:
            # process output
            if line.startswith("dir"):
                fs._dir_names.append(line.split()[1])
                pass
            else:
                size, filename = line.split()
                size = int(size)
                fs.add_file(filename,size)
                

    root = fs.goto_root()
    things = root.find_nodes_by_size(100000)
    
    print("Part 1: Sum of directory sizes, where the size is at most 100000: %d" % sum([obj._size for obj in things]) )
    
    
    dir_list = root.list_node_sizes()
    fs_max = 70000000
    required = 30000000
    target_reduction = required - (fs_max - root._size)
    print("Part 2: We need to reduce disk space by: %d" % target_reduction)
    
    candidate_pool = []
    for dir_name, size in dir_list:
        if size >= target_reduction:
            candidate_pool.append( (dir_name,size) )
    print("%d directories meet the required criteria" % len(candidate_pool))
    print("Recommend to delete %s with size %d" %  min(candidate_pool,key=lambda t:t[1]) )
            

    return 0

if __name__ == "__main__":
    main()