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
  
 if __name__ == '__main__':
	main()
 ```
