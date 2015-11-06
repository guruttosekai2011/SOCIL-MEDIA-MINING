# -*- coding: utf-8 -*-

import ch2_2_Depth_First_Search as ch2_2


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


def BFS(tree):

    Order = []
    stack = [S_Node]
    
    while stack:
        node = stack.pop(0)
        if node not in Order:
            Order.append(node)
            New_node = set(tree[node]) - set(Order)
            stack.extend(New_node)
            
    return Order 


if __name__ == '__main__':

    Tree, Tree2 = ch2_2.get_exampletree()
    #Search_order = BFS(Tree)
    Search_order = BFS(Tree2)
    print Search_order








