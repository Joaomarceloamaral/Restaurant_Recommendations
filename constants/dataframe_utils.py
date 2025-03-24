"""
in the Restaurant Recommendations system. The constants are lists of column
names that correspond to different aspects of the data.
Constants:
    CONTEXT_NAMES (list): Column names related to the context of interactions,
        such as location, time of day, and weather.
    INTERACTION_NAMES (list): Column names related to user-restaurant interactions,
        including user ID, restaurant ID, interaction type, and timestamp.
    RESTAURANT_NAMES (list): Column names describing restaurant details, such as
        ID, name, cuisine, rating, price range, and location.
    USER_NAMES (list): Column names describing user details, such as ID, age,
        gender, and preferred cuisine.
    CATEGORICAL_COLUMNS (list): Column names that represent categorical data,
        such as cuisine, price range, and location.
    CONTINUOUS_COLUMNS (list): Column names that represent continuous numerical
        data, such as restaurant ratings.
    SOLO_COLUMN (str): A single column name representing the restaurant name.
This module defines constants used for managing and processing dataframes
"""

CONTEXT_NAMES = [
    "interaction_id",
    "context_location",
    "context_time_of_day",
    "context_weather",
]

INTERACTION_NAMES = [
    "user_id",
    "restaurant_id",
    "interaction_type",
    "interaction_timestamp",
]

RESTAURANT_NAMES = [
    "restaurant_id",
    "restaurant_name",
    "restaurant_cuisine",
    "restaurant_rating",
    "restaurant_price_range",
    "restaurant_location",
]

USER_NAMES = ["user_id", "user_age", "user_gender", "user_preferred_cuisine"]

CATEGORICAL_COLUMNS = [
    "restaurant_cuisine",
    "restaurant_price_range",
    "restaurant_location",
]

CONTINUOUS_COLUMNS = ["restaurant_rating"]

SOLO_COLUMN = "restaurant_name"
