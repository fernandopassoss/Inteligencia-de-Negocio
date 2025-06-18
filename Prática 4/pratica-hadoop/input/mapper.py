#!/usr/bin/env python3

import sys

def main():
    header_skipped = False
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        if not header_skipped:
            header_skipped = True
            continue

        columns = line.split(',')
        for i, _ in enumerate(columns):
            print(f"{i}\t1")

if __name__ == "__main__":
    main()