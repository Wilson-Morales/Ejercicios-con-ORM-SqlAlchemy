from jinja2 import FileSystemBytecodeCache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print ("Obtener toos los registro de la tabla directores de peliculas, que tengan dentro del valor del atributo \
    nacionalidad la cadena 'Mex', y el atributo apellido sea diferente de none; finalmente, se debe ordenar por \
        el atributo experiencia en años")
print ("-----------------------------------------")

directores = session.query(Director_cine).filter(and_(Director_cine.nacionalidad.like("%Mex%")), \
    Director_cine.apellido!=None).order_by(Director_cine.experiencia_anos).all()
for s in directores:
    print("%s" % (s,))
    print("---------")
    
    
print ("-----------------------------------------")

print("Obtener todos los registro de la tabla peliculas, que tengan dentro del valor del atributo año de lanzamiento \
    la cadena '20', y el atributo director cine id sea diferente de none; finalmente, se debe ordenar por \
        el atributo nombre")

films = session.query(Peliculas).filter(and_(Peliculas.ano_lanzamiento.like("%20%")), Peliculas.director_cine_id!=None) \
    .order_by(Peliculas.nombre).all()
    
for s in films:
    print("%s" % (s))
    print("--------")
    
