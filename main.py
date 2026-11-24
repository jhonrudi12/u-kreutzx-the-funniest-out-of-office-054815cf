#!/usr/bin/env python3
"""The Funniest Out-of-Office — writes one out-of-office line to /output/entry.txt."""

import os

ENTRY = "Out until Monday. In my absence, please direct all emergencies to my plant, Gerald. He has never let me down, mostly because he can't move."


def main():
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
