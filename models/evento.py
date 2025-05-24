from sqlalchemy import Column, Integer, String, ForeignKey
from models.base import Base

class Evento(Base):
    __tablename__ = "evento"

    id_evento = Column(Integer, primary_key=True)
    anfitrion = Column(String)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)

class Fiesta(Base):
    __tablename__ = "Fiesta"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    anfitrion = Column(String)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)

class Cumpleaños(Base):
    __tablename__ = "Cumpleaños"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    cumpleañero = Column(String)
    edad = Column(Integer)
    mesa_regalos = Column(String)

class Graduacion(Base):
    __tablename__ = "Graduación"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    escuela = Column(String)
    nivel_educativo = Column(String)
    generacion = Column(String)
    invitados_por_alumno = Column(Integer)

class XVAnos(Base):
    __tablename__ = "XV_años"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    cumpleañero = Column(String)
    padre = Column(String)
    madre = Column(String)
    padrino = Column(String)
    madrina = Column(String)
    mesa_regalos = Column(String)

class Boda(Base):
    __tablename__ = "Boda"
    
    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    novia = Column(String)
    novio = Column(String)
    padrino = Column(String)
    madrina = Column(String)
    mesa_regalos = Column(String)
    misa = Column(String)
    iglesia = Column(String)
    menores_permitidos = Column(String)
