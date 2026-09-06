Respuestas a preguntas de razonamiento

-----Etapa 1: Cargar y diagnosticar-----

P. ¿Por qué diagnosticar el dataset completo (forma, nulos) antes de limpiar nada, en vez de empezar a  limpiar directamente desde la 
primera columna que veas?
R. Diagnosticar el dataset completo antes de empezar a limpiarlo permite entender su estructura y detectar los principales problemas de 
calidad de los datos. Por ejemplo, revisar su tamaño y los valores nulos ayuda a identificar qué columnas realmente necesitan tratamiento.
Si comenzara a limpiar directamente la primera columna, podría tomar decisiones sin conocer el contexto general del dataset, realizar 
transformaciones innecesarias o incluso afectar información importante. Por eso, primero haría un diagnóstico general y, a partir de los 
problemas encontrados, definiría una estrategia de limpieza adecuada.

-----Etapa 2: Limpiar-----

P. ¿Qué pasaría si rellenaras Budget con 0 en vez de eliminar esas filas? ¿Cómo afectaría eso a la columna Ganancia que vas a crear en la
próxima etapa?
R. Si rellenara los valores nulos de Budget con 0, estaría asumiendo que esas películas tuvieron un presupuesto de cero dólares, cuando en 
realidad lo que ocurre es que no conocemos su presupuesto. Esto afectaría directamente a la columna Ganancia (WorldGross - Budget), 
porque para esas películas la ganancia sería igual a WorldGross. Por ejemplo, si una película recaudó 100 millones y su presupuesto es 
desconocido, al sustituirlo por 0 obtendríamos una ganancia falsa de 100 millones. Por eso, en este caso es más adecuado eliminar las filas 
con valores nulos en Budget, ya que necesitamos valores reales para calcular una ganancia confiable.

-----Etapa 3: Crear columnas nuevas-----

P. Ganancia se calcula restando (WorldGross - Budget). ¿Qué representaría, en cambio, una columna que dividiera WorldGross entre
Budget? ¿En qué caso preferirías esa versión en vez de la resta?
R. Una columna calculada como WorldGross / Budget representaría el retorno de la película en relación con su presupuesto, es decir, cuántas 
veces logró recaudar mundialmente lo que costó producirla. Por ejemplo, si una película tuvo un presupuesto de 50 millones y recaudó 
200 millones:

Ganancia: 200 - 50 = 150 millones.
WorldGross / Budget: 200 / 50 = 4, lo que significa que recaudó 4 veces su presupuesto.

Preferiría utilizar la división cuando quisiera comparar la eficiencia o rentabilidad relativa de películas con presupuestos muy diferentes. 
Una película pequeña podría generar menos dinero en términos absolutos, pero tener un retorno proporcional mucho mayor que una superproducción.

-----Etapa 4: Tipos de datos y ordenar-----

P. ¿Qué habría pasado si hubieras intentado ordenar por Ganancia antes de limpiar los nulos de WorldGross y Budget en la Etapa 2? ¿Por qué
el orden en que se hacen las etapas importa aquí?
R. Si hubiera calculado y ordenado por Ganancia antes de limpiar los valores nulos de WorldGross y Budget, las películas que tuvieran alguno 
de esos datos faltantes también tendrían una Ganancia nula (NaN), porque no es posible realizar correctamente la resta si falta uno de los 
valores. Esto podría dificultar el análisis y producir un ranking incompleto o poco confiable. Por eso, el orden de las etapas importa: 
primero se limpian y validan los datos, luego se crean variables como Ganancia y finalmente se realizan análisis como ordenar las películas 
de mayor a menor ganancia.

-----Etapa 5: Agrupar y analizar-----

P. De los géneros con más películas en el dataset (Comedia, Acción, Drama), ¿cuál tiene el promedio de calificación de crítica más alto? ¿Te
sorprende, o era lo que esperabas?
R. De los tres géneros con más películas, Drama tiene el promedio de calificación más alto en Rotten Tomatoes, superando a Acción y Comedia.
El resultado no me sorprende demasiado, ya que las películas de drama suelen dar mayor importancia a elementos como la narrativa, las 
actuaciones y el desarrollo de personajes, aspectos que pueden ser bien valorados por la crítica. Sin embargo, también hay que considerar 
que Drama tiene menos películas que Acción y Comedia. Al tener una muestra menor, su promedio puede ser más sensible a calificaciones altas o 
bajas. Por lo tanto, el tamaño de cada grupo también debe tenerse en cuenta al interpretar esta diferencia.

-----Etapa 6: Guardar el resultado-----

P. ¿Por qué guardar el resultado en un archivo nuevo (hollywood_limpio.csv), en vez de sobrescribir el archivo original hollywood.csv que
descargaste?
R. Guardar el resultado en un archivo nuevo como hollywood_limpio.csv permite conservar el dataset 
original sin modificaciones. Esto es importante porque el archivo original funciona como una fuente 
de respaldo a la que podemos regresar si cometemos algún error durante la limpieza o necesitamos 
aplicar un procedimiento diferente. Además, mantener separados los datos originales y los procesados 
facilita la trazabilidad del pipeline, ya que podemos comparar ambos archivos y saber qué 
transformaciones se realizaron. Si sobrescribiéramos hollywood.csv, perderíamos los datos originales 
y sería más difícil recuperar información eliminada o modificada accidentalmente.