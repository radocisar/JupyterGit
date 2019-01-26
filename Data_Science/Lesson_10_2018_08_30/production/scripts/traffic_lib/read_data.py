# Copyright PT
"""
This script reads and interpret the data on traffic from all UK counties.
"""

# todo list
# 3) write function which calculates ratio of pedalcycle, motorcycle, carstaxis, 
#    busescoaches, lightgoodvehicles


import pandas as pd
import numpy as np
import json as js
import scipy
import sys
import os


def check_missing_value(list_to_check):
    "This script handles missing or invalid values, setting them to 0"

    for i, l in enumerate(list_to_check):
        try:
            a = int(l)
            del list_to_check[i]
            list_to_check.insert(i, a)
        except:
            del list_to_check[i]
            list_to_check.insert(i, 0)

    return list_to_check


#def check_sum(df):
def check_sum(df, attribute1, attribute2, attribute3, attribute4, attribute5):
    "Checking the sum of all motor vehicles"

    #motorcycles_list = check_missing_value(list(df['Motorcycles']))
    #carstaxis_list = check_missing_value(list(df['CarsTaxis']))
    #busescoaches_list = check_missing_value(list(df['BusesCoaches']))
    #lightgoods_list = check_missing_value(list(df['LightGoodsVehicles']))
    #all_motor_list = check_missing_value(list(df['AllMotorVehicles']))

    motorcycles_list = check_missing_value(list(df[attribute1]))
    carstaxis_list = check_missing_value(list(df[attribute2]))
    busescoaches_list = check_missing_value(list(df[attribute3]))
    lightgoods_list = check_missing_value(list(df[attribute4]))
    all_motor_list = check_missing_value(list(df[attribute5]))

    flag = True
    count = 0
    while count < len(motorcycles_list) and flag is True:
        if motorcycles_list[count] + carstaxis_list[count] + busescoaches_list[count] + lightgoods_list[count] > all_motor_list[count]:
            flag = False
        else:
            count += 1

    return flag


def reading_data(directory):

    # reading columns from a json file
    json_data = open("../data/columns_to_check.json").read()

    json_columns_to_check = js.loads(json_data)
    columns_to_check = json_columns_to_check['columns']

    #columns_to_check = ['Year', 'CP', 'Estimation_method', 'Estimation_method_detailed',
    #       'Region', 'LocalAuthority', 'Road', 'RoadCategory', 'Easting',
    #       'Northing', 'StartJunction', 'EndJunction', 'LinkLength_miles',
    #       'PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches',
    #       'LightGoodsVehicles', 'V2AxleRigidHGV', 'V3AxleRigidHGV',
    #       'V4or5AxleRigidHGV', 'V3or4AxleArticHGV', 'V5AxleArticHGV',
    #       'V6orMoreAxleArticHGV', 'AllHGVs', 'AllMotorVehicles']
    
    total_df = pd.DataFrame()
    
    for root, dirs, files in os.walk(directory):
        for file_ in files:
            if file_.endswith(".csv"):
                df = pd.read_csv(os.path.join(root, file_))
                if list(df.columns) == columns_to_check:
                    #if check_sum(df):
                    if check_sum(df, columns_to_check[14], columns_to_check[15], columns_to_check[16], columns_to_check[17], columns_to_check[25]):
                        # appending the dataframe
                        total_df = total_df.append(df, ignore_index=True)
    
    print(total_df.shape)
