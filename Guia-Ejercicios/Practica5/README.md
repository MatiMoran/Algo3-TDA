# Práctica 5: Recorrido mínimo

## Algoritmo de Dijkstra

### 1) st-eficientes
Dado un digrafo $D$ con pesos $c : E(D) \rightarrow N$ y dos vértices $s$ y $t$, decimos que una arista $v \rightarrow w$ es $st$-eficiente cuando $v \rightarrow w$ pertenece a algún camino mínimo de $s$ a $t$. Sea $d(·, ·)$ la función que indica el peso de un camino mínimo entre dos vértices.

(a) Demostrar que $v \rightarrow w$ es $st$-eficiente si y sólo si $d(s, v) + c(v \rightarrow w) + d(w, t) = d(s, t)$.

>$\Rightarrow$) Supongamos que $v \rightarrow w$ es $st$-eficiente. Esto significa que $v \rightarrow w$ pertenece a algún camino mínimo de $s$ y $t$, lo que implica que $d(s,t) = d(s,v) + c(v \rightarrow w) + d(w,t)$, lo cual es consecuencia directa de que $v \rightarrow w$ está en camino mínimo de $s$ a $t$.
>
>$\Leftarrow$) Supongamos que $d(s,v) + c(v \rightarrow w) + d(w,t) = d(s,t)$. Para ver que $v \rightarrow w$ es $st$-eficiente, necesitamos ver que está en un camino mínimo de $s$ a $t$. Podemos descomponer los tramos de $s \rightarrow v$ y $w \rightarrow t$ si no es camino mínimo entonces existiría un $d_{alt}(s,t) < d(s,t)$ lo que contradice la hipótesis, luego $v \rightarrow w$ es $st$-eficiente. No puede existir un camino más corto de $s$ a $t$ que no pase por $v \rightarrow w$, ya que eso contradiría la definición de $d(s, t)$ como el peso de un camino mínimo. La idea es que bajo esta condición, cualquier desviación aumentaría el costo total del camino, asegurando que $v \rightarrow w$ debe ser parte de un camino mínimo.

(b) Usando el inciso anterior, proponga un algoritmo eficiente que encuentre el mínimo de los caminos entre $s$ y $t$ que no use aristas $st$-eficientes. Si dicho camino no existe, el algoritmo retorna $\bot$.

>1. Ejecuta Dijkstra en $D$ desde $s$ para calcular $d(s,v)$ para todo $v$.
>2. Ejecuta Dijkstra en $D$ complemento desde $t$ para calcular $d(w,t)$ para todo $w$ ($D$ complemento es dar vuelta todas las aristas).
>3. Para cada arista $v \rightarrow w$ en $D$ verifica $d(s,v) + c(v \rightarrow w) + d(w,t) = d(s,t)$
>4. Marcar estas aristas como no elegibles para el cálculo de la ruta mínima en el siguiente paso.
>5. Corro Dijkstra otra vez en $D$ desde $s$ a $t$ y es el resultado.  Antes de hacer esto, necesito asegurarme de que el grafo ha sido modificado para reflejar la exclusión (o la no elección) de las aristas $st$-eficientes. Esto podría implicar ajustar el algoritmo de Dijkstra para que ignore estas aristas marcadas durante su ejecución.
    
### 2) Arista max en ruta de peso $c$
Diseñar un algoritmo eficiente que, dado un digrafo $G$ con pesos no negativos, dos vértices $s$ y $t$ y una cota $c$, determine una arista de peso máximo de entre aquellas que se encuentran en algún recorrido de $s$ a $t$ cuyo peso (del recorrido, no de la arista) sea a lo sumo $c$. 
Demostrar que el algoritmo propuesto es correcto.

>Algoritmo:
>1. Dijkstra desde $s$ en $G$ para calcular $d(s,v)$ para todo $v$ con arista menor a $c$. (ya que los pesos son positivos)
>2. Dijkstra desde $t$ en $G$ con las aristas invertidas para calcular $d(w,t)$ para todo $w$ con arista menor a $c$. (ya que los pesos son positivos)
>3. Ordenar todas las aristas $(v,w)$ según peso decreciente.
>4. Para cada arista ordenado: si $d(s,v) + c(v,w) + d(w,t) \leq c$ devolver arista.
>5. Devolver null.
        
