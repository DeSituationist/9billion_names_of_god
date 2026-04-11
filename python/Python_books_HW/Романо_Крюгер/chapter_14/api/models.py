import hashlib
import os
import secrets
from enum import StrEnum, auto

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Unicode,
)

from sqlalchemy.orm import mapped_column, relationship, Mapped

from .database import Base

UNICODE_LEN = 128 
SALT_LEN = 64 # кол-во байт соли добавляем перед хэшированием пароля

# Перечисления
class Classes(StrEnum): # Члены перечисления можно сравнивать со строками напрямую
    first = auto()  # Автоматически задает значения элементов
    second = auto()  # Здесь это будет строка с именем элемента

class Roles(StrEnum):
    admin = auto()
    passenger = auto()

# Станция
class Station(Base):
    __tablename__ = 'station'
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(Unicode(UNICODE_LEN), unique=True)
    country: Mapped[str] = mapped_column(Unicode(UNICODE_LEN))
    city: Mapped[str] = mapped_column(Unicode(UNICODE_LEN))
    departures: Mapped[list['Train']] = relationship(
        foreign_keys='[Train.station_from_id]',
        back_populates='station_from'
    )
    arrivals: Mapped[list['Train']] = relationship(
        foreign_keys='[Train.station_to_id]',
        back_populates='station_to',
    )

    def __repr__(self):
        return f'<{self.code}: id={self.id} city={self.city}>'
    
    __str__ = __repr__

# Поезд
class Train(Base):
    __tablename__ = 'train'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(Unicode(UNICODE_LEN))

    station_from_id: Mapped[int] = mapped_column(
        ForeignKey('station_id')
    )
    station_to: Mapped['Station'] = relationship(
        foreign_keys=[station_from_id],
        back_populates='arrivals',
    )
    departs_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True)
    )
    arrives_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True)
    )
    first_class: Mapped[int] = mapped_column(default=0)
    second_class: Mapped[int] = mapped_column(default=0)
    seats_per_car: Mapped[int] = mapped_column(default=0)

    tickets: Mapped[list['Ticket']] = relationship(
        back_populates='train'
    )
    def __repr__(self): return f'<{self.name}: id={self.id}>'
    __str__ = __repr__

# Билет
class Ticket(Base):
    __tablename__ = 'ticket'

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped['User'] = relationship(
        foreign_keys=[user_id],
        back_populates='tickets',
    )
    train_id: Mapped[int] = mapped_column(ForeignKey('train.id'))
    train: Mapped['Train'] = relationship(
        foreign_keys=[train_id],
        back_populates='tickets',
    )
    price: Mapped[float] = mapped_column(default=0)
    car_class: Mapped[Enum] = mapped_column(Enum(Classes))

    def __repr__(self): return f'<id={self.id} user={self.user} train={self.train}>'

    __str__ = __repr__

# Пользователь
class User(Base):
    __tablename__ = 'user'
    pwd_separator = '#'

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(
        Unicode(UNICODE_LEN), nullable=False
    )
    email: Mapped[str] = mapped_column(Unicode(2 * UNICODE_LEN))
    password: Mapped[str] = mapped_column(Unicode(2 * UNICODE_LEN))
    role: Mapped[Enum] = mapped_column(Enum(Roles))
    tickets: Mapped[list['Ticket']] = relationship(back_populates='user')
    def is_valid_password(self, password: str):
        """Проверяет, совпадает ли переданный пароль с тем, который хранится в базе данных."""
        salt, stored_hash = self.password.split(self.pwd_separator)
        computed_hash = hash(password=password, salt=bytes.fromhex(salt))
        return secrets.compare_digest(stored_hash, computed_hash)
    @classmethod
    def hash_password(cls, password: str, salt: bytes = None):