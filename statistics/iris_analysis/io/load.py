"""
File iris_analysis/io/load.py should contain functions needed to load and parse
data/iris.csv. I attach external iris dataset file.
"""

import csv
import os
import numpy as np
from pathlib import Path

def load_data(dataset_path:str):
    dataset_path = Path(dataset_path)
    assert dataset_path.exists()
    assert dataset_path.is_file()

    with open(dataset_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        sepal_length = []
        sepal_width = []
        petal_length = []
        petal_width = []
        for row in reader:
            sepal_length.append(row[0])
            sepal_width.append(row[1])
            petal_length.append(row[2])
            petal_width.append(row[3])
        return sepal_length, sepal_width, petal_length, petal_width


res = load_data(r'C:\NYPD_github\NYPD\statistics\iris.csv')
print(res)
