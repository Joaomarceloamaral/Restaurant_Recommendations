"""
This module provides functionality for creating a TableOne object from a given dataframe.
Functions:
----------
- create_tableone(dataframe):
    Creates a TableOne object for descriptive statistics and comparison of categorical
    and continuous variables grouped by a specified column.
    Parameters:
    ----------
    dataframe : pandas.DataFrame
        The input dataframe containing the data to be analyzed.
    Returns:
    -------
    tableone.TableOne
        A TableOne object containing the descriptive statistics and hypothesis test results.
Constants:
----------
- CATEGORICAL_COLUMNS : list
    A list of column names in the dataframe that are categorical variables.
- CONTINUOUS_COLUMNS : list
    A list of column names in the dataframe that are continuous variables.
- SOLO_COLUMN : str
    The name of the column used for grouping the data in the TableOne analysis.
"""

from tableone import TableOne

from constants.dataframe_utils import (
    CATEGORICAL_COLUMNS,
    CONTINUOUS_COLUMNS,
    SOLO_COLUMN,
)


def create_tableone(dataframe):
    """
    Create the tableone from the final dataframe.
    """

    table1 = TableOne(
        dataframe,
        categorical=CATEGORICAL_COLUMNS,
        continuous=CONTINUOUS_COLUMNS,
        groupby=SOLO_COLUMN,
        pval=True,
        htest_name=True,
        overall=True,
        decimals=2,
        missing=False,
    )

    return table1
