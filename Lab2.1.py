# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:40:06 2020

@author: Den
"""

import random
from math import sin, cos, pi
import matplotlib.pyplot as plt
import timeit


def generateX(n, time, W):
    x = [0] * time

    for i in range(1, n + 1):
        amplitude = random.random()
        phase = random.random()

        for t in range(time):
            x[t] += amplitude * sin(W / i * (t + 1) + phase)
    return x
 

def calculateDFT(signal: list, N):
    
    coeff = lambda i, j : 2 * pi * i * j / N
    
    summ = lambda i : sum((signal[j] * complex(cos(coeff(i,j)), sin(-coeff(i,j))) for j in range(N)))
        
    return [summ(i) for i in range(N)]

def main():
    n = 8
    N = 1024
    W = 1200
    
    xValues = generateX(n, N, W)
    
    time_0 = timeit.default_timer()
    
    dftValues = calculateDFT(xValues, N)
    
    print("DFT пораховано за: {}".format(timeit.default_timer() - time_0))
    
    figure, (plotXValues, plotDFTValues) = plt.subplots(2, figsize=(20, 20))
    plotXValues.plot(range(N), xValues, "b")
    plotXValues.title.set_text("Згенерований сигнал X")
    plotDFTValues.plot(range(N), dftValues, "r")
    plotDFTValues.title.set_text("DFT")
    plt.show()


if __name__ == '__main__':
    main()
