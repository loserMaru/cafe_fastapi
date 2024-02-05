from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cafe(Base):
    __tablename__ = "cafe"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    address = Column(String(255), index=True)
    description = Column(Text, index=True)


class Coffee(Base):
    __tablename__ = "coffee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    description = Column(Text, index=True)
    location = Column(String(255), index=True)


class Drinks(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), index=True)
    drinks_123 = Column(String(45))
    drinks_1231 = Column(String(45))
    drinks_3123 = Column(String(45))
    cafe_id = Column(Integer, ForeignKey("cafe.id"))

    cafe = relationship("Cafe", back_populates="drinks")


Cafe.drinks = relationship("Drinks", order_by=Drinks.id, back_populates="cafe")


class Desert(Base):
    __tablename__ = "desert"

    id = Column(Integer, primary_key=True, index=True)


class Weight(Base):
    __tablename__ = "weight"

    id = Column(Integer, primary_key=True, index=True)
    weight = Column(String(45), index=True)
    price = Column(Integer, index=True)
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    drinks_id = Column(Integer, ForeignKey("drinks.id"))

    coffee = relationship("Coffee", back_populates="weights")
    drinks = relationship("Drinks", back_populates="weights")


Coffee.weights = relationship("Weight", order_by=Weight.id, back_populates="coffee")
Drinks.weights = relationship("Weight", order_by=Weight.id, back_populates="drinks")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    drinks_id = Column(Integer, ForeignKey("drinks.id"))
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    weight_id = Column(Integer, ForeignKey("weight.id"))
    status = Column(String(45), index=True)
    total_price = Column(Float, index=True)
    count = Column(Integer, index=True)
    drink_type = Column(String(45), index=True)

    cafe = relationship("Cafe", back_populates="orders")
    drinks = relationship("Drinks", back_populates="orders")
    coffee = relationship("Coffee", back_populates="orders")
    weight = relationship("Weight", back_populates="orders")


Cafe.orders = relationship("Order", order_by=Order.id, back_populates="cafe")
Drinks.orders = relationship("Order", order_by=Order.id, back_populates="drinks")
Coffee.orders = relationship("Order", order_by=Order.id, back_populates="coffee")
Weight.orders = relationship("Order", order_by=Order.id, back_populates="weight")


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    drinks_id = Column(Integer, ForeignKey("drinks.id"))
    coffee_id = Column(Integer, ForeignKey("coffee.id"))
    desert_id = Column(Integer, ForeignKey("desert.id"))

    cafe = relationship("Cafe", back_populates="products")
    drinks = relationship("Drinks", back_populates="products")
    coffee = relationship("Coffee", back_populates="products")
    desert = relationship("Desert", back_populates="products")


Cafe.products = relationship("Products", order_by=Products.id, back_populates="cafe")
Drinks.products = relationship("Products", order_by=Products.id, back_populates="drinks")
Coffee.products = relationship("Products", order_by=Products.id, back_populates="coffee")
Desert.products = relationship("Products", order_by=Products.id, back_populates="desert")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True)
    password = Column(String(45), index=True)
    role = Column(String(45), index=True)


class Favorite(Base):
    __tablename__ = "favorite"

    id = Column(Integer, primary_key=True, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    cafe = relationship("Cafe", back_populates="favorites")
    user = relationship("User", back_populates="favorites")


Cafe.favorites = relationship("Favorite", order_by=Favorite.id, back_populates="cafe")
User.favorites = relationship("Favorite", order_by=Favorite.id, back_populates="user")


class Rating(Base):
    __tablename__ = "rating"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, index=True)
    cafe_id = Column(Integer, ForeignKey("cafe.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    cafe = relationship("Cafe", back_populates="ratings")
    user = relationship("User", back_populates="ratings")


Cafe.ratings = relationship("Rating", order_by=Rating.id, back_populates="cafe")
User.ratings = relationship("Rating", order_by=Rating.id, back_populates="user")