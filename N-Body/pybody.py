"""
Author: William Gabriel Carreras Oropesa
Date: April 19, 2020, Neuqué, Argentina

module body: This module has implemented a series of functions and objects 
			 that will be useful when solving the problem of the N bodies.
"""

# necessary modules
import numpy as np
from copy import copy

class body(object):

    def __init__(self, mass, rVec):
        super(body, self).__init__()
	
	self.mass = mass
	self.rVec = rVec
	self.vVec = np.array([0, 0], dtype=float)
	

    def __str__(self):
	return "body object: M = {}, R = ({}, {}), V = ({}, {})".format(self.mass, 
			self.rVec[0], self.rVec[1], self.vVec[0], self.vVec[1])
	
    def setV(self, newV):
	self.vVec = newV


    def setR(self, newR):
	self.rVec = newR


    def gravitationForce(self, P):
	return (P.mass * (P.rVec - self.rVec))/np.linalg.norm(P.rVec - self.rVec)**3
