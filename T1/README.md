¿Qué es un paradigma de programación?

Un paradigma de programación es un enfoque particular para abordar y resolver problemas mediante el uso de lenguajes de programación. Entre los paradigmas más comunes se encuentran la programación imperativa, funcional, orientada a objetos y lógica. Cada uno de estos paradigmas establece una manera específica en que los desarrolladores deben estructurar y organizar su código, influyendo tanto en el estilo como en las técnicas empleadas durante la programación.

¿En qué se basa la programación orientada a objetos?

La programación orientada a objetos (POO) se fundamenta en el uso de "objetos", instancias de clases que integran datos y comportamientos. Sus pilares esenciales son la abstracción, que se enfoca en representar solo los detalles relevantes; la herencia, que permite a una clase adquirir características de otra; y el polimorfismo, que facilita el tratamiento uniforme de objetos de distintos tipos. La creación de un programa en POO involucra ensamblar objetos y hacerlos interactuar entre sí.

¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación
big 𝑂?

La recursividad implica que una función se llame a sí misma hasta que se alcanza una condición base, mientras que la iteración usa bucles para repetir un bloque de código. En términos de notación Big O, los algoritmos recursivos pueden tener una complejidad mayor debido al costo asociado a las llamadas a funciones y el uso de la pila, mientras que los iterativos pueden ser más eficientes en algunos casos. Sin embargo, la elección entre uno u otro depende del problema específico que se esté resolviendo.

explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

O(1) representa un algoritmo de complejidad constante, lo que significa que su tiempo de ejecución no varía con el tamaño de la entrada; un ejemplo típico sería acceder a un elemento de un array. O(n), por otro lado, tiene complejidad lineal, lo que implica que el tiempo de ejecución crece proporcionalmente con el tamaño de la entrada. Un ejemplo sería recorrer una lista de tamaño n.

¿Cómo se calcula el orden en un programa que funciona por etapas

En un programa que se ejecuta en etapas, el orden o complejidad se calcula sumando o multiplicando las complejidades de cada etapa. Si las etapas se ejecutan de manera secuencial, las complejidades se suman. Si una etapa contiene otra (como un bucle dentro de otro bucle), las complejidades se multiplican. La complejidad global estará dominada por el término de mayor crecimiento.

¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

Se puede determinar usando ecuaciones de recurrencia. Estas ecuaciones describen cómo el tiempo de ejecución se divide entre las llamadas recursivas. Para resolver la ecuación y obtener la complejidad en notación Big O, se utilizan métodos como la sustitución o el análisis de árbol de recurrencia, lo que permite determinar la eficiencia del algoritmo en función del tamaño de la entrada.

-----------------------------------------------------------------------------------------------------------------------------

Para el código se desarrollaron tres códigos, el primero tiene de nombre "funciones" en el que se desarrollan únicamente las formas de calcular lo solicitado y se comprueba su correcto funcionamiento. En el segundo de nombre "T! clases sin decorador" vemos una clase que contiene métodos que calculan de diferentes formas los caminos posibles, utilizando las funciones del archivo anterior, además de un método que calcula el tiempo de ejecución de cada método. Finalmente en el archivo "T1 final" tenemos la misma clase, pero en vez de calcular el tiempo en un método de la clase, lo hace con el decorador solicitado. En la carpeta "Resultados" vemos los gráficos con los tiempos de ejecución de cada método.
