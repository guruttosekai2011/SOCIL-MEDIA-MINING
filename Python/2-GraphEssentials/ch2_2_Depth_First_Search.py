# -*- coding: utf-8 -*-


S_Node = "v1"


"""
sample network
--Tree--

       v1
       |
   v2-----v3
   |       |
v4---v5 v6---v7


--Tree2--

           v1
            |
     v2----v3----v4
      |           |
   v5---v6     v7---v8
    |           |
 v9---v10   v11---v12

"""


def get_exampletree():

    Tree = {
        "v1" : ["v2", "v3"],    
        "v2" : ["v4", "v5"],    
        "v3" : ["v6", "v7"],    
        "v4" : [], 
        "v5" : [],    
        "v6" : [],    
        "v7" : [] 
        }


    Tree2 = {
        "v1" : ["v2", "v3", "v4"],
        "v2" : ["v5", "v6"],
        "v3" : [],
        "v4" : ["v7", "v8"],
        "v5" : ["v9", "v10"],
        "v6" : [],
        "v7" : ["v11", "v12"],
        "v8" : [],
        "v9" : [],
        "v10": [],
        "v11": [],
        "v12": []
        }


    return Tree, Tree2



def DFS(tree):

    Order = []
    stack = [S_Node] 
    
    while stack:
        node = stack.pop()
        if node not in Order:
            Order.append(node)
            New_node = set(tree[node]) - set(Order)
            stack.extend(New_node)
            
    return Order 

if __name__ == '__main__':

    Tree, Tree2 = get_exampletree()
    #Search_order = DFS(Tree)    
    Search_order = DFS(Tree2)    
    print Search_order


