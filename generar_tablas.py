from sqlite3 import dbapi2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

from conexion import engine



audiovisual = declarative_base()

class Director_cine(audiovisual):
    __tablename__ = 'director_cine'
    id = Column(Integer, primary_key=True)
    nombre= Column(String)
    apellido= Column(String)
    nacionalidad= Column(String)
    experiencia_anos= Column(Integer)
    
    def __repr__(self):
        return "Director_cine: nombre=%s, apellido=%s,nacionalidad=%s,experiencia_anos=%s " % (
            self.nombre,
            self.apellido,
            self.nacionalidad,
            self.experiencia_anos)

class Peliculas(audiovisual):
    __tablename__ = 'peliculas'
    id = Column(Integer, primary_key=True)
    nombre= Column(String)
    tipo_pelicula = Column(String)
    ano_lanzamiento = Column(Integer)
    costo_pelicula = Column(Integer)
    
    director_cine_id = Column(Integer, ForeignKey('director_cine.id'))
    director_cine = relationship ("Director_cine", back_populates="peliculas")
    
    def __repr__(self):
        return "Peliculas: nombre=%s, tipo_pelicula=%s, ano_lanzamiento=%s, costo_pelicula=%s" % (
            self.nombre,
            self.tipo_pelicula,
            self.ano_lanzamiento,
            self.costo_pelicula)
        
Director_cine.peliculas = relationship("Peliculas",back_populates="director_cine")

audiovisual.metadata.create_all(engine)



    
    