import pandas as pd

# # CONTEXT DATAFRAME


context_names = [
    "interaction_id",
    "context_location",
    "context_time_of_day",
    "context_weather",
]


context_df = pd.read_csv(r"data\context.csv")
print(context_df.head())


context_df.columns = context_names


print(context_df.isnull().sum())
print(context_df.shape)

# # INTERACTIONS DATAFRAME


interaction_names = [
    "user_id",
    "restaurant_id",
    "interaction_type",
    "interaction_timestamp",
]


interactions_df = pd.read_csv(r"data\interactions.csv")
print(interactions_df.head())


interactions_df.columns = interaction_names


print(interactions_df.isnull().sum())
print(interactions_df.shape)


interaction_id_list = []

for i in range(len(interactions_df["restaurant_id"])):
    interaction_id_list.append(i + 1)

interactions_df["interaction_id"] = interaction_id_list
print(interactions_df.head())


# Inner Join:
final_df = pd.merge(context_df, interactions_df, on="interaction_id", how="inner")
print(final_df)

# # RESTAURANTS DATAFRAME


restaurant_names = [
    "restaurant_id",
    "restaurant_name",
    "restaurant_cuisine",
    "restaurant_rating",
    "restaurant_price_range",
    "restaurant_location",
]


restaurants_df = pd.read_csv(r"data\restaurants.csv")
print(restaurants_df.head())


restaurants_df.columns = restaurant_names


print(restaurants_df.isnull().sum())
print(restaurants_df.shape)


# Inner Join:
final_df = pd.merge(final_df, restaurants_df, on="restaurant_id", how="inner")
print(final_df.shape)


print(final_df.columns)

# # USERS DATAFRAME


user_names = ["user_id", "user_age", "user_gender", "user_preferred_cuisine"]


users_df = pd.read_csv(r"data\users.csv")
print(users_df.head())


users_df.columns = user_names


print(users_df.isnull().sum())
print(users_df.shape)


final_df = pd.merge(final_df, users_df, on="user_id", how="inner")
print(final_df.columns)
print(final_df.shape)


print(final_df.isnull().sum())
