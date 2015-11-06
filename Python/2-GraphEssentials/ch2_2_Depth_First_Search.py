# -*- coding: utf-8 -*-


S_Node = "v1"


def get_exampletree():

    """
           v1
           |
       v2-----v3
       |       |
    v4---v5 v6---v7
    """

    Tree = {
        "v1" : ["v2", "v3"],    
        "v2" : ["v4", "v5"],    
        "v3" : ["v6", "v7"],    
        "v4" : [], 
        "v5" : [],    
        "v6" : [],    
        "v7" : [] 
    }

    return Tree


def DFS(tree):

    Order = []
    stack = [S_Node] 
    
    while stack:
        node = stack.pop()
        if node not in Order:
            Order.append(node)
            New_node = set(Tree[node]) - set(Order)
            stack.extend(New_node)
            
    return Order 

if __name__ == '__main__':

    Tree = get_exampletree()
    Search_order = DFS(Tree)    
    print Search_order


