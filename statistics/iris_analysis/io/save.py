from pathlib import Path
import csv


def save_to_csv(stat_dict: dict, output_path: str):
    dataset_path = Path(output_path)
    assert dataset_path.exists()

    with open(dataset_path, 'w', newline='') as csvfile:
        fieldnames = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(stat_dict)
