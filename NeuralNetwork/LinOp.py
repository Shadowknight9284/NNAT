import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
import pandas as pd

def processPoints(points): #SCALE
    xP = []
    yP = []
    for p in points:
        xP.append(p[0])
        yP.append(p[1])
    return [xP, yP]
def processPoints(df):
    xP = df['X_1'].to_numpy()  
    yP = df['Y_1'].to_numpy() 
    return [xP ,yP]
df = pd.read_csv('points.csv')

