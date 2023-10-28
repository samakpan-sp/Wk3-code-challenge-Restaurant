# debug.py

from database import session
from models import Customer, Restaurant, Review

# Testing the methods
first_customer = session.query(Customer).first()
print(first_customer.full_name())

# Implement the logic for finding and printing the favorite restaurant
# Example:
# favorite_restaurant = first_customer.favorite_restaurant()
# print(f"Favorite restaurant: {favorite_restaurant.name}")

# Implement the logic for adding a new review
# Example:
# restaurant_to_review = session.query(Restaurant).filter_by(name="Your Restaurant Name").first()
# first_customer.add_review(restaurant_to_review, 5)  # 5-star rating

# Implement the logic for deleting reviews
# Example:
# restaurant_to_delete_reviews = session.query(Restaurant).filter_by(name="Restaurant to Delete Reviews").first()
# first_customer.delete_reviews(restaurant_to_delete_reviews)

# Implement logic to fetch and print customer's reviews and restaurants
# Example:
# customer_reviews = first_customer.reviews()
# for review in customer_reviews:
#     print(f"Review: {review.restaurant.name} - Rating: {review.rating}")

# customer_restaurants = first_customer.restaurants()
# for restaurant in customer_restaurants:
#     print(f"Reviewed Restaurant: {restaurant.name}")

session.close()
