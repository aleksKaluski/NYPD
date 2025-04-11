"""
File iris_analysis/io/load.py should contain functions needed to load and parse
data/iris.csv. I attach external iris dataset file.
"""

import csv
import os
import numpy as np
from pathlib import Path

def load_data(dataset_path:str) -> dict:
    dataset_path = Path(dataset_path)
    assert dataset_path.exists()
    assert dataset_path.is_file()

    with open(dataset_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        result = {"sepal_length" : [],
                  "sepal_width" : [],
                  "petal_length" : [],
                  "petal_width" : []}

        # skip the first row
        next(reader, None)
        for row in reader:
            result["sepal_length"].append(float(row[0]))
            result["sepal_width"].append(float(row[1]))
            result["petal_length"].append(float(row[2]))
            result["petal_width"].append(float(row[3]))
        return result

print(load_data(r"C:\NYPD_github\NYPD\statistics\iris.csv"))