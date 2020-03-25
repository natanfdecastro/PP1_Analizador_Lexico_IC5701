# PP1_Analizador_Lexico_IC5701
###  Proyecto Programado 1 para el curso Compiladores E Intérpretes
#### Instituto Tecnológico de Costa Rica
##### Centro Académico de Alajuela
##### Ingeniería en Computación
----------------------------------
Prof. Emmanuel Ramírez Segura
Semestre I – 2020
Valor: 12,50%
Fecha de Asignación: 17/03/2020
Fecha de Entrega: 14/04/2020
Proyecto #1:
Creación de un Analizador Léxico – Java Tropicalizado al Español
---------------------------------

* **Objetivo General**: Aplicar principios, modelos y técnicas para el diseño y la construcción de procesadores de lenguajes de programación de alto nivel, con énfasis en compiladores e intérpretes, para este proyecto, enfocándose en el diseño de un Analizador Léxico.

* **Objetivos Específicos**

1. Identificar los principales problemas relacionados con la implementación de lenguajes de
programación.
2. Comprender principios y métodos para implementar lenguajes de programación.
3. Comprender modelos abstractos de lenguajes y máquinas formales (gramáticas, expresiones
regulares y autómatas) y su aplicabilidad para la implementación de lenguajes de
programación.
4. Diseñar un Analizador Léxico que procese el lenguaje a crear.

* **Especificación del Proyecto**: El proyecto consistirá en implementar un analizador léxico sobre un subconjunto del lenguaje Java pero en idioma español, es decir, se intentará generar un lenguaje java tropicalizado.

* **Requerimientos de Diseño de Software**

1. El lenguaje fuente sobre el que construirá el analizador puede ser Java o Python, según se prefiera, sin embargo, es importante tener en cuenta que una vez iniciado el desarrollo en alguno de estos lenguajes, las siguientes fases deberán implementarse en el lenguaje seleccionado.
2. Independiente del lenguaje a utilizar, sea este Java o Python, deben hacer uso de la Orientación a Objetos y aprovechar las características de este paradigma. Además, deben saber que este primer proyecto, será posteriormente un módulo (denominado
“F   AL x c ”) a utilizar en fases posteriores.
3. Posterior a la fase del analizador léxico, seguirá la fase del análisis sintáctico por lo es de extrema importancia que este primer módulo quede funcional para no atrasar las fases subsecuentes.
4. La gramática a utilizar se muestra en el anexo 1, como podrán observar, la misma se encuentra en inglés, por lo que ustedes en su grupo deberán traducirla y reescribirla al lenguaje español para que inicien con la implementación del analizador léxico.
5. La aplicación a entregar deberá utilizarse desde la línea de comandos.
6. Se deberá entregar al finalizar el analizador léxico el siguiente software:
a. El código fuente desarrollado, el mismo debe encontrarse con comentarios
generales indicando lo que hacen los procedimientos, funciones que se utilizan.
b. Un archivo README.txt que indique cómo ejecutar su programa en la línea de
comandos.
c. Dos archivos de prueba: prueba1.txt y prueba2.txt que permitan ser utilizados para
corroborar el funcionamiento de su analizador léxico.
d. Debe entregar la gramática al idioma español en un archivo formato pdf.
7. Sobre la manera de ejecutar el programa del analizador léxico:
[NOMBRE DEL PROGRAMA] [ARCHIVO DE ENTRADA] [ARCHIVO SALIDA]
Descripción:
[NOMBRE DEL PROGRAMA]: Se recomienda utilizar el nombre analizadorLexico.
[ARCHIVO DE ENTRADA]: Es el archivo a ser analizado léxicamente. Por ejemplo: prueba1.txt.
[ARCHIVO DE SALIDA]: Acá aparecerán el [ARCHIVO DE ENTRADA] transformado según los
lexemas clasificados por tokens.
Por ejemplo, el [ARCHIVO DE SALIDA CONTENDRÁ]:< “tipo de token”, “texto del token”> … < “tipo de token”, “texto del token”> ….
8. Puesto que el analizador léxico puede reportar errores, en esta parte sólo será necesario indicar el número de línea que contiene el error, por ejemplo: “La línea 7 contiene un error, el lexema identificado con error es: XXXXXXX”.
9. No se requiere para esta entregar implementar técnicas de corrección de errores, es decir, ante un error, el programa desplegará lo contenido en el punto 8 y finalizará la ejecución del programa.
10. No se podrá hacer uso de analizadores léxicos automáticos o bibliotecas de análisis léxico, todo se deberá programar. Puede hacer uso de bibliotecas para el manejo de expresiones regulares con libertad.
11. Se recomienda poner énfasis para la implementación de este proyecto los conceptos de: buffers para la lectura de archivos, tabla de identificadores.

