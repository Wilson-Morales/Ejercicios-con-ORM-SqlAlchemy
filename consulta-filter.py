from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from generar_tablas import Director_cine, Peliculas

from conexion import engine


Session = sessionmaker(bind=engine)
session = Session()

print("Mostrar en pantalla todos los directores con mas de 45 años de experiencia...")

directores = session.query(Director_cine).filter(Director_cine.experiencia_anos=="45").all()
print("----------------------------------------------------------------")
for s in directores:
    print("%s"%(s))
    print("-------")
    
print("----------------------------------------------------------------")

print("mostrar en pantalla todos las peliculas que hayan sido lanzadas en 2004")

fimls = session.query(Peliculas).filter(Peliculas.ano_lanzamiento=="2004")
print("----------------------------------------------------------------")
for s in fimls:
    print("%s"%(s))
    print("-------")

