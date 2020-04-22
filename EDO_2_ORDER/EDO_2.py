import numpy as np

class EDO_Solver(object):
	"""docstring for EDO_Solver"""
	def __init__(self, f, x, v, dt):
		super(EDO_Solver, self).__init__()
		
		self.f = f
		self.x = x
		self.v = v
		self.dt = dt
		self.a = self.f(self.x)
		self.counter = 0


	def totalEnergy(self):
		return (self.v**2 + self.x**2)/2


	def eulerIteration(self):
		
		self.x += self.dt * self.v
		self.v += self.dt * self.a
		self.a = self.f(self.x)
		self.counter += 1

	
	def rk2Iteration(self):
		
		xt = self.x + (self.dt * self.v)/2
		vt = self.v + (self.dt * self.a)/2

		self.x += self.dt * vt
		self.v += self.dt * self.f(xt)
		self.a = self.f(self.x)
		self.counter += 1


	def verletIteration(self):
		
		self.v += (self.dt * self.a)/2
		self.x += self.dt * self.v
		self.a = self.f(self.x)
		self.v += (self.dt * self.a)/2
		self.counter += 1



def force(x):
	return -x



def main():

	x_0 = 1.0
	v_0 = 1.0
	dt = 0.005

	T = 10.0

	s = EDO_Solver(force, x_0, v_0, dt)

	for i in range(int(T/dt)+1):
		print("{}\t{}\t{}\t{}".format(s.counter*dt, s.x, s.v, s.totalEnergy()))
		s.verletIteration()


if __name__ == '__main__':
	main()