* **Requerimientos del Reporte**

Se deberá entregar de manera impresa un documento con las siguientes secciones, cada una en una hoja independiente.

PORTADA (incluir entre lo usual el número de grupo).

INDICE (con la numeración de páginas correctamente).

GRAMATICA (la gramática en español).

RECONOCIMIENTO DE TOKENS (presentar una tabla de dos columnas, indicando los tokens que se identificar en la primer columna, y las expresiones regular que utilizó para asociarlo).

LOGROS, ERRORES O PROBLEMAS (describir brevemente que se logró colocar imágenes de
ejemplo de análisis léxicos y en caso de existir describir qué problemas o errores persisten).

* **Consideraciones a tomar en cuenta en general**

1. Los diversos grupos pueden aportar ideas en la solución de sus proyectos entre sí, pero se prohíbe compartir códigos o implementaciones entre los grupos.
2. La solución de los proyectos debe ser algo inédito, no se deberán copiar de libros u otras fuentes de información secciones de código.
3. El profesor bajo ninguna circunstancia atenderá dudas originadas a problemas de diseño o implementación de los proyectos, únicamente atenderá dudas en cuanto al entendimiento del proyecto si hubieren.
4. Se insta a utilizar los libros del curso para ahondar en aspectos de diseño e implementación.

* **Aspectos Evaluativos**
Aspecto a evaluar Porcentaje
Requerimientos del Diseño del Software 70%
Revisión Parcial 10%
Requerimientos del Reporte 20%
-------- 100%
Sobre cada Aspecto se evaluará: Porcentaje
Excelente (cumple con lo solicitado) [90% al 100%]
Muy Bueno [80% a 89%]
Bueno [70% - 79%]
Regular [50% - 69%]
Malo [1% al 49%]
No hay entrega 0%

* **Aspectos de entrega**

1. La fecha de entrega de este proyecto es antes del Martes 14 de Abril a las 6:00pm (GMT-6).
No se aceptarán proyectos posteriores a esa fecha-hora.
2. Durante la segunda lección del Martes 31 de Marzo, el profesor habilitará un espacio para que
los estudiantes le demuestren lo que llevan implementado a la fecha (esto constituye la revisión parcial), se espera observar:
    a. Código ejecutable que realice ciertos análisis léxicos parciales a archivos de entrada.
    b. La gramática propuesta en el anexo 1, pero tropicalizada por ustedes todo al español.
3. El medio de entrega digital a la dirección de correo: entregasITCR@gmail.com debe de
adjuntar un archivo .ZIP con:
a) Código Fuente.
b) Archivo README.txt
c) Archivos de Pruebas 1 y 2.
4. El reporte impreso se entregará en las clases del Martes 14 de Abril, el mismo debe contener lo solicitado en la sección “Requerimientos del Reporte”.
Para está entrega el Asunto deberá indicar: Proyecto N1. Análisis Léxico Grupo X
El Adjunto deberá indicar: ProyectoN1_AnalisisLexico_GrupoX.zipANEXO 1. Gramática en formato llamado Extended Backus-Naur Form (EBNF)*
Esta gramática es tomada del libro Modern Compiler Implementation in Java, en las páginas **484 - 486.** 
Donde: 
**_o Identifier (identificadores):_** Los identificadores son secuencias de letras, dígitos, guiones bajos („_‟), iniciando siempre con una letra.
Hay sensibilidad de mayúsculas y minúsculas, es decir, un identificador con el nombre: hola123, será tratado diferente si se escribe como Hola123 u HoLa123, entre otras combinaciones.
**_o Integer literals (enteros literales):_** Estos corresponden a una secuencia de dígitos del 0 al 9 (uno o varios), denotan el correspondiente valor entero. 
**_o Binary Operators (operadores binarios):_** Los mismos pueden ser: &&, <, +, -,
**_o Comments (comentarios):_** El comentario en este caso sería como sigue: /* Aquí el Comentario */
Observese los tokens de inicio y de fin.

* **Links Importantes**
Si bien los analizadores léxicos automáticos no los pueden utilizar como parte de esta entrega, sí
pueden utilizarlos para comprender su funcionamiento, uno de ellos es:
JFlex
https://www.jflex.de/
Otros enlaces importantes: Especificación del Lenguaje JAVA Completa:
https://docs.oracle.com/javase/specs/jls/se13/html/jls-3.html#jls-3.8
