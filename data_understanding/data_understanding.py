#!/bin/python

from data_understanding.data_description import data_description_handler
from data_understanding.data_exploration import data_explore_handler
from data_understanding.data_quality_verification import data_quality_verification_handler

# print("Hello Data Understanding")

def crisp_dm_phase_2_data_understanding(df):
    print("crisp_dm_phase_2_data_understanding phase")
    data_description_handler(df)
    data_explore_handler(df)
    data_quality_verification_handler(df)

# Step 1 - Descript the data
# Call the relevant functioballity



# Step 2 - Explore the data
# ....


# Step 3 - Veify Data Quality