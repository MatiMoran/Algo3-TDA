
# A
# la idea seria no recorrer caminos que veamos q no sean factibles, en el ejemplo
# [ -2 -3 3 ]
# [ -5 -10 1 ]
# [ 10 30 -5 ]
# deberiamos dejar de probar todas las posibilidades q tengan como primer paso hacia abajo ya que nos quedamos a 0 de vida
# similarmente solo podemos seguir a la derecha y no podriamos bajar a -10 por el mismo motivo asi que vamos descartando decisiones.
# el algortimo obtendria como parametro la matriz y una vida inicial, si no encontramos una solucion con esa vida probamos con vida + 1
# hasta encontrar algun camino, como vimos en clase este tipo de problema tiene complejidad O(n*m)

# B y C
# f(i,j) = max (1, 1 - m[i,j]) si i = rows-1 y j = cols-1
# f(i,j) = max (1, f(i, j + 1) - m[i,j]) si i = rows-1
# f(i,j) = max (1, f(i + 1, j) - m[i,j]) si j = cols-1
# f(i,j) = max (1, min (f(i+1,j), f(i,j+1)) - m[i,j])

# D
def sol(matriz):
    rows = len(matriz)
    cols = len(matriz[0])

    matriz_minima_vida = [ [ -1 for y in range(cols) ] for x in range(rows) ]

    matriz_minima_vida[rows-1][cols-1] = 1 - matriz[rows-1][cols-1] if 1 - matriz[rows-1][cols-1] >= 1 else 1

    for j in range(cols-2, -1, -1):
        matriz_minima_vida[rows-1][j] = matriz_minima_vida[rows-1][j+1] - matriz[rows-1][j]
        if matriz_minima_vida[rows-1][j] < 1:
            matriz_minima_vida[rows-1][j] = 1

    for i in range(rows-2, -1, -1):
        matriz_minima_vida[i][cols-1] = matriz_minima_vida[i+1][cols-1] - matriz[i][cols-1]
        if matriz_minima_vida[i][cols-1] < 1:
            matriz_minima_vida[i][cols-1] = 1

    for i in range(rows-2, -1, -1):
        for j in range(cols-2, -1, -1):
            matriz_minima_vida[i][j] = min(matriz_minima_vida[i+1][j], matriz_minima_vida[i][j+1]) - matriz[i][j]
            if matriz_minima_vida[i][j] < 1:
                matriz_minima_vida[i][j] = 1

    print(matriz_minima_vida)


sol([[-2,-3,3],[-5,-10,1],[10,30,-5]])

# complejidad temporal es O(n*m)
# su complejidad espacial es O(n*m) pero se podria reducir a O(min(n,m)) simplemente en vez de almacenar la matriz de minimas vidas
# ir descartando cada col o fila segun cual sea mas grande e ir calculando una fila o columna a la vez con los valores anteriores.
