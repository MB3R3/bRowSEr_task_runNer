import csv
from pathlib import Path
from core.utils import ensure_directory


def export_csv(data, filepath:Path):

    ensure_directory(filepath.parent)

    if not data:
        print("There is no data to export")

        return
    
    headers = data[0].keys()

    with open(filepath, "w", encoding="utf-8", newline="") as file:

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(data)

    print(f"data exported: \n{filepath}")