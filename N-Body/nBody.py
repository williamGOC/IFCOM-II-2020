import numpy as np
import matplotlib.pyplot as plt

from pybody import *



def totalForce(element, system):
	"""
	Total force acting on the body "element" which is in the body 
	system "system"

	Keyword Arguments:
	system  ---> is a list object with each element as body object
	element ---> is a body object 

	Return  ---> 1 x 2 numpy array.
	"""
	pass
	force = np.array([0, 0], dtype=float)

	copySystem = copy(system)
	copySystem.remove(element)

	for elemNow in copySystem:
		force += element.gravitationForce(elemNow)

	return force



def farceSystem(system, K, nbodies):
	"""
	Creates a copy of a system with generalized coordinates offset 
	by a quantity "K"

	Keyword Arguments:
	system  ---> is a list object with each element as body object
	K       ---> is a N x 2 numpy array
	nbodies ---> is a int (numbert of bodies)

	Return: list object with a copy of each element as body object
	"""
	pass
	copySystem = [copy(system[i]) for i in range(nbodies)]
	updateSystem(copySystem, K, nbodies)

	return copySystem



def updateSystem(system, K, nbodies):
	"""
	Creates a system with generalized coordinates offset 
	by a quantity "K"

	Keyword Arguments:
	system  ---> is a list object with each element as body object
	K       ---> is a N x 2 numpy array
	nbodies ---> is a int (numbert of bodies)
	"""
	pass
	for i in range(nbodies):
		system[i].setR(system[i].rVec + K[i])
		system[i].setV(system[i].vVec + K[nbodies + i])
	


def F(system):
	"""
	This function calculates the generalized force acting on each 
    body of our system.
	
	Keyword Arguments:
	system ---> is a list object with each element as body object.

	Return: N x 2 numpy array object with the generalized forces.
	"""
	pass
	GenericV = [element.vVec for element in system]
	GenericF = [totalForce(element, system) for element in system]
	return np.array(GenericV + GenericF)




def stepRK4(F, system, h, nbodies):
	"""
	Implementation of Runge-Kutta Algorithm of 4-order.

	Keyword Arguments:
	F      ---> N x 2 numpy array object with the generalized forces.
	system ---> is a list object with each element as body object.
    h      ---> float object.

    Return: N x 2 numpy array object with the correction in generalized coordinates.
	"""
	pass
	K1 = h * F(system)
	K2 = h * F(farceSystem(system, K1/2, nbodies))
	K3 = h * F(farceSystem(system, K2/2, nbodies))
	K4 = h * F(farceSystem(system, K3, nbodies))
	return (K1 + 2 * (K2 + K3) + K4)/6


def adaptativePass(F, system, h, nbodies, prec=1e-6):
	"""
	Implementation of adaptive steps with interpolation.

	Keyword Arguments:
	F      ---> N x 2 numpy array object with the generalized forces.
	system ---> is a list object with each element as body object.
    h      ---> float object.

    Return: tuple object.
	"""
	pass
	rate = 1.0 + 1e-10
	while rate >= 1.0 + 1e-10:
		h /= rate
		dX12 = stepRK4(F, system, h, nbodies)
		dX1 = dX12 + stepRK4(F, farceSystem(system, dX12, nbodies), h, nbodies)
		dX2 = stepRK4(F, system, 2*h, nbodies)
		epsilon = (dX2 - dX1)/30
		error = max([ np.linalg.norm(np.array(epsilon[k])) for k in range(nbodies)])
		rate = (error/(h*prec))**0.25
	h_approx = min(h/(rate+1e-10), 2*h)
	dX = dX2 + (dX2-dX1)/15
	return dX, 2*h, h_approx


def main():
	
	t_0 = 0.0  			# Start of time interval.
	t_N = 2.0           # End of time interval.
	t = t_0             # Initialization time.
	
	h = 1e-3			# Step's size.
	h_now = h 			# Initialization step's size.

	
	# Creation of the bodies of our system.
	A = body(1, np.array([-1, 1], dtype=float))
	B = body(1, np.array([-1, -1], dtype=float))
	C = body(1, np.array([1, -1],dtype=float))
	D = body(1, np.array([1, 1],dtype=float))
	
	system = [A, B, C, D]
	N = len(system)

	# upgrade steps.
	while t <= t_N:
		dX, h_now, h_approx = adaptativePass(F, system, h, N)
		t += h_now
		updateSystem(system, dX, N)
		h = h_approx

		# printer system
		printer = ''
		for element in system:
			printer += '{}\t{}\t'.format(element.rVec[0], element.rVec[1])
		print(printer)
		printer = ''


if __name__ == '__main__':
	main()