# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from your_database_module import session  # Replace 'your_database_module' with the actual module where you create your SQLAlchemy session.

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary='reviews')

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Find and return the restaurant with the highest star rating from this customer
        highest_rating = 0
        favorite = None
        for review in self.reviews:
            if review.rating > highest_rating:
                highest_rating = review.rating
                favorite = review.restaurant
        return favorite

    def add_review(self, restaurant, rating):
        # Create a new review for the specified restaurant
        new_review = Review(restaurant=restaurant, customer=self, rating=rating)
        session.add(new_review)
        session.commit()  # Commit the changes to the database

    def delete_reviews(self, restaurant):
        # Delete all reviews for the specified restaurant
        for review in self.reviews:
            if review.restaurant == restaurant:
                session.delete(review)
        session.commit()  # Commit the changes to the database

    def restaurants(self):
        return [review.restaurant for review in self.reviews]
