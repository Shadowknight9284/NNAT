import numpy as np
import matplotlib.pyplot as plt
from NodeClass import node

xP = []
yP = []
points = [[0,3],[3,4],[6,8],[9,20],[13,8],[16,4],[19,0]]
for p in points:
    xP.append(p[0])
    yP.append(p[1])
    
# 2 nodes
# Node1 m1 b1
m1 = -1
b1 = 0
Node1 = node(m1,b1,p)
    
    
    
# Node2 m2 b2 
m2 = 1
b2 = 0
Node2 = node(m1,b1,p)

# m3*Node1 +m4*Node2 + b3 

