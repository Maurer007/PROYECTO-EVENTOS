#Orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.usuario import Usuario
from models.evento import Evento, Fiesta, Cumpleaños, Graduacion, XVAnos, Boda
from models.asistencia import Asiste

engine = create_engine("sqlite:///db/app.db", echo=False)
Session = sessionmaker(bind=engine)

def crear_base_de_datos():
    Base.metadata.create_all(engine)
