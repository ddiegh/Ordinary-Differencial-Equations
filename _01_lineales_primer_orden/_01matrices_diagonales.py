from numpy import linspace, meshgrid, sqrt
import matplotlib.pyplot as plt

def soluciones(lambda1, lambda2):
    # Intervalos
    x_range = linspace(-10, 10, 100)
    y_range = linspace(-10, 10, 100)
    X, Y = meshgrid(x_range, y_range)
    
    # Ecuación diferencial 
    U = lambda1 * X
    V = lambda2 * Y
    
    # Calcular la magnitud (velocidad) para el gradiente de color
    velocidad = sqrt(U**2 + V**2)
    
    # Aseguramos el estilo clásico de fondo blanco
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Dibujar flujo con el mapa de colores 'plasma' (perfecto para fondo blanco)
    strm = ax.streamplot(X, Y, U, V, color=velocidad, cmap='gist_heat_r', 
                         linewidth=1.2, density=1)
        
    # PUNTO SINGULAR: Borde negro para que contraste con el fondo blanco
    ax.scatter(0, 0, color='red', s=100, zorder=5, 
               linewidth=0.8, label='Punto Singular (0,0)')
    
    # Dibujar los ejes coordenados (ahora en negro translúcido)
    ax.axhline(0, color='black', lw=1, alpha=0.3)
    ax.axvline(0, color='black', lw=1, alpha=0.3)
    
    # Estética del título y los límites
    ax.set_title(rf"Soluciones a la ecuación diferencial: $\dot{{x}} = ({lambda1}x_1, {lambda2}x_2)$")
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    
    # Leyenda con sombra para que se despegue del fondo
    ax.legend(loc='upper right', frameon=True, shadow=True)

    plt.tight_layout()
    plt.show()