>Demostración:
>- El algoritmo devuelve la arista que cumple con los criterios, en 4 se itera todas las aristas y si se cumple la condición devuelve arista, me asegura que es max ya que está ordenado y empiezo a recorrer desde los de más alto valor.
>- El algoritmo termina y no deja ningún arista sin verificar, examina cada arista exactamente 1 vez y Dijkstra me garantiza que las distancias son correctos sin pasar por alto ninguno, termina cuando encuentra o recorre todos.

### 3) Max 1 arista negativa
Diseñar un algoritmo eficiente que, dado un digrafo pesado $G$ y dos vértices $s$ y $t$, determine el recorrido minimo de $s$ a $t$ que pasa por a lo sumo una arista de peso negativo. 
Demostrar que el algoritmo propuesto es correcto.

>Antes del algoritmo preparamos un $G'$ que es un subgrafo de $G$ sin aristas negativas.
>
>Algoritmo:
>1. Inicializamos dos estructuras para $G'$, uno para $d_{G'}(s,v)$ o otro para $d_{G'}(v,t)$ para todos $v$ en $V$.
>2. Ejecutamos Dijkstra dos veces, una desde $s$ en $G'$ y otra en $t$ en $G'$ con aristas invertidas.
>3. Inicializo variable $minDist$ en infinito para el seguimiento del camino mínimo.
>4. Para cada arista en $G$ donde $c(v,w) < 0$ verifica si la suna de $d_{G'}(s,v) + c(v,w) + d_{G'}(w,t)$ es menor que $minDist$, si lo es, actualizo y sigo recorriendo.
>5. Finalmente hago $min(d_{G'}(s,t), minDist)$ y reconstuyo el camino mínimo que resulte.
>            
>Complejidad: Dijkstra tiene una complejidad de $O((V+E) log V)$ usando un montículo de Fibonacci. Entonces, ejecutarlo dos veces sería $O(2(V+E) log V)$ y revisar todas las aristas negativas añade $O(E)$ en el peor caso. Así que sería $O((V+E) log V + E)$, considerando $V$ vértices y $E$ aristas en total.

>Para reconstruir el camino mínimo una vez encontrado:
>Durante la ejecución de Dijkstra: mantiene un arreglo de predecesores para cada nodo. Es decir, para cada nodo $v$, guarda el nodo previo $u$ en el camino mínimo desde $s$ a $v$ (y similarmente para el camino de $t$ a $v$ con las aristas invertidas). Al encontrar el camino mínimo que incluye una arista negativa: Si el camino mínimo pasa por una arista negativa $(v, w)$, entonces hay que combinar tres partes:
>- El camino desde $s$ a $v$ utilizando el arreglo de predecesores desde $s$.
>- La arista negativa $(v, w)$.
>- El camino desde $w$ a $t$, que se obtiene invirtiendo el camino reconstruido desde $t$ a $w$ usando el arreglo de predecesores hacia $t$.

>Demostración:
>- Corrección parcial: caminos mínimos en $G'$, al usar Dijkstra nos garantiza los subcaminos minimos de $s$ hacia todos los nodos, y desde cualquier nodo hacia $t$. Ya que en $G'$ no hay aristas de peso negativo.
>- Corrección global: vemos el caso de los caminos que usan una arista negativa, checkeando todas las aristas negativas en función de los subcaminos mínimos calculados en $G'$ (sin arista negativos).
>- Finalmente, comparamos el minimo entre no usar arista negativa con una solo 1 arista negativa.

### 4) Aristas que mejoran
Sea $G$ un digrafo con pesos positivos que tiene dos vértices especiales $s$ y $t$. Para una arista $e \notin E(G)$ con peso positivo, definimos $G + e$ como el digrafo que se obtiene de agregar $e$ a $G$. Decimos que $e$ mejora el camino de $s$ a $t$ cuando $d_G (s, t) > d_{G+e} (s, t)$. 
Diseñar un algoritmo eficiente que, dado un grafo $G$ y un conjunto de aristas $E \notin E(G)$ con pesos positivos, determine cuáles aristas de $E$ mejoran el camino de $s$ a $t$ en $G$. 
Demostrar que el algoritmo es correcto.

>Algoritmo:
>1. Inicio un conjunto para guardar las aristas que mejoran.
>2. Ejecuto Dijkstra en $G$ para encontrar $d(s,t)$.
>3. Para cada arista $e$ en $E$ (que son de pesos positivos), la agrego al grafo $G$ generando el grafo $G+e$ y ejecuto Dijkstra. Si $d_{G+e}(s,t) < d(s,t)$ lo agrego al conjunto que mejora.
>4. Saco la arista e del grafo y sigo recorriendo el conjunto $E$.

>Complejidad: $O(|E| * min(n², m log(n)))$ ya que hago Dijkstra $|E|$ veces.
>
>(alternativa mejor): si calculamos $d(s,v)$ y $d(v,w)$ para todos los nodos $v$ en $G$ reduce drasticamente la cantidad de ejecución de Dijkstra. Entonces por cada arista de $E$, al tener los dos extremos y el costo, calcular el CM de $d_{G+e}(s,t)$ es $O(1)$ ya que es una cuenta y no es necesario la inserción/sacado de la arista en sí. 
        
>Demostración: pruebo cada arista de |E| y veo si mejora el camino minimo.

### 5) Aristas críticas
Sea $G$ un digrafo con pesos positivos que tiene dos vértices especiales $s$ y $t$. Decimos que una arista $e \in E(G)$ es crítica para $s$ y $t$ cuando $d_G(s, t) < d_{G−e} (s, t)$. Diseñar un algoritmo eficiente que, dado $G$, determine las aristas de $G$ que son críticas para $s$ y $t$. 
Demostrar que el algoritmo es correcto. Ayuda: pensar en el subgrafo $P$ de $G$ que está formado por las aristas de caminos mínimos de $G$ (el "grafo de caminos mínimos").

>Algoritmo:
>1. Ejecuto Dijkstra de $s$ a $t$ para obtener $d(s,v)$ para todos los $v$ en $G$.
>2. Ejecuto Dijkstra de $t$ a $s$ con las aristas invertidas para obtener $d(v,t)$ para todos los $v$ en $G$.
>3. Para cada arista de $G$, recorremos verificando la ecuación de $d(s,v) + c(v \rightarrow w) + d(w,t) = d(s,t)$. Las aristas que cumplen serán posibles aristas críticas. Usamos esta info para construir un subgrafo $P$ que consiste exclusivamente en las aristas que forman parte de algún camino mínimo de $s$ a $t$. Todas las aristas de $P$ son candidatas a ser críticas, la razón es que, por definición, si una arista no está en un camino mínimo desde $s$ a $t$, su eliminación no puede afectar la distancia mínima entre estos dos puntos.
>4. Usamos la propiedad de los predecesores/sucesores, para cada arista $(v, w)$ en el camino mínimo, mira si existe otra ruta de $v$ a $w$ que no sea más larga que la arista original. Esto puede hacerse manteniendo y consultando una estructura de datos que almacene caminos alternativos y sus respectivos pesos durante la construcción de $P$. Si no existe tal ruta alternativa, entonces la arista es crítica.
>
>(optimización): Para evitar la reconstrucción del grafo y la repetición de Dijkstra, se puede precalcular y almacenar las distancias mínimas entre todos los pares de vértices usando el algoritmo de Floyd-Warshall o repetir Dijkstra desde cada vértice. Aunque esto tiene una complejidad temporal mayor ($O(n³)$ para Floyd-Warshall y $O(n*m/log(n))$ para Dijkstra repetido), te permite responder inmediatamente si la eliminación de cualquier arista aumentaría la distancia mínima de $s$ a $t$. Esta estrategia es especialmente útil si el grafo no cambia frecuentemente y se hacen muchas consultas sobre aristas críticas.
        
>Demostración: las aristas que cumplen con la ecuación pertenecen a algún camino minimo. Como pueden haber varios caminos mínimos, esto no significa que al removerse pasaría que $d_G(s,t) < d_{G-e}(s,t)$. Entonces pueden pasar los siguientes casos:
>1. Al removerla existe otro camino minimo de mismo peso.
>2. Al remover existe otro camino de mayor peso.
>3. No hay otro camino y $st$ quedan en dos componentes conexas.

### 6) Pesos probabilisticos
No se incluye un ejercicio en particular de este tema debido a que Estadística Computacional no es correlativa con TDA. :)

## Algoritmo de Bellman-Ford y SRDs

### 7) Ciclos Puré
Para organizar el tráfico, la ciudad de Ciclos Positivos ha decidido implementar las cabinas de peaje inverso. La idea de estas cabinas es incentivar la circulación de vehículos por caminos alternativos, estableciendo un monto que se le paga a le conductore de un vehículo. Estas cabinas inversas se suman a las cabinas regulares, donde le conductore paga. La ciudad sabe que estas nuevas cabinas pueden dar lugar al negocio del "ciclo puré", que consiste en transitar eternamente por la ciudad a fin de obtener una ganancia infinito. Para evitar esta situación, que genera costos y tráfico adicional, la ciudad quiere evaluar distintas alternativas antes de llevar a la práctica.

(a) Modelar el problema de determinar si la ciudad permite el negocio del ciclo puré cuando el costo de transitar por cada cabina $i$ de peaje es $c_i$ ($c_i < 0$ si la cabina es inversa) y el costo que cuesta viajar de forma directa de cada cabina $i$ a cada cabina $j$ es $c_{ij} > 0$.

>Modelamos: cabinas como vértices en un digrafo y arista representa el costo de viajar entre cabinas. El peso de las arista representa el precio a pagar en el nodo destino, que representa una cabina, las aristas que tenga como destino una cabina regular tendrá peso positivo y las que tenga una cabina inversa como destino tienen peso negativo.

(b) Dar un algoritmo para resolver el problema del inciso anterior, indicando su complejidad temporal. 

>Algoritmo: para encontrar un ciclo negativo en principio Bellman Ford no sirve pues si el nodo inicial no alcanza todas los nodos se podría perder algún ciclo. Por eso:
>1. Agrego un nodo extra y conecto a todos los vértices con costo 0
>2. Aplico Bellman Ford desde el nuevo nodo que agregué para buscar un ciclo negativo.
>3. Si encuentra, es posible ciclo pure.
>4. Si no, es imposible.
>
>Complejidad: depende de Bellman Ford $O(n*m)$.

El sistema arrojó que ninguna de las configuraciones deseadas para desincentivar el tráfico evita el negocio de los ciclos puré. A fin de obtener cierto rédito, sugieren transformar la idea de cabinas inversas en cabinas mixtas. Cuando un vehículo pasa por una cabina mixta, se le paga a le conductore si se le cobró a le conductore en la cabina anterior; caso contrario, le conductore paga. Obviamente, sugieren que se le pague a le conductore cuando la cabina mixta sea la primera cabina recorrida.

(c) Modelar el problema de determinar si la ciudad permite el negocio de los ciclos puré cuando se aplica la nueva configuración para las cabinas. Además de la información utilizada para el problema original, ahora se conoce cuáles cabinas son mixtas: notar que el monto de cobro es $c_i$ y el monto de pago es $−c_i$ para la cabina mixta $i$ (con $c_i > 0$).

>Modelado: seguimos con el formato de cabina como nodos y aristas como la unión entre dos cabinas. Solo que ahora las cabinas serán representado como el par(int, bool) donde el int identifica la cabina y el bool si se pago en la cabina anterior. Es decir si el bool es $true$, el conductor pagó en la cabina anterior y si es $false$, el conductor cobró. Vamos a duplicar los nodos que sean las cabinas mixtas ({cabina, $true$} y {cabina, $false$}). Así al momento de conectar las aristas, si una cabina normal conecta hacia una cabina mixta, solo se hará la conexion con {cabina, $false$}, en cambio si una mixta conecta con una normal no tiene restricción en la conexión. En el caso de que se conecten dos cabinas mixtas, {cabina1, $false$} conecta con {cabina2, $true$} y viceversa, dependiendo de la acción (cobrar o pagar) realizada en la cabina de origen. Y los pesos de cada arista de cabina mixta se asigna según el valor del bool en el nodo destino.
>
>Para calcular ciclos negativos es la misma idea del inciso anterior agregando un nodo $(c0, false)$ ya que el primero se cobra.

### 8) SRD
Un sistema de restricciones de diferencias (SRD) es un sistema $S$ que tiene $m$ inecuaciones y $n$ incógnitas $x_1 ,... , x_n$. Cada inecuación es de la forma $xi − xj \leq c_{ij}$ para una constante $c_{ij} \in R$; por cada par $i, j$ existe a lo sumo una inecuación (por qué?). Para cada SRD $S$ se puede definir un digrafo pesado $D(S)$ que tiene un vértice $v_i$ por cada incógnita $x_i$ de forma tal que $v_j \rightarrow v_i$ es una arista de peso $c_{ij}$ cuando $x_i − x_j \leq c_{ij}$ es una inecuación de $S$. Asimismo, $S$ tiene un vértice $v_0$ y una arista $v_0 \rightarrow v_i$ de peso 0 para todo $1 \leq i \leq n$.

(a) Demostrar que si $D(S)$ tiene un ciclo de peso negativo, entonces $S$ no tiene solución.

>Dato: por cada par $i$, $j$ existe a lo sumo 1 inecuación porque en caso contrario tenemos 2 inecuaciones contradictoria o redundante, lo que implica solución no única o inconsistente.
>
>Lo demostramos por el absurdo:
Supongamos que $D(S)$ tiene un ciclo de peso negativo y existe una solución única.
Supongamos que el ciclo incluye los nodos $c = (v_1, v_2, ..., v_k)$ donde $v_k = v_1$. El nodo $v_0$ no puede ser parte de ciclos pues no tiene arista entrante. El ciclo corresponde a la siguiente sistema de inecuaciones:
>
>- $x_2 - x_1 <= w(v_1, v_2)$
>- $x_3 - x_2 <= w(v_2, v_3)$
>- ...
>- $x_{k-1} - x_{k-2} <= w(v_{k-2}, v_{k-1})$
>- $x_k - x_{k-1} <= w(v_{k-1}, v_k)$
>
>La solución también debe satisfacer a la suma de las $k$ inecuaciones. 
>
>Si sumamos la izquierda cada término $x_i$ aparece sumando y restando 1 vez (pues $v_k = v_1$), es igual a 0.
>Si sumamos la derecha tenemos $w(c)$. Como suponemos que $c$ es un ciclo negativo, nos queda que $0 <= w(c) < 0$ ABS!!
>
>Entonces si $D(S)$ tiene ciclo negativo, no tiene solución.

(b) Demostrar que si $D(S)$ no tiene ciclos de peso negativo, entonces $\{xi = d(v_0 , v_i ) | 1 \leq i \leq n\}$ es una solución de $D(S)$. Acá $d(v_0 , v_i)$ es la distancia desde $v_0$ a $v_i$ en $D(S)$.

>Consideremos cualquier arista $(v_i, v_j)$ en $E(S)$. Por la inecuación $d(v_0, v_j) <= d(v_0,v_i) + w(v_i,v_j)$ entonces $d(v_0, v_j) - d(v_0,v_i) <= w(v_i,v_j)$. Si igualamos $x_i = d(v_0,v_i)$ y $x_j = d(v_0, v_j)$ satisface la inecuación $x_j - x_i <= w(v_i,v_j)$ que corresponde a la arista $(v_i,v_j)$.

(c) A partir de los incisos anteriores, proponer un algoritmo que permita resolver cualquier SRD. En caso de no existir solución, el algoritmo debe mostrar un conjunto de inecuaciones contradictorias entre sí.

>Usamos algoritmo de busqueda de ciclos negativo desde v0 (Bellman Ford).
>
>Si BF devuelve True $\rightarrow$ el ciclo negativo es un conjunto de valores que hace contradictoria el sistema.
>
>Si BF devuelve False $\rightarrow$ el camino mínimo a todos los nodos es una solución del sistema.

## Algoritmo de Floyd-Warshall y recorrido mínimo en DAGs

### 13) Matriz FW
Decimos que una matriz cuadrada, simétrica y positiva $M \in N²$ es de Floyd-Warshall (FW) si existe un grafo $G$ tal que $M$ es el resultado de aplicar FW a $G$. Describir un algoritmo para decidir si una matriz $M$ es FW. En caso afirmativo, el algoritmo debe retornar un grafo $G$ con la mínima cantidad de aristas posibles tal que el resultado de FW sobre $G$ sea $M$ . En caso negativo, el algoritmo debe retornar alguna evidencia que pruebe que $M$ no es FW.

>Algoritmo:
>1. Chequear si $M$ es simétrico, tiene 0 en la diagonal y tiene la propiedad de triangulo de desigualdad (que para todo trío de índices $i, j, k$, la distancia directa de $i$ a $j$ no sea mayor que la suma de las distancias de ($i$ a $k$) y de ($k$ a $j$)). Si se encuentra $M[i][j] > M[i][k] + M[k][j]$ no puede ser resultado de aplicar Floyd-Warshall, ya que esta condición violaría la lógica de encontrar el camino más corto entre los nodos.
>2. Si $M$ satisface 1 construimos grafo, comenzar con un grafo sin aristas y luego, iterar sobre cada par $i$, $j$ y agregar la arista $i \rightarrow j$ con peso $M[i][j]$ solo si esa es la única manera de alcanzar la distancia mínima entre esos puntos, es decir, si no existe un $k$ tal que $M[i][k] + M[k][j] = M[i][j]$. Esto garantizará que solo se añadan las aristas esenciales para preservar las distancias mínimas.
>3. Si $M$ no satisface la simetría, tiene valores no nulos en la diagonal, o viola la propiedad del triángulo de desigualdad, debería ser capaz de identificar y devolver el conjunto de índices que violan estas condiciones como evidencia de que $M$ no puede ser resultado del algoritmo de Floyd-Warshall.

### 14) st-eficiente en matriz
Dado un digrafo $D$ con pesos $c$ : $E(D) \rightarrow R$ que no tiene ciclos de peso negativo, queremos encontrar la arista $v \rightarrow w$ que sea $st$-eficiente para la mayor cantidad de pares $s$ y $t$. Proponer un algoritmo eficiente y "simple de programar" para resolver este problema.

>Algoritmo:
>1. Corremos Floyd-Warshall para obtener el camino mínimo todos a todos en la estructura de dist $O(n³)$
>2. Iniciamos un diccionario de aristas para encontrar el mayor $st$-eficiente.
>3. Lo que necesitamos verificar es si la presencia de la arista $v \rightarrow w$ en el camino mínimo de $s$ a $t$ realmente hace que ese camino sea único o eficiente en términos de coste. Para esto, podríamos necesitamos asegurarnos de que no exista un camino alternativo de $s$ a $t$ que no pase por $v \rightarrow w$ y tenga el mismo costo mínimo. Esto implica verificar si la eliminación de la arista $v \rightarrow w$ y recalculando el camino mínimo entre $s$ y $t$ resulta en un camino de mayor costo o no. Para hacerlo eficiente y no estar sacando arista para recalcular el camino minimo nuevo, hacemos:
>
>       - Durante la ejecución de Floyd-Warshall, además de calcular las distancias mínimas, podría almacenar los caminos mínimos. Esto se puede hacer manteniendo una matriz de predecesores. Por cada par de nodos $(i, j)$, almacena el nodo predecesor de $j$ en el camino mínimo desde $i$ hasta $j$. Esto te permitirá reconstruir el camino mínimo sin tener que recalcular las distancias.
>       - Una vez se tiene los caminos mínimos, puedo verificar si la arista $v \rightarrow w$ es parte de estos caminos. Para cada par $(s, t)$, reconstruye el camino mínimo usando la matriz de predecesores y verifica si la arista $v \rightarrow w$ está en ese camino.
>       - Si $dist[s][v] + peso(v, w) + dist[w][t] = dist[s][t]$ entonces sabemos que cualquier camino mínimo de $s$ a $t$ debe pasar por $v \rightarrow w$. Si se elimina la arista $v \rightarrow w$, entonces, por definición, el camino mínimo de $s$ a $t$ tendría que ser diferente y por lo tanto, de mayor costo, dado que no existen ciclos de peso negativo en el grafo.
>       - Registro en un diccionario la frecuencia con que cada arista cumple la condición establecida anteriormente para todos los pares $(s, t)$.
>4. Devuelvo el max del diccionario.