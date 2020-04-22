import matplotlib.pyplot as plt
import numpy as np
import gif


@gif.frame
def plot_bodies(data):
	pass
	

	plt.figure(figsize=(5, 3), dpi=100)

	plt.title(r'$N = 3$', fontsize=20)

	plt.xlim(xmin=-2, xmax=3.1)
	plt.ylim(ymin=-3, ymax=3.3)
	
	plt.xlabel(r'$x(t)$', fontsize=15)
	plt.ylabel(r'$y(t)$', fontsize=15)

	plt.plot(data[:,0], data[:,1], label=r'$m_{1}=150$')
	plt.plot(data[:,2], data[:,3], label=r'$m_{2}=200$')
	plt.plot(data[:,4], data[:,5], label=r'$m_{3}=250$')

	plt.legend(fontsize=10)
	plt.tight_layout()

	


def main():
	pass

	dataName = "data_N=3.dat"
	name_gif = "./move.gif"
	data = np.loadtxt(dataName, dtype=float)
	N = len(data)

	frames = []
	for i in range(N):
		frame = plot_bodies(data[:i])
		frames.append(frame)

	gif.save(frames, name_gif, duration=50)



if __name__ == '__main__':
	main()
