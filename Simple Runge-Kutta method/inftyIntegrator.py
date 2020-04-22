from math import sin,cos,exp,sqrt,log,tanh
from numpy import arange
import matplotlib.pyplot as plt

# Parâmetros da exibição dos gráficos
plt.rcParams['xtick.labelsize'] = 24
plt.rcParams['ytick.labelsize'] = 24
plt.rcParams['axes.labelsize'] = 28

gama, omega = 1.0, 10.0

def g(x,u):
    t = 0.5*log((1.0+u)/(1.0-u))
    f = 1.0/(x**2+t**2)
    return f/(1.0-u**2)

def passo_rk4(f,x,t,h):            # Calcula um passo no método de RK4
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    return (k1+2.0*(k2+k3)+k4)/6.0


def main():
    a = 0.            # Início do intervalo
    b = tanh(8.)      # Final do intervalo
    xa = 1.0          # Condição inicial, ou seja, x(a)

    N = 1000000            # Número de passos da integração numérica
    h = (b-a)/N        # Tamanho do passo da integração

    xrk4 = xa
    u_rk4 = []
    t_rk4 = []
    x_rk4 = []

    u = a
    t = 0.5*log((1.0+u)/(1.0-u))
    u_rk4.append(u)
    t_rk4.append(t)
    x_rk4.append(xrk4)
    for i in range(1,N+1):   # Realizando a integração numérica
        xrk4 += passo_rk4(g,xrk4,u,h)
        u = u + h
        t = 0.5*log((1.0+u)/(1.0-u))
        u_rk4.append(u)
        t_rk4.append(t)
        x_rk4.append(xrk4)
    
    plt.figure(figsize=(12,9))
    plt.xlim(0.,8.)
    plt.plot(t_rk4,x_rk4) 
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.show() 

if __name__ == '__main__':
    main()
