from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Obtener todos los registros de la tabla directo de cines ordenados segun el tipo de pelicula")

directores = session.query(Director_cine).order_by(Director_cine.nombre).all()
print("----------------")
for s in directores:
    print("%s" % (s))
    print("--------")
    
    
print("----------------------------")
print("Obtener todos los registros de la tabla peliculas ordenados segun el nombre")

films = session.query(Peliculas).order_by(Peliculas.nombre).all()
for s in films:
    print("%s" % (s))
    print("--------")
    
