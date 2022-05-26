from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Obtener todos los registros de la tabla directores de cine, que tengan el atributo nacionalidad mexicana\
      y ademas el valor del atributo experiencia en años sea diferente de none, \
          Finalmente se lo debe ordenar por el atributo de la tabla directores de cine apellido")
directores = session.query(Director_cine).filter(Director_cine.nacionalidad=="Mexicano", Director_cine.experiencia_anos!=None)\
    .order_by(Director_cine.apellido).all()
for s in directores:
    print("%s" % (s))
    print("--------")
    
print("--------------------------------")

print("Obtener todos los regustrosa de la tabla peliculas, que tengan el atributo tipo de pelicula fantasia, comedia \
    y ademas el valor del atributo nombre sea diferente de none, \
        Finalamente se debe ordenarpor el atributo año de lanzamiento")
fimls = session.query(Peliculas).filter(Peliculas.tipo_pelicula=="Fantasia, Comedia", Peliculas.nombre!=None)\
    .order_by(Peliculas.ano_lanzamiento).all()
for s in fimls:
    print("%s" % (s))
    print("--------")
    
    
    
    