# N-Body problem:
### pybody module
 The ```pybody``` module is currently under construction but it has implemented ```body``` type objects that represent isolated bodies in space. Next we will see how with the help of these objects we can easily solve the problem of ```N interacting bodies```, but first let's familiarize ourselves with the ```body``` objects.
 ```python
 from pybody import body
 import numpy as np
 
 def main():
 	pass
  
 	# body masses
 	M_1 = 150.0
 	M_2 = 200.0
  	
	    # body positions
	    R_1 = np.array([1, 2], dtype=float)
	    R_2 = np.array([0, 3], dtype=float)
  	
	    # creation of two body type objects
	    star_1 = body(M_1, R_1)
	    star_2 = body(M_2, R_2)
  
  	# force between the bodies per mass
  	f_12 = star_1.gravitationForce(star_2)
  	f_21 = star_2.gravitationForce(star_1)

   	print(star_1)
   	print(star_2)

   	print("F_12 = f_12 * M_1 = {}".format(f_12 * star_1.mass))
   	print("F_21 = f_21 * M_2 = {}".format(f_21 * star_2.mass))
  
 if __name__ == '__main__':
	main()
 ```
the output os this program is:
```console
body object: M = 150.0, R = (1.0, 2.0), V = (0.0, 0.0)
body object: M = 200.0, R = (0.0, 3.0), V = (0.0, 0.0)
F_12 = f_12 * M_1 = [-10606.6017178  10606.6017178]
F_21 = f_21 * M_2 = [ 10606.6017178 -10606.6017178]
```
We can also set the position and speed of a body using some methods of the body class
 ```python
 from pybody import body
 import numpy as np
 
 def main():
  	pass
  
  	# body mass
  	M = 150.0
  
  	# body position
  	R = np.array([1, 2], dtype=float)
  
  	# creation of two body type objects
  	star = body(M, R)
  
  	print("The body is in the position R = {}, and has velocity V = {}\n".format(star.rVec, star.vVec))
  
  	newR = np.array([2, 2], dtype=float)
  	newV = np.array([1,-1], dtype=float)
  
  	star.setR(newR)
  	star.setV(newV)
  
  	print("The body is in the position R = {}, and has velocity V = {}".format(star.rVec, star.vVec))
  
 if __name__ == '__main__':
	main()
 ```
the output is:
```console
The body is in the position R = [1. 2.], and has velocity V = [0. 0.]

The body is in the position R = [2. 2.], and has velocity V = [ 1. -1.]
```
Now that we are familiar with the ```body class```, let's see how we can solve the problem of the ```N interacting bodies```.

### N-interacting bodies
To solve the problem of N interacting bodies under the effects of gravitational attraction, it is necessary to solve the following system of differential equations

<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/79851559-ded6a580-839b-11ea-98fc-a398c7252e19.gif">
</p>

To solve this problem we will use the fourth order ```Runge-Kutta algorithm```. We must first decompose the entire system of ```N``` vector equations into one of ```2 x d x N``` scalar equations (here ```d``` is the dimension of the problem). Then we can notice that we are in the presence of a **Multi-variable Runge-Kutta Problem**.

```python
# Multi-variable Runge-Kutta algorithm.
def stepRK4(X, F, h):
	"""
	Keyword Arguments:
	X     --->  np.array
	F     --->  np.array
	h     --->  float
	"""
	pass
	
	K1 = h * F(X)
	K2 = h * F(X + K1/2)
	K3 = h * F(X + K2/2)
	K4 = h * F(X + K3)
	
	return (K1 + 2 * (K2 + K3) + K4)/6
```
In our problem we have to look for an alternative implementation of the algorithm. Firstly we have,

<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/79925935-06685500-8412-11ea-99e7-50f86219ce22.gif">
</p>

The above equations can be represented as a ```numpy array```. The next step is to build a function that is capable of offsetting the generalized coordinates of a body object. For this, functions ```updateSystem``` and ```farceSystem``` were implemented, which are documented in the file ```nBody.py```. Finally, our implementation of the **Multi-variable Runge-Kutta** algorithm with ```adaptive steps``` is a simple extension of the one shown in classes for the case of a dimension.
```python
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
```
### complilation
```console
groot@iron:~$ python3 nBody.py >> name_output.dat
```
