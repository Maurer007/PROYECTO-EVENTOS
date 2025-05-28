from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from models.base import Base
from sqlalchemy.orm import relationship

class Evento(Base):
    __tablename__ = "evento"

    id_evento = Column(Integer, primary_key=True)
    anfitrion_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    imagen_bytes = Column(LargeBinary)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)

    anfitrion = relationship("Usuario")

class Fiesta(Base):
    __tablename__ = "Fiesta"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    anfitrion_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    imagen_bytes = Column(LargeBinary)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)
    descripcion = Column(String)

    anfitrion = relationship("Usuario")

class Cumpleaños(Base):
    __tablename__ = "Cumpleaños"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    anfitrion_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    imagen_bytes = Column(LargeBinary)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)
    cumpleañero = Column(String)
    edad = Column(Integer)
    mesa_regalos = Column(String)

    anfitrion = relationship("Usuario")

class Graduacion(Base):
    __tablename__ = "Graduación"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    anfitrion_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    imagen_bytes = Column(LargeBinary)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)
    escuela = Column(String)
    nivel_educativo = Column(String)
    generacion = Column(String)
    invitados_por_alumno = Column(Integer)

    anfitrion = relationship("Usuario")

class XVAnos(Base):
    __tablename__ = "XV_años"

    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    anfitrion_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    imagen_bytes = Column(LargeBinary)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)
    cumpleañero_xv = Column(String)
    padre = Column(String)
    madre = Column(String)
    padrino = Column(String)
    madrina = Column(String)
    mesa_regalos_xv = Column(String)

    anfitrion = relationship("Usuario")

class Boda(Base):
    __tablename__ = "Boda"
    
    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"), primary_key=True)
    anfitrion_id = Column(Integer, ForeignKey("usuario.id_usuario"))
    imagen_bytes = Column(LargeBinary)
    tipo_evento = Column(String)
    fecha = Column(String)
    hora = Column(String)
    direccion = Column(String)
    num_invitados = Column(Integer)
    privacidad = Column(String)
    novia = Column(String)
    novio = Column(String)
    padrino_boda = Column(String)
    madrina_boda = Column(String)
    mesa_regalos_boda = Column(String)
    misa = Column(String)
    iglesia = Column(String)
    menores_permitidos = Column(String)

    anfitrion = relationship("Usuario")
