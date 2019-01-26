# Copyright PT
"""
This script reads and interpret the data on traffic from all UK counties.
"""

# todo list
# 1) add condition to fill values when missing
# 2) add condition to fill values when columns are missing
# 3) write function which calculates ratio of pedalcycle, motorcycle, carstaxis, 
#    busescoaches, lightgoodvehicles
# 4) write function to check that sum of those vehicles match allmotorvehicles
# 4b) if a match is never found, make sure that allmotorvehicles is always greater than the sum
# 4c) count the remaining vehicles and label them as 'other'
# 5) create library and main function
# 6) read columns to check from a json file


import pandas as pd
import numpy as np
import scipy
import sys
import os

directory = sys.argv[1]

columns_to_check = ['Year', 'CP', 'Estimation_method', 'Estimation_method_detailed',
       'Region', 'LocalAuthority', 'Road', 'RoadCategory', 'Easting',
       'Northing', 'StartJunction', 'EndJunction', 'LinkLength_miles',
       'PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches',
       'LightGoodsVehicles', 'V2AxleRigidHGV', 'V3AxleRigidHGV',
       'V4or5AxleRigidHGV', 'V3or4AxleArticHGV', 'V5AxleArticHGV',
       'V6orMoreAxleArticHGV', 'AllHGVs', 'AllMotorVehicles']

total_df = pd.DataFrame()

for root, dirs, files in os.walk(directory):
    for file_ in files:
        if file_.endswith(".csv"):
            df = pd.read_csv(os.path.join(root, file_))
            if list(df.columns) == columns_to_check:
                total_df = total_df.append(df, ignore_index=True)

print(total_df.shape)
