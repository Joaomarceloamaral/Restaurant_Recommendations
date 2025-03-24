import pandas as pd
from modules.dataframe_analysis import create_tableone
from modules.data_treatment import (
    create_context_df,
    create_interactions_df,
    create_restaurants_df,
    create_users_df,
)


# # CONTEXT DATAFRAME
context_df = create_context_df()

# # INTERACTIONS DATAFRAME
interactions_df = create_interactions_df()

# # RESTAURANTS DATAFRAME
restaurants_df = create_restaurants_df()

# # USERS DATAFRAME
users_df = create_users_df()


final_df = pd.merge(context_df, interactions_df, on="interaction_id", how="inner")
final_df = pd.merge(final_df, restaurants_df, on="restaurant_id", how="inner")
final_df = pd.merge(final_df, users_df, on="user_id", how="inner")

table1 = create_tableone(final_df)
print(table1)
