A powerful tool for real-time observation of our simulations is the ```gnuplot``` software (available for both ```Windows``` and ```Linux```). An elegant way of integrating this software with python can be achieved through the ```subprocess module```. Before going into simulation topics, let's see some examples of how we can call ```gnuplot``` from our ```python``` code.

##### Simple plot
A very simple gnuplot code is as follows
```gp
set xrange [-1:1]
set yrange [-1:1]

plot sin(x**2) + cos(x)**2 w l lw 2 t ''
```
