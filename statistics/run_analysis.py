from iris_analysis.io import load, save
from iris_analysis import calculate as cal
import os


os.chdir(r"C:\NYPD_github\NYPD\statistics")
print(os.getcwd())

iris = 'iris.csv'
output = 'result.csv'
data = load.load_data(dataset_path=iris)
result = cal.stats_for_all(data)
save.save_to_csv(stat_dict=result, output_path=output)

