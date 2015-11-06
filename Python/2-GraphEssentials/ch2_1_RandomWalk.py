# -*- coding: utf-8 -*-

import numpy as np
import random

MAX_STEP = 10
S_Node = 0

def generate_weighted_graph():

    """
    - non-directed graph -
          v0   v1   v2   v3   v4   v5
     v0  0.0  0.2  0.2  0.3  0.2  0.1      
     v1  0.1  0.0  0.3  0.3  0.1  0.2                  
     v2  0.3  0.2  0.0  0.1  0.2  0.2                
     v3  0.1  0.4  0.2  0.0  0.2  0.1                
     v4  0.2  0.2  0.2  0.2  0.0  0.2                  
     v5  0.2  0.1  0.1  0.3  0.3  0.0            
    """
    
    Adj_Matrix = np.array([
    [0.0,  0.2,  0.2,  0.3,  0.2,  0.1],
    [0.1,  0.0,  0.3,  0.3,  0.1,  0.2],
    [0.3,  0.2,  0.0,  0.1,  0.2,  0.2],
    [0.1,  0.4,  0.2,  0.0,  0.2,  0.1],
    [0.2,  0.2,  0.2,  0.2,  0.0,  0.2],
    [0.2,  0.1,  0.1,  0.3,  0.3,  0.0]
    ])

    return Adj_Matrix    


def choice_node(prob_list):

    border = random.uniform(0, 1)
    prob_sum = 0.0

    for i in xrange(len(prob_list)):
        prob_sum += prob_list[i]
        if border < prob_sum:
            return i
    
    return i


def Random_Walk(M):

    state = 0
    node = S_Node
    Path = [S_Node]

    while state < MAX_STEP:
        state += 1
        
        target = choice_node(M[node])
        
        node = target
        Path.append(node)
    
    return Path


if __name__ == "__main__":

    Matrix = generate_weighted_graph()
    Path = Random_Walk(Matrix)

    print Path

