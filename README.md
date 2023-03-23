# WBSLA_parsero
Programa que permite transformar archivos fastas de proteínas en dataframes para una anotación de datos más fluida

**NOTA:Este programa esta pensado para el entorno de Windows.**

## 1. Instalación

El flujo de trabajo hace uso dos scripts de python:

1. liniero.py: script que pasa las secuencias de fastas de un bloque a una sola linea
2. parsero_.py: script que lee y convierte el archivo linearizado en un data frame con las categorías *accesion*, *specie* y *fasta*

Para hacer uso de estos scripts es necesario contar con las librerías **pandas**, **re** y **csv**, ya que el script *parsero_.py* las invoca a través de **import** al ejecutarse. 

Tomando en cuenta esto se recomienda lo siguiente para su instalación:
1. Crear una carpeta nueva con el nombre *parsero*
2. Descargar los scripts y guardarlos en la carpeta del paso 1.
3. Mover el archivo fasta a la misma carpeta donde estan los scripts
4. ¡El ejecutable esta listo para usarse!

## 2. Corrida

Para realizar la corrida del programa debemos ejecutar los siguientes pasos:
1. Abrimos el **Terminal**  y ubicamos la ruta donde se encuentra la carpeta *parsero*
```
PS C:\Users\IO> cd Desktop\parsero
```
2. Ejecutamos primero el archivo *liniero.py* y nos preguntará el archivo que queremos modificar:
```
PS C:\Users\IO\Desktop\parsero python liniero.py
Hello, input fasta file you want to linearize: TEST_2_Panga.txt
Which will be te name of your output file?: line_TEST_2_panga
PS C:\Users\IO\Desktop\parsero
```
3. Luego ponemos el nombre que queremos para el archivo de salida y con ello ya tendremos nuestro archivo linearizado.
4. Despues ejecutamos a *parsero_.py* donde nos pregunta el archivo que queremos transformar (usamos el fasta linearizado)
```
PS C:\Users\IO\Desktop\parsero python parsero_.py
Hello, input linearized fasta file you want to modify:: line_TEST_2_Panga.txt
preparing file as dataframe
            Accesion                        Species                                     Fasta sequence
0    [>KAB5583777.1]  [Pangasianodon hypophthalmus]  [MLRLQCVVLALVLYLKGSLSQLDVCGRAPFNTRIVGGQSASDGVW...
1  [>XP_026801323.2]  [Pangasianodon hypophthalmus]  [MLRLQCVVLALVLYLKGSLSQLDVCGRAPFNTRIVGGQSASDGVW...
2    [>MCI4375000.1]          [Pangasianodon gigas]  [MMRLQCVVLALVLYLKGSLSQLDVCGRAPFNTRIVGGQSASDGVW...
3  [>XP_026801315.3]  [Pangasianodon hypophthalmus]  [MLRFQCVAVALALYLKGSLSQLNVCGRAPFNTRIVGGQSASDGVW...
4  [>XP_053492400.1]           [Ictalurus furcatus]  [MLRYQCVVLALVLYLNGSLSQLNECGSAPFNTRIVGGQNASDGVW...
5  [>XP_017336018.1]          [Ictalurus punctatus]  [MLRYQCVVLALVLYLNGSLSQLNECGSAPFNTRIVGGQNASDGVW...
6  [>XP_053492401.1]           [Ictalurus furcatus]  [MLRYQCVVVALVLYLKGSLSQLNECGSAPFNTRIVGGQNASDGVW...
7    [>KAF4078738.1]               [Ameiurus melas]  [MLRYQCVVVALVLYLKGSLSQLNECGTAPFNTRIVGGQNASDGVW...
8  [>XP_017336017.1]          [Ictalurus punctatus]  [MLRYQCVVVALVLYLKGSLSQLSECGSAPFNTRIVGGQNASDGVW...
9    [>KAG7326120.1]        [Hemibagrus wyckioides]  [MLRLQCVFVALVLYLKGSLSQLNECGSAPFNTRIVGGQNASAGAW...
Great! we have our fasta dataframe!
what name would you like for your exit file?: df_TEST_2_panga
thank you for using parsero!
PS C:\Users\IO\Desktop\parsero
```
5. Luego genera e imprime el data frame y nos pregunta el nombre que queremos para el archivo de salida.
6. Finalmente abrimos la carpeta donde estan los ejecutables y encontraremos el archivo csv de nuestros fastas.

## 2. Usos
Con este script podremos luego habilitar nuestros datos para hacer uso de la librería pandas y poder ya sea aumentar columnas (agregar nombres comunes o metadatos de secuencias), filtrat por especie, o generar un nuevo archivo de texto con headers que sean más descriptivos para las investigaciónes tanto de alineamientos o de filogenias.


Si tienes alguna sugerencia no dudes en contactarme
isabela_avila@msn.com

Gracias por usar parsero!
