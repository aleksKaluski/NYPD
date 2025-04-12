from pathlib import Path
import csv


def save_to_csv(stats: list, output_path: str):
    dataset_path = Path(output_path)
    assert dataset_path.exists()

    with open(dataset_path, 'w', newline='') as csvfile:
        fieldnames = ["feature", "mean", "median", "sd"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for s in stats:
            writer.writerow(s)
        print("Files where saved")
