from jinja2 import FileSystemBytecodeCache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Obtener todos los registros de directores de cine, que tengan almenos una pelicula asociada. ")

print("----------------------------------------------------------------")

directores = session.query(Director_cine, Peliculas).join(Peliculas).filter(Peliculas.director_cine_id).all()
for s in directores:
   print(s [0])
   print(s [1])

   
   
  
 
