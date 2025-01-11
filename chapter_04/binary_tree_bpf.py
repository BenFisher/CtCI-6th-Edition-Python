
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        

class BinaryTree:
    NodeCls = Node
    def __init__(self):
        self.root = None
    
    def insert(self, key, parent):
        new = self.NodeCls(key)
        
        if parent is None:
            if self.root is None:
                self.root = new
                return new
        
        # Insert - set the parent
        # push the children down
            
        
        
    
    
    