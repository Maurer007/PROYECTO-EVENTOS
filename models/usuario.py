#Usuario
from sqlalchemy import Column, Integer, String
from models.base import Base

#from sqlalchemy.orm import declarative_base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido_paterno = Column(String, nullable=False)
    apellido_materno = Column(String)
    género = Column(String)
    ciudad = Column(String)
    estado = Column(String)
    fecha_nacimiento = Column(String)
    nom_usuario = Column(String)
    contraseña = Column(String, nullable=False)
    teléfono = Column(String)
    correo = Column(String, nullable=False, unique=True)
