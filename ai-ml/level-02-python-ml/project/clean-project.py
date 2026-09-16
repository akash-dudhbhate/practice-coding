"""
LEVEL 02 PROJECT — Messy Data Cleaner
========================================

You've been handed a CSV file that a colleague exported badly.
It has: missing ages, duplicate rows, inconsistent country names,
and salaries stored as strings with "$" and commas.

YOUR DATA (embedded — no file needed):
  records below simulate the CSV rows.

BUILD:
  Write `clean(records)` that returns a clean list of dicts:
    1. Remove exact duplicate rows
    2. Fill missing "age" with the median age
    3. Normalize "country": "USA"/"usa"/"US" → "USA"
    4. Parse "salary": "$52,000" → 52000 (int); missing → None
  Then `report(cleaned)` prints per-country count + avg age.

INPUT EXAMPLE:
  records = [
      {"name": "Ana", "age": "28", "country": "USA", "salary": "$52,000"},
      {"name": "Ana", "age": "28", "country": "USA", "salary": "$52,000"},  # dupe
      {"name": "Ben", "age": "",   "country": "usa", "salary": "$61,500"},
      {"name": "Cid", "age": "35", "country": "IN",  "salary": ""},
      {"name": "Dee", "age": "41", "country": "US",  "salary": "$48,000"},
  ]

EXPECTED OUTPUT:
  ```
  Cleaned 5 → 4 rows
  Ben's age filled with median: 34.5
  USA: 3 people, avg age 33.0
  IN: 1 person, avg age 35.0
  ```

STEPS:
  1. Dedup with a set of tuple(row.items())
  2. Collect numeric ages → statistics.median
  3. Normalize + parse
  4. Group by country, average ages

No sklearn needed — pure Python + statistics.
"""

import statistics

RECORDS = [
    {"name": "Ana", "age": "28", "country": "USA", "salary": "$52,000"},
    {"name": "Ana", "age": "28", "country": "USA", "salary": "$52,000"},
    {"name": "Ben", "age": "",   "country": "usa", "salary": "$61,500"},
    {"name": "Cid", "age": "35", "country": "IN",  "salary": ""},
    {"name": "Dee", "age": "41", "country": "US",  "salary": "$48,000"},
]


def clean(records):
    """Return a deduplicated, normalized list of record dicts."""
    # TODO: implement the 4 cleaning steps above
    pass


def report(cleaned):
    """Print per-country stats."""
    # TODO: group by country, print count + avg age
    pass


if __name__ == "__main__":
    cleaned = clean(RECORDS)
    print(f"Cleaned {len(RECORDS)} → {len(cleaned)} rows")
    report(cleaned)
