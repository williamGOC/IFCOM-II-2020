from math import sin,cos,exp,sqrt,log
from numpy import arange
import sys
import matplotlib.pyplot as plt

# Parâmetros da exibição dos gráficos
plt.rcParams['xtick.labelsize'] = 24
plt.rcParams['ytick.labelsize'] = 24
plt.rcParams['axes.labelsize'] = 28

RC = float(sys.argv[1])

def vinquad(t):
    vin = 1.
    if int(2*t)%2 == 1:
        vin = -1.
    return vin

def fquad(x,t):
    return (vinquad(t) - x)/RC


def passo_rk4(f,x,t,h):            # Calcula um passo no método de RK4
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    return (k1+2.0*(k2+k3)+k4)/6.0

def sol_exata(t,a,xa):             # Válida somente para fquad
    n = int((t-a)/0.5)
    x0 = xa
    t0 = a
    sinal = 1.
    vin = sinal
    for i in range(n):
        xf = vin - (vin - x0)*exp(-0.5/RC)
        t0 = t0 + 0.5
        x0 = xf
        sinal = -sinal
        vin = sinal
    xf = vin - (vin - x0)*exp(-(t-t0)/RC)
    return xf


def main():

    a = 0.00         # Início do intervalo
    b = 10.0         # Final do intervalo
    xa = 0.0         # Condição inicial, ou seja, x(a)

    N_exato = 1000    # Número de pontos para o gráfico da solução exata
    h_exato = (b-a)/N_exato
    t_exato = arange(a,b,h_exato)
    x_exato = [] 

    for t in t_exato:  # Criando as listas para o gráfico da função
        x_exato.append(sol_exata(t,a,xa))


    N = 1000           # Número de passos da integração numérica
    h = (b-a)/N        # Tamanho do passo da integração

    xrk4 = xa
    t_rk4 = arange(a,b,h)
    x_rk4 = []

    for t in t_rk4:   # Realizando a integração numérica
        x_rk4.append(xrk4)
        xrk4 += passo_rk4(fquad,xrk4,t,h)
    
    plt.figure(figsize=(12,9))
    plt.plot(t_rk4,x_rk4,'r-',t_exato,x_exato,'bo')
    plt.xlabel("$t$")
    plt.ylabel("$V_{out}(t)$")
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()