#se usará numpy para facilitar todo lo relacionado a los calculos vectoriales
from numpy import linalg, linspace, meshgrid, sqrt, array
from math import floor, ceil
from _01matrices_diagonales import soluciones_diagonales
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors 


def soluciones(a,b,c,d):
    #creamos la matriz que define la ecuacion diferencial
    A = array([[a,b],
            [c,d]])
    #obtenemos los eigenvalores y los eigenvectores asociados
    eigenvalores, eigenvectores = linalg.eig(A)
    #cambio de coordenadas
    P = eigenvectores
    #matriz inversa
    Pinversa = linalg.inv(P)

    Lambd = Pinversa.dot(A.dot(P))
    eigen1, eigen2 = P[:,0], P[:,1]
    #usamos las funciones techo y piso para que no queden muchos decimales 
    if abs(floor(Lambd[0][0])-Lambd[0][0])<abs(ceil(Lambd[0][0])-Lambd[0][0]):
        lambda1 = floor(Lambd[0][0])
    else:
        lambda1 = ceil(Lambd[0][0])

    if abs(floor(Lambd[1][1])-Lambd[1][1])<abs(ceil(Lambd[1][1])-Lambd[1][1]):
        lambda2 = floor(Lambd[1][1])
    else:
        lambda2 = ceil(Lambd[1][1])
    #graficamos las soluciones bonitas usando la funcion que grafica ecuaciones definidas por matrices diagonales
    sol_bonitas = soluciones_diagonales(lambda1, lambda2)

    #obtenemos las soluciones originales
    #intervalos
    x = linspace(-15,15, 100)
    y = linspace(-15,15,100)
    #creamos pares en el cuadrante creado arriba
    X,Y = meshgrid(x,y)
    #definimos la ecuacion dif
    ejex = (a*X)+(b*Y)
    ejey = (c*X)+(d*Y)
    #norma de cada vector (rapidez) para poder hacer el degradado en el dibujo
    rapidez = sqrt(ejex**2 + ejey**2)
    t_vals = linspace(-10, 10, 2)
    #usamos streamplot para dibujar el campo vectorial (ecu dif)
    plt.figure(figsize=(9,8))
    norma_color = mcolors.Normalize(vmin=-rapidez.max() * 0.2, vmax=rapidez.max())
    plt.streamplot(X,Y, ejex, ejey, density=1, color = rapidez, cmap ='gist_heat_r', norm=norma_color)
    plt.title(rf'Soluciones Originales de la ecuacion: $\dot{{x}} = {a}x_1+{b}x_2, {c}x_1+{d}x_2$')
    plt.axhline(0, color='black', lw=1, alpha=0.3)
    plt.axvline(0, color='black', lw=1, alpha=0.3)
    plt.plot(t_vals * eigen1[0], t_vals * eigen1[1], color='green', linestyle='--', alpha=0.5,linewidth=1.5, label=f'Vector Propio $\lambda={eigenvalores[0].real:.1f}$')
    plt.plot(t_vals * eigen2[0], t_vals * eigen2[1], color='blue', linestyle='--',alpha=0.5,  linewidth=1.5, label=f'Vector Propio $\lambda={eigenvalores[1].real:.1f}$')
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])

    plt.legend()
    plt.show()
    return


#Aqui las pruebas 
def main(a,b,c,d):
    soluciones(a,b,c,d)
if __name__ == "__main__":
    main(1,1,4,1)