import csv
import json

def convert_csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(rows, jsonfile, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    convert_csv_to_json("profiles1.csv", "web/data.json")
