import ssl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Obtenertodos los registros de la tabla directores de cine que tengan el atributo nacionalidad \
    con un valor Estadounidense, ordenados segun su nombre")

directores = session.query(Director_cine).filter(Director_cine.nacionalidad=="Estadounidense").order_by(Director_cine.nombre).all()
for s in directores:
    print("%s" % (s))
    print("--------")
    

print("------------------------------------------------------------------------")

print("Obtener los registros de la tabla Peliculas que tengan el atributo costo de la pelicula \
    con un valor de 80 000 000, ordenados segun el año de su lanzamiento")
films = session.query(Peliculas).filter(Peliculas.costo_pelicula == "80 000 000").order_by(Peliculas.ano_lanzamiento).all()
for s in films:
    print("%s" % (s))
    print("--------")
    