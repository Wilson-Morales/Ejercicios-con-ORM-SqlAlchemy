from jinja2 import FileSystemBytecodeCache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Obtener todos los registros de la tabla directores de cine que tengan el valor de expereincia en años \
    igual a '35' o '45', finalmente, se debe ordenar por el atributo apellido")

print("------------------------------------------------------------------------------------------------")

directores = session.query(Director_cine).filter(or_(Director_cine.experiencia_anos=="35", \
    Director_cine.experiencia_anos=="45")).order_by(or_(Director_cine.apellido))
for s in directores:
    print("%s" % (s))
    print("--------")
    
    
print("------------------------------------------------------------------------------------------------")

print("Obtener todos los registro de la tabla peliculas que tengan el valor de tipo de pelicula \
    igual a 'Superheroes', o que sea igual a 'Romantica', finalmente, se debe ordenar por el atributo \
        año de lanzamiento.")

print("------------------------------------------------------------------------------------------------")

films = session.query(Peliculas).filter(or_(Peliculas.tipo_pelicula=="Superhéroes, Acción", Peliculas.tipo_pelicula=="Romantica, Comedia")) \
    .order_by(Peliculas.ano_lanzamiento).all() 
    
for s in films:
    print("%s" % (s))
    print("--------")
    
    
