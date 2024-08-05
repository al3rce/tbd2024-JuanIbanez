from datetime import datetime, date
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]

    grupo_users_travels: Mapped[list["User_Travel"]] = relationship(back_populates="grupo_users")
    grupo_expenses: Mapped["Expense"] = relationship(back_populates="grupo_users")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")

class Travel(Base):
    __tablename__ = "travels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    start_date: Mapped[date]
    end_date: Mapped[date]

    grupo_accommodations: Mapped["Accommodation"] = relationship(back_populates="grupo_travels")
    grupo_transports: Mapped["Transport"] = relationship(back_populates="grupo_travels")
    grupo_expenses: Mapped["Expense"] = relationship(back_populates="grupo_travels")
    grupo_users_travels: Mapped[list["User_Travel"]] = relationship(back_populates="grupo_travels")
    grupo_activities: Mapped["Activity"] = relationship(back_populates="grupo_travels")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")

class Accommodation(Base):
    __tablename__ = "accommodations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    location: Mapped[str]
    price: Mapped[int]
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    observations: Mapped[str]
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    gasto: Mapped[Optional[int]] = mapped_column(ForeignKey("expense.id")) #gasto opcional

    grupo_cities: Mapped["City"] = relationship(back_populates="grupo_accommodations")
    grupo_travels: Mapped["Travel"] = relationship(back_populates="grupo_accommodations")
    grupo_gasto: Mapped["Expense"] = relationship(back_populates="grupo_accommodations")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")
    
class Transport(Base):
    __tablename__ = "transports"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str]
    company: Mapped[str]
    price: Mapped[int]
    start_datetime: Mapped[datetime]
    start_location: Mapped[str]
    end_datetime: Mapped[datetime]
    end_location: Mapped[str]
    start_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    end_city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    gasto: Mapped[Optional[int]] = mapped_column(ForeignKey("expense.id")) #gasto opcional

    grupo_cities: Mapped["City"] = relationship("City", foreign_keys=[start_city_id], back_populates="grupo_transports")
    grupo_cities2: Mapped["City"] = relationship("City", foreign_keys=[end_city_id], back_populates="grupo_transports2")
    grupo_travels: Mapped["Travel"] = relationship("Travel", back_populates="grupo_transports")
    grupo_gasto: Mapped["Expense"] = relationship(back_populates="grupo_transports")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")

class Activity(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    location: Mapped[str]
    start_datetime: Mapped[datetime]
    price: Mapped[int]
    duration: Mapped[int]
    city_id: Mapped[int] = mapped_column(ForeignKey("cities.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))
    gasto: Mapped[Optional[int]] = mapped_column(ForeignKey("expense.id")) #gasto opcional

    grupo_cities: Mapped["City"] = relationship("City", back_populates="grupo_activities")
    grupo_travels: Mapped["Travel"] = relationship("Travel", back_populates="grupo_activities")
    grupo_gasto: Mapped["Expense"] = relationship(back_populates="grupo_activities")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")

class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    amount: Mapped[int]
    datetime: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"))

    grupo_users: Mapped["User"] = relationship(back_populates="grupo_expenses")
    grupo_travels: Mapped["Travel"] = relationship(back_populates="grupo_expenses")

    grupo_activities: Mapped["Activity"] = relationship(back_populates="grupo_expenses")
    grupo_transports: Mapped["Transport"] = relationship(back_populates="grupo_expenses")
    grupo_accommodation: Mapped["Accommodation"] = relationship(back_populates="grupo_expenses")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")

class City(Base):
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    country: Mapped[str]

    grupo_accommodations: Mapped["Accommodation"] = relationship(back_populates="grupo_cities")
    grupo_transports: Mapped["Transport"] = relationship("Transport", foreign_keys="[Transport.start_city_id]", back_populates="grupo_cities")
    grupo_transports2: Mapped["Transport"] = relationship("Transport", foreign_keys="[Transport.end_city_id]", back_populates="grupo_cities2")
    grupo_activities: Mapped["Activity"] = relationship(back_populates="grupo_cities")

    enabled: Mapped[bool] = mapped_column(default=True, server_default="1")

class User_Travel(Base):
    __tablename__ = "users_travels"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    travel_id: Mapped[int] = mapped_column(ForeignKey("travels.id"), primary_key=True)

    grupo_users: Mapped["User"] = relationship(back_populates="grupo_users_travels")
    grupo_travels: Mapped["Travel"] = relationship(back_populates="grupo_users_travels")