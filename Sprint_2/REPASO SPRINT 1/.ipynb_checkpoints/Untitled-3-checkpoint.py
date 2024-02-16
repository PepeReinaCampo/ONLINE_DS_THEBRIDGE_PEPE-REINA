"""
si se puede, siendo incluso mejor:

"""
from pprint import pprint
#le cambiamos el nombre a la biblioteca, si seguimos trabajando con el mismo hará los cambios 2 veces, no se podrá ver si es lo mismo tan bien.
biblioteca_v2 = [("El mal de Corcira",4),("Un mundo feliz", 2),("Lolita", 5),\
              ("Crimen y castigo",2),("Python from for to pro", 0),("El señor de los anillos", 6),\
              ("Cien años de soledad", 5),("Harry Potter", 9),("Lectura Fácil", 4),("Seda", 2),\
              ("La chica de nieve", 6),("El día que se perdió la cordura", 3), ("Data Science", 0), ('Balada de pájaros cantores y serpientes', 10)]

libro_que_aumentará_su_cantidad= "El mal de Corcira"

for x, cada_libro in enumerate(biblioteca_v2):#va recorriendo cada libro de la biblioteca, le va llamando "cada_libro"
    
    libros_en_la_biblioteca, la_cantidad_de_libros_que_tengo_de_cada_titulo= cada_libro  #y cada libro esta compuesto de 2 cosas.
     
    if libros_en_la_biblioteca == libro_que_aumentará_su_cantidad:  #encuentra una coincidencia con el libro escogido (mira fuera de for, más arriba)
        biblioteca_v2[x] = (libros_en_la_biblioteca, la_cantidad_de_libros_que_tengo_de_cada_titulo + 1) #x es "cada saltito", osea cada tupla (su título y su cantidad) cuando ha encontrado coincidencia, justo entra y le suma 1.
        
        break
else:
    print("NO HAY UNIDADES DISPONIBLES")

pprint(biblioteca_v2)
