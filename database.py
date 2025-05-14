from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de SQLAlchemy
Base = declarative_base()
DATABASE_URL = "sqlite:///eventos.db"

# Modelo de la tabla de eventos
class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True)
    categoria = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    color = Column(String, nullable=False)

# Clase para manejar la base de datos
class DatabaseManager:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def obtener_eventos(self):
        session = self.Session()
        eventos = session.query(Evento).all()
        session.close()
        return eventos

    def insertar_eventos_ejemplo(self):
        session = self.Session()
        if session.query(Evento).count() == 0:
            eventos_ejemplo = [
                Evento(categoria="Cumpleaños", nombre="Fiesta de Juan", color="pink"),
                Evento(categoria="Graduaciones", nombre="Graduación de Ana", color="blue"),
                Evento(categoria="XV años", nombre="XV de María", color="purple"),
            ]
            session.add_all(eventos_ejemplo)
            session.commit()
        session.close()