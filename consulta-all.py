from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()


directores = session.query(Director_cine).all()
print("Presentacion de Directores")
print(directores)
for s in directores:
    print("%s" %(s))
    print("------------")
    
    



peliculas = session.query(Peliculas).all()
print("Presentacion de Peliculas")
for s in peliculas:
    print("%s" %(s))
    print("------------")
    

