from sqlalchemy import Column, Integer, ForeignKey
from models.base import Base


class Asiste(Base):
    __tablename__ = "asiste"
    
    id_asistencia = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario", ondelete="CASCADE"))
    id_evento = Column(Integer, ForeignKey("evento.id_evento", ondelete="CASCADE"))
