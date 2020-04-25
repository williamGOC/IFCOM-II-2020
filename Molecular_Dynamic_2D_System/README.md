# Molecular dynamics in 2D gas
This code can be used for the study of classical gases with weak interaction (Van der Waals). The evolution of the system is done by the ```Speed Verlet algorithm```.

```python
...
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
 
 ...
 
  def verletIterator(self):
    pass
      
    self.momentum += self.acelerat * self.passTime / 2
    self.position += self.momentum * self.passTime
    self.acelerat = self.force(self.position)
    self.momentum += self.acelerat * self.passTime / 2
    self.counter += 1
 ...
```


<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/80276255-e8268180-86bd-11ea-9601-08f15d60e73d.gif">
</p>
