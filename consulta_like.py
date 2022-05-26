from jinja2 import FileSystemBytecodeCache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Obtener todos los registros de la tabla directores de cine que tengan dentro del valor del atributo nacionalidad \
    la cadena 'Est', y su atributo apellido sea diferente de none; finalmente, se debe ordenar por el atributo \
        experiencia en años.")

print("----------------------------------------------------------------")

directores = session.query(Director_cine).filter(Director_cine.nacionalidad.like("%Est%"), Director_cine.apellido!=None) \
    .order_by(Director_cine.experiencia_anos).all()
for s in directores:
    print("%s" % (s))
    print("--------")
    

print("----------------------------------------------------------------")

print("Obtener todos los registros de la tabla peliculas que tengan dentro del valor del atributo nombre \
    la cadena 'La', y su atributo tipo de pelicula sea diferente de none; finalmente, se debe ordenar por el atributo \
        año de lanzamiento.")

films = session.query(Peliculas).filter(Peliculas.nombre.like("%La%"), Peliculas.tipo_pelicula!=None)\
    .order_by(Peliculas.ano_lanzamiento).all()
for s in films:
    print("%s" % (s))
    print("--------")
    
