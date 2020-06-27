A powerful tool for real-time observation of our simulations is the ```gnuplot``` software (available for both ```Windows``` and ```Linux```). An elegant way of integrating this software with python can be achieved through the ```subprocess module```. Before going into simulation topics, let's see some examples of how we can call ```gnuplot``` from our ```python``` code.

##### Simple plot
A very simple gnuplot code is as follows
```gp
set title '{/=30 My Simple Plot}'

set tics scale 1.5
set border linewidth 2

set xlabel '{/=20 x}'
set ylabel '{/=20 y}' rotate by 0

set xrange [-1:1]
set yrange [-1:1]

plot sin(x**2) - x**3 w l lw 2 t ''
```
and we obtain

<p align="center">
  <img src="https://github.com/williamGOC/IFCOM-II-2020/files/4823615/simple.pdf">
</p>

```python
import subprocess

proc = subprocess.Popen(['gnuplot', '-p'], shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

def simplePlot():
  pass
  
  proc.stdin.write("set title '{/=30 My Simple Plot}\n".format(self.counter).encode("utf-8"))
  
  proc.stdin.write("set tics scale 1.5\n".encode("utf-8"))
  proc.stdin.write("set border linewidth 2\n".encode("utf-8"))
  
  proc.stdin.write("set xlabel '{/=20 x}'\n".encode("utf-8"))
  proc.stdin.write("set ylabel '{/=20 y}' rotate by 0\n".encode("utf-8"))
  
   proc.stdin.write("set xrange [-1:1]\n".encode("utf-8"))
   proc.stdin.write("set yrange [-1:1]\n".encode("utf-8"))
   
   proc.stdin.write("plot sin(x**2) - x**3 w l lw 2 t ''\n".encode("utf-8"))
   
   
def main():
  pass
  
  simplePlot():
  

if __name__ == '__main__':
  main()
```
