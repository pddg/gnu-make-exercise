import argparse
import csv
import json
from pathlib import Path
from typing import List

from mimesis import schema


def generate_data_set(num: int, seed: str) -> List[dict]:
    _ = schema.Field('ja', seed=seed)
    profile_schema = lambda: {
        "name": _("person.full_name"),
        "email": _("person.email"),
    }
    s = schema.Schema(profile_schema)
    return s.create(iterations=num)


def write_to_csv(data: List[dict], filepath: Path):
    header = data[0].keys()
    with filepath.open('w') as fp:
         writer = csv.DictWriter(fp, header, quoting=csv.QUOTE_MINIMAL)
         writer.writeheader()
         writer.writerows(data)


def write_to_json(data: List[dict], filepath: Path):
    with filepath.open('w') as fp:
        json.dump({'data': data}, fp)


def main():
    parser = argparse.ArgumentParser(description="Test data generator")
    parser.add_argument("filename",
                        type=Path,
                        help="Path to output file name")
    parser.add_argument("-s",
                        "--seed",
                        type=Path,
                        default="seed",
                        help="Path to seed file")
    parser.add_argument("-f",
                        "--format",
                        default="csv",
                        choices=["json", "csv"],
                        help="Format of output")
    parser.add_argument("-n",
                        "--number",
                        type=int,
                        default=100,
                        help="Number of data record to generate")
    args = parser.parse_args()
    num = args.number
    if num < 1:
        print(f"Number must be an positive integer. {num} is given.")
        exit(1)
    parent_dir = args.filename.parent
    if not parent_dir.exists():
        print(f"'{parent_dir}' does not exist.")
        exit(1)
    seed_file = args.seed
    if not seed_file.exists():
        print(f"'{seed_file}' does not exist.")
        exit(1)
    with seed_file.open('r') as fp:
        seed = fp.read().strip()
    body = generate_data_set(num, seed)
    write_func = globals()[f"write_to_{args.format}"]
    write_func(body, args.filename)


if __name__ == "__main__":
    main()
    