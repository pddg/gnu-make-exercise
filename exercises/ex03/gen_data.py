import argparse
import csv
from pathlib import Path
from typing import List

from mimesis import schema


def generate_data_set(num: int) -> List[dict]:
    _ = schema.Field('ja')
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


def main():
    parser = argparse.ArgumentParser(description="Test data generator")
    parser.add_argument("filename",
                        type=Path,
                        help="Path to output file name")
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
    if not parent_dir.exists:
        print(f"'{parent_dir}' does not exist.")
        exit(1)
    body = generate_data_set(num)
    write_to_csv(body, args.filename)


if __name__ == "__main__":
    main()
    