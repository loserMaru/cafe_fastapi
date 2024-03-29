from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, select, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from database.db import database

Base = declarative_base()

# DATABASE_URL = "postgresql://postgres:4863826M@localhost/cafe_fastapi"
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = SessionLocal()


class CafeModel(Base):
    __tablename__ = "cafe"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    address = Column(String(255), index=True)
    description = Column(Text, index=True)

    drinks = relationship("DrinksModel", back_populates="cafe")
    orders = relationship("OrderModel", back_populates="cafe")
    products = relationship("ProductsModel", back_populates="cafe")
    favorites = relationship("FavoriteModel", back_populates="cafe")
    ratings = relationship("RatingModel", back_populates="cafe")


class CoffeeModel(Base):
    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    description = Column(Text, index=True)
    location = Column(String(255), index=True)

    weights = relationship("WeightModel", back_populates="coffee")
    orders = relationship("OrderModel", back_populates="coffee")
    products = relationship("ProductsModel", back_populates="coffee")


class DrinksModel(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    description = Column(Text, index=True)

    cafe_id = Column(Integer, ForeignKey("cafe.id"))

    cafe = relationship("CafeModel", back_populates="drinks")
    weights = relationship("WeightModel", back_populates="drinks")
    orders = relationship("OrderModel", back_populates="drinks")
    products = relationship("ProductsModel", back_populates="drinks")


class DessertModel(Base):
    __tablename__ = "dessert"

    id = Column(Integer, primary_key=True, index=True)
    products = relationship("ProductsModel", back_populates="dessert")


class WeightModel(Base):
    __tablename__ = "weight"

    id = Column(Integer, primary_key=True, index=True)
    weight = Column(String(45), index=True)
    price = Column(Integer, index=True)

    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    drinks_id = Column(Integer, ForeignKey("drinks.id"))

    coffee = relationship("CoffeeModel", back_populates="weights")
    drinks = relationship("DrinksModel", back_populates="weights")
    orders = relationship("OrderModel", back_populates="weight")


class OrderModel(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(45), index=True)
    total_price = Column(Float, index=True)
    count = Column(Integer, index=True)
    drink_type = Column(String(45), index=True)

    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    drinks_id = Column(Integer, ForeignKey("drinks.id"))
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    weight_id = Column(Integer, ForeignKey("weight.id"))

    cafe = relationship("CafeModel", back_populates="orders")
    drinks = relationship("DrinksModel", back_populates="orders")
    coffee = relationship("CoffeeModel", back_populates="orders")
    weight = relationship("WeightModel", back_populates="orders")


class ProductsModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    drinks_id = Column(Integer, ForeignKey("drinks.id"))
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    dessert_id = Column(Integer, ForeignKey("dessert.id"))

    cafe = relationship("CafeModel", back_populates="products")
    drinks = relationship("DrinksModel", back_populates="products")
    coffee = relationship("CoffeeModel", back_populates="products")
    dessert = relationship("DessertModel", back_populates="products")


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True)
    password = Column(String(255), index=True)
    role = Column(String(45), index=True)

    favorites = relationship("FavoriteModel", back_populates="user")
    ratings = relationship("RatingModel", back_populates="user")

    @classmethod
    async def get_by_email(cls, email: str):
        query = select(cls).where(cls.email == email)
        result = await database.execute(query)
        return result.scalar_one()


class FavoriteModel(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    cafe = relationship("CafeModel", back_populates="favorites")
    user = relationship("UserModel", back_populates="favorites")


class RatingModel(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    cafe = relationship("CafeModel", back_populates="ratings")
    user = relationship("UserModel", back_populates="ratings")


# Base.metadata.create_all(bind=engine)
