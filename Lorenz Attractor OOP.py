# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:07:25 2017

@author: Ahmed Shalabi
"""
import numpy as np
import matplotlib.pyplot as plt
#Implement a Lorentz_Attractor class 

class Lorenz_Attractor(object):
    def __init__(self , sigma , beta , rho , Initial_r ):
        self.Sigma = sigma
        self.Beta = beta
        self.Rho = rho
        self.r = Initial_r
        
    def f(self):
        x =self.r[0]
        y = self.r[1]
        z = self.r[2]
        x_prime = self.Sigma * ( y - x )
        y_prime = x * ( self.Rho - z ) - z
        z_prime = x * y - ( self.Beta * z )
        return np.array([x_prime , y_prime , z_prime ],float)
    
    def Integration(self):
        a = 0
        b = 20
        N = 1500
        h = (b-a)/N
        time_scale = np.arange(a,b,h)
        X = []
        Y = []
        Z = []
        for t in time_scale:
         
            X.append(self.r[0])
            Y.append(self.r[1])
            Z.append(self.r[2])
            rTemp = self.r
            
            k1 = h*self.f()
            self.r = self.r+ 0.5*k1
            k2 = h*self.f()
            self.r = rTemp
            self.r = self.r + 0.5*k2
            k3 = h*self.f()
            self.r = rTemp
            self.r = self.r+k3
            k4=h*self.f()
            self.r = rTemp
            self.r += (k1+2*k2+2*k3+k4)/6
                        
        fig = plt.figure()
        fig.add_subplot(111, projection='3d')   # Don't forget to add a 3d axes!
        plt.plot(X,Y,Z)
        plt.tight_layout()
        plt.show()
        
        
L1 = Lorenz_Attractor(10, 8/3, 28, [2,3,4])
L1.Integration()

