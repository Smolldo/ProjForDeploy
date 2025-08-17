import os
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

# Отримуємо DATABASE_URL з Render (або використовуємо SQLite локально)
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    # Для pg8000 потрібен спеціальний драйвер
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+pg8000://")
else:
    # Якщо немає DATABASE_URL → fallback на SQLite
    DATABASE_URL = "sqlite:///local.db"

# Створюємо engine
engine = create_engine(DATABASE_URL, echo=True)

# Сесія
Session = sessionmaker(bind=engine)

# Базовий клас
class Base(DeclarativeBase):
    pass


# Приклад моделі
class Conversion(Base):
    __tablename__ = "conversions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    input_value: Mapped[str] = mapped_column(String, nullable=False)
    output_value: Mapped[str] = mapped_column(String, nullable=False)


# Функції для створення/видалення таблиць
def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)
