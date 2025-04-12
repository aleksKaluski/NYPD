from pathlib import Path
import csv


def save_to_csv(stat_dict: dict, output_path: str):
    dataset_path = Path(output_path)
    assert dataset_path.exists()

    rows = []
    for prop, stat in stat_dict.items():
        row = {
            prop: stat,
            'mean': stat['mean'],
            'median': stat['median'],
            'sd': stat['sd'],
        }
        rows.append(row)
        print(rows)


    with open(dataset_path, 'w', newline='') as csvfile:
        fieldnames = ["feature", "mean", "median", "sd"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(rows[1])
