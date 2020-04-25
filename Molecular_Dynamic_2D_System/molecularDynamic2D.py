import gif
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from random import randint

# Global variables os the system
L = 27.386127875258307
NC = 15
RHO = 0.3
EMPTY = -1
N = 225

class particles(object):
	"""docstring for particles"""
	def __init__(self, force, passTime):
		super(particles, self).__init__()
		
		self.force = force
		self.passTime = passTime
		self.counter = 0

		self.position = np.zeros((N, 2), dtype=float)
		self.momentum = np.zeros((N, 2), dtype=float)
		self.acelerat = np.zeros((N, 2), dtype=float)

		for i in range(N):
			self.position[i][0] = (i % NC) * L / (NC + 1)
			self.position[i][1] = (i / NC) * L / (NC + 1)
			self.momentum[i][0] = 1.1 if (randint(1,10)%2 == 0) else -1.1 
	

		self.acelerat = self.force(self.position)



	def __call__(self):
		pass

		self.verletIterator()
		self.peridCondition()



	def __del__(self):
		pass

		del self.passTime
		del self.counter
		del self.force
		del self.position
		del self.acelerat
		del self.momentum



	def verletIterator(self):
		pass

		self.momentum += self.acelerat * self.passTime / 2
		self.position += self.momentum * self.passTime
		
		self.acelerat = self.force(self.position)
		
		self.momentum += self.acelerat * self.passTime / 2

		self.counter += 1


	def peridCondition(self):
		pass

		size = 1.0 / L
		self.position -= np.floor(self.position * size) * L

	
	@gif.frame
	def printerSystem(self):
		pass 

		plt.figure(figsize=(7, 5), dpi=100)
		plt.title('time = {:.3f}'.format(self.passTime * self.counter))

		plt.xlim(xmin=1, xmax=L)
		plt.ylim(ymin=1, ymax=L)
		plt.axis('off')

		plt.plot(self.position[:,0], self.position[:,1], linestyle='' , marker='o', markersize=2)



def minimalImage(r_i, r_j):
	pass

	r_ij = r_i - r_j
	return r_ij - L * np.round(r_ij / L) 


def d_ij(r_i, r_j):
	pass

	return np.linalg.norm(minimalImage(r_i, r_j))



def f_ij(r_i, r_j):
	pass
	
	d = d_ij(r_i, r_j)
	v_ij = 48 * ((d ** -14) - (d ** -8) / 2)

	return v_ij * minimalImage(r_i, r_j)


def f(position):
	pass

	force = np.zeros((N, 2), dtype=float)

	for i in range(N):
		for j in range(i+1, N):
			force[i] += f_ij(position[i], position[j])
			force[j] -= f_ij(position[i], position[j])

	return force




def main():
	pass

	sys = particles(f, 0.005)
	name_gif = "./move.gif"

	frames = []
	for i in range(1000):
		frame = sys.printerSystem()
		frames.append(frame)
		sys()

	gif.save(frames, name_gif, duration=200)
	

if __name__ == '__main__':
	main()