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
