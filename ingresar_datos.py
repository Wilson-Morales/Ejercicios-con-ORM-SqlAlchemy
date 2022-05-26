from sqlite3 import dbapi2
from git import Commit
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from conexion import engine
from generar_tablas import Director_cine, Peliculas


Session = sessionmaker(bind=engine)
session = Session()

director_cine1 = Director_cine(nombre="Quentin", apellido="Trantino", nacionalidad="Estadounidense", experiencia_anos="35",)
director_cine2 = Director_cine(nombre="Guillermo del Toro", apellido="Gómez", nacionalidad="Mexicano", experiencia_anos="37",)
director_cine3 = Director_cine(nombre="Samuel", apellido="Rami", nacionalidad="Estadounidense", experiencia_anos="45",)
director_cine4 = Director_cine(nombre="Steve", apellido="Buscemi", nacionalidad="Estadounidense", experiencia_anos="40",)
director_cine5 = Director_cine(nombre="Alfonso", apellido="Cuarón", nacionalidad="Mexicano", experiencia_anos="39",)


pelicula1 = Peliculas(nombre="Bastardos sin gloria", tipo_pelicula="Bélico, Acción", ano_lanzamiento="2009", costo_pelicula="70 000 000", director_cine=director_cine1)
pelicula2 = Peliculas(nombre="DJango sin cadenas", tipo_pelicula="Drama Oeste", ano_lanzamiento="2012", costo_pelicula="1000 000 000", director_cine=director_cine1)

pelicula3 = Peliculas(nombre="Titanes del Pacifico", tipo_pelicula="Ciencia ficción, Acción", ano_lanzamiento="2013", costo_pelicula="190 000 000", director_cine=director_cine2)
pelicula4 = Peliculas(nombre="HellBoy", tipo_pelicula="Fantasia oscura, Ciencia ficción", ano_lanzamiento="2004", costo_pelicula="66 000 000", director_cine=director_cine2)

pelicula5 = Peliculas(nombre="Spider-Man", tipo_pelicula="Superhéroes, Acción", ano_lanzamiento="2002", costo_pelicula="139 000 000", director_cine=director_cine3)
pelicula6 = Peliculas(nombre="Oz: El poderoso", tipo_pelicula="Fanstasia", ano_lanzamiento="2013", costo_pelicula="215 000 000", director_cine=director_cine3)

pelicula7 = Peliculas(nombre="Son como niños 2", tipo_pelicula="Comedia, Buddy film", ano_lanzamiento="2013", costo_pelicula="80 000 000", director_cine=director_cine4)
pelicula8 = Peliculas(nombre="La herencia de Mr. Deeds", tipo_pelicula="Romantica, Comedia", ano_lanzamiento="2022", costo_pelicula="50 000 000", director_cine=director_cine4)

pelicula9 = Peliculas(nombre="Harry Potter y el pricioner de Azkaban", tipo_pelicula="Fantasia, Ficción", ano_lanzamiento="2004", costo_pelicula="130 000 000", director_cine=director_cine5)
pelicula10 = Peliculas(nombre="Las Brujas", tipo_pelicula="Fantasia, Comedia", ano_lanzamiento="2020", costo_pelicula="----", director_cine=director_cine5)


session.add(director_cine1)
session.add(director_cine2)
session.add(director_cine3)
session.add(director_cine4)
session.add(director_cine5)

session.add(pelicula1)
session.add(pelicula2)
session.add(pelicula3)
session.add(pelicula4)
session.add(pelicula5)
session.add(pelicula6)
session.add(pelicula7)
session.add(pelicula8)
session.add(pelicula9)
session.add(pelicula10)

session.commit()

