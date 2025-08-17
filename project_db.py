import os
from sqlalchemy import create_engine, String, Integer, ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column


DATABASE_URL = os.getenv("DATABASE_URL")


DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+pg8000://")


engine = create_engine(DATABASE_URL, echo=True)


Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass



class Conversion(Base):
    __tablename__ = "conversions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    input_value: Mapped[str] = mapped_column(String, nullable=False)
    output_value: Mapped[str] = mapped_column(String, nullable=False)



def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)
