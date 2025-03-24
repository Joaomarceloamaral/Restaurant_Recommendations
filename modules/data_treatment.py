import pandas as pd
from constants.dataframe_utils import (
    CONTEXT_NAMES,
    INTERACTION_NAMES,
    RESTAURANT_NAMES,
    USER_NAMES,
)


def create_context_df():
    """
    Create the context dataframe from the context.csv file.
    """
    context_df = pd.read_csv(r"restaurants\data\context.csv")

    context_df.columns = CONTEXT_NAMES

    return context_df


def create_interactions_df():
    """
    Create the interactions dataframe from the interactions.csv file.
    """
    interactions_df = pd.read_csv(r"restaurants\data\interactions.csv")

    interactions_df.columns = INTERACTION_NAMES

    interaction_id_list = []

    for i in range(len(interactions_df["restaurant_id"])):
        interaction_id_list.append(i + 1)

    interactions_df["interaction_id"] = interaction_id_list

    return interactions_df


def create_restaurants_df():
    """
    Create the restaurants dataframe from the restaurants.csv file.
    """
    restaurants_df = pd.read_csv(r"restaurants\data\restaurants.csv")

    restaurants_df.columns = RESTAURANT_NAMES

    return restaurants_df


def create_users_df():
    """
    Create the users dataframe from the users.csv file.
    """
    users_df = pd.read_csv(r"restaurants\data\users.csv")

    users_df.columns = USER_NAMES

    return users_df
