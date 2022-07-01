Proyecto Discreto - Grupo UwU
###################################  RESUMEN  ###################################

El código interpreta una base de datos introducida en formato csv (no header) como un objeto que posee en sus atributos las herramientas necesarias para estandarizarlo en una matriz binaria.

Esta matriz es luego comparada con un juego de expresiones de logica proposicional a traves de las cuales se determina en que interación la reaccion es positiva (1) o negativa (0).

En el caso del trabajo, el input es el desempeño de las 13 variables económicas elegidas de uno de los 4 paises (US, JAPON, KOREA y BRASIL). El objeto estandariza este dataframe elaborando una matriz binaria. Esta matriz binaria luego es puesta a prueba con el juego de expresiones lógicas de cada país. El objeto devuelve las iteraciones positivas, para las cuales se debe tomar la accion de comprar (irse de largo). 

###################################  DETALLE  ###################################

QM_completo.py y tablas_de_verdad.py son ambos documentos con codigos que usamos durante el desarrollo del trabajo. QM_completo.py fue recogido de un repositorio de GitHub (https://github.com/int-main/Quine-McCluskey) y adaptado acorde a los requerimientos de nuestro proyecto. tablas_de_verdad.py fue elaborado por un miembro del grupo UwU.

Para el funcionamiento de combinaciones.py se usaron coeficientes obtenidos gracias a una regresion (realizada por el grupo UwU) elaborada a la informacion del desempeño económico de los países que son sujeto de estudio. Estos son USA, BRASIL, KOREA y JAPON.

El archivo combinaciones.py usa estos coeficientes en una tabla de verdad de 13 variables para hallar cuales de las combinaciones tienen un indice mayor o igual a 0.5. Estos valores que cumplen la condición se encuentran en el archivo valores.py de acuerdo a cada país. 

Una vez obtenidos estas combinaciones, son procesados en QM_completo.py el cual incluye el algoritmo Quine-McCluskey para reducir las expresiones a sus implicantes primos esenciales. Estos valores están almacenados en forma de listas en el archivo Implicantes_esenciales.py.

Estos implicantes primos esenciales son rescatados por maincode.py, el cual contiene una clase donde usa de esta informacion, junto a los datos de cada país para hallar cuales son las iteraciones donde se debe comprar.

Los datos de cada pais se encuentran en csvs dentro de la carpeta /df, junto con los archivos binarios de los objetos de cada país. Si se desease evaluar las iteraciones de otro archivo, solo haria falta reemplazar el archivo del país dentro de /df con el que deseases evaluar. 

################################  INSTRUCCIONES  ################################

-------------------------------PARTE ESTÁTICA------------------------------------
1. Ejecutar el archivo combinaciones.py. Los valores obtenidos (minterminos) de esta ejecución se colocaron en el archivo valores.py.
2. Para ejecutar el archivo QM_completo.py, primero se tendrá que dirigir a la linea 98 y descomentar el país del que quiera obtener los valores. Asimismo, deberá hacer el cambio correspondiente en la línea 107. Los resultados pueden tardar en aparecer entre 10 a 35 minutos dependiendo del país. Los valores obtenidos (implicantes primos esenciales) se colocaron en el archivo Implicantes_esenciales.py.
3. Los valores de cada país en el archivo Implicantes_esenciales.py serán utilizados posteriormente en el maincode.py

-------------------------------PARTE DINÁMICA------------------------------------
1. Dirigirse a la carpeta \###CSV ACA###
2. Modificar el CSV del país del que se introducirá la información. Estas son 13 variables con el formato (var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13)
3. Ejecutar el maincode y escoger la opcion del país que se desea consultar

#################################################################################
