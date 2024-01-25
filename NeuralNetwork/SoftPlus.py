import numpy as np
import matplotlib.pyplot as plt



def softplus(x):
    return np.log(1 + np.exp(x))

def sigmoid(x):
    return np.exp(x)/(1+np.exp(x)) 
xP = []
yP = []
points = [[0,3],[3,4],[6,8],[9,20],[13,8],[16,4],[19,0]]
for p in points:
    xP.append(p[0])
    yP.append(p[1])
m = 1
b = 0 


# Node
pderivM = 0
pderivB = 0
epochs = 0
L = 0.0001

while epochs < 50000:
    print(f'EPOCH: {epochs}')
    pderivM = 0
    pderivB = 0
    for p in points:
        pderivM += 2*p[0]*(m*softplus(p[0])+b-p[1])
        pderivB += 2*(m*softplus(p[0])+b-p[1])
    m-=L*pderivM
    b-=L*pderivB
    epochs+=1

start_points = 0
end_points = 20
iter = 1000
x = np.linspace(start_points, end_points, iter) 
y = m*softplus(x)+b


plt.plot(xP, yP, 's')
plt.plot(x,y)
plt.show()

