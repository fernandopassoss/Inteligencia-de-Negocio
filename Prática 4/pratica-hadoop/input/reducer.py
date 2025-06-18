#!/usr/bin/env python3

import sys

def main():
    current_column = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            column_index, count = line.split('\t', 1)
            count = int(count)
        except ValueError:
            # Pula linhas mal formatadas
            continue

        if current_column == column_index:
            current_count += count
        else:
            if current_column is not None:
                column_names = {
                    "0": "id",
                    "1": "valor1",
                    "2": "valor2"
                }
                column_name = column_names.get(current_column, f"coluna_{current_column}")
                print(f"{column_name}\t{current_count}")
            current_column = column_index
            current_count = count

    if current_column is not None:
        column_names = {
            "0": "id",
            "1": "valor1",
            "2": "valor2"
        }
        column_name = column_names.get(current_column, f"coluna_{current_column}")
        print(f"{column_name}\t{current_count}")

if __name__ == "__main__":
    main()