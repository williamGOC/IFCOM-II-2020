# EDO of second order.
Consider a body of unitary mass under the action of an elastic force. The motion of this body can be described by the ordinary second order differential equation:

<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/79963697-1575f400-8460-11ea-9479-0641ce1b8aea.gif">
</p>

the general solution of this equation is given by.

<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/79971027-2d527580-846a-11ea-82c7-deca44ba1ded.gif">
</p>
So let's take a look at some of the numerical solutions we can give to this problem.

<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/79975732-d355ae00-8471-11ea-8af3-ec187d7fc758.png">
</p>

The most significant of these solutions is what happens with the total energy of the system. We can see how when using ```Euler's method``` the calculated system energy moves away from the exact system energy (dashline), the same happens with the ```Runge-Kutta method``` but to a lesser extent. When a behavior similar to the previous one occurs with the energy of a system, it is said that the method by which the energy was calculated is ```non-conservative```. We can see how when using the ```Verlet's method```, the energy oscillates around its real value

<p align="center">
  <img src="https://user-images.githubusercontent.com/37045478/79978696-b40d4f80-8476-11ea-81f8-664babd9da67.png">
</p>
