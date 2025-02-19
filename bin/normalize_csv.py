#!/usr/bin/env python3

import csv
import sys
import os

def normalize_csv(input_path):
    """
    Reads a CSV by column index, ignoring header names.
    Assumes the CSV has (at least) 4 columns in this order:
      0: symbol
      1: price
      2: price_change
      3: price_percent_change
    Skips the first row (header), then processes subsequent rows.
    Returns a list of dicts with the normalized data.
    """
    assert isinstance(input_path, str), f"Expected string path, got {type(input_path)}"
    assert os.path.exists(input_path), f"File not found: {input_path}"

    normalized_rows = []

    with open(input_path, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        raw_rows = list(reader)  # read entire file into memory

        # Skip the first row (assumed to be a header row).
        data_rows = raw_rows[1:]
        assert len(data_rows) > 0, f"No data found after skipping header in {input_path}"

        # Parse each row by position.
        for row in data_rows:
            # Ensure row has at least 4 columns.
            assert len(row) >= 4, f"Row has fewer than 4 columns: {row}"

            symbol = row[0]
            price = row[1]
            price_change = row[2]
            price_percent_change = row[3]

            normalized_rows.append({
                "symbol": symbol,
                "price": price,
                "price_change": price_change,
                "price_percent_change": price_percent_change
            })

    # Output guard: we must have at least one record.
    assert len(normalized_rows) > 0, "No valid data rows to output"
    return normalized_rows

def write_normalized_csv(normalized_rows, output_path):
    """
    Writes the normalized rows to a new CSV with standard headers:
      symbol, price, price_change, price_percent_change
    """
    assert isinstance(normalized_rows, list), f"Expected list, got {type(normalized_rows)}"
    assert len(normalized_rows) > 0, "Nothing to write"
    assert isinstance(output_path, str), f"Expected string path, got {type(output_path)}"

    fieldnames = ["symbol", "price", "price_change", "price_percent_change"]

    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in normalized_rows:
            writer.writerow(row)

def main():
    if len(sys.argv) < 2:
        print("Usage: python bin/normalize_csv.py <path_to_raw_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    normalized_data = normalize_csv(input_path)
    output_path = f"{input_path}_norm.csv"

    write_normalized_csv(normalized_data, output_path)
    print(f"Normalized CSV created: {output_path}")

if __name__ == "__main__":
    main()
