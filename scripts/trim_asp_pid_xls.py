#!/usr/bin/env python3
"""Trim ASP org PID transaction spreadsheet: drop non-MIG product families in column G."""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

DROP_VALUES = frozenset(
    {
        "Collaboration",
        "Cisco Compute",
        "Enterprise Switching",
        "Wireless",
    }
)

SEARCH_DIRS = [
    Path("/Users/brucemcdougall/Documents/DSE"),
    Path("/Users/brucemcdougall/Documents/DSE/DSE"),
]


def find_asp_file(explicit: Path | None) -> Path:
    if explicit is not None:
        if not explicit.exists():
            raise FileNotFoundError(f"File not found: {explicit}")
        return explicit

    candidates: list[Path] = []
    for directory in SEARCH_DIRS:
        if not directory.is_dir():
            continue
        for pattern in ("ASP*.xlsx", "ASP*.xls", "ASP*.xlsm", "asp*.xlsx", "asp*.xls"):
            candidates.extend(directory.glob(pattern))

    if not candidates:
        searched = ", ".join(str(d) for d in SEARCH_DIRS)
        raise FileNotFoundError(
            f"No ASP* spreadsheet found. Searched: {searched}. "
            "Pass --input /path/to/file.xlsx"
        )

    return max(candidates, key=lambda p: p.stat().st_mtime)


def load_sheet(path: Path) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".xls":
        return pd.read_excel(path, engine="xlrd")
    return pd.read_excel(path, engine="openpyxl")


def column_g_name(df: pd.DataFrame) -> str:
    if len(df.columns) <= 6:
        raise ValueError(
            f"Expected column G (index 6); sheet has {len(df.columns)} columns: "
            f"{list(df.columns)}"
        )
    return df.columns[6]


def trim_and_sort(df: pd.DataFrame) -> tuple[pd.DataFrame, str, dict[str, int]]:
    col_g = column_g_name(df)
    before = len(df)
    counts = df[col_g].value_counts(dropna=False).to_dict()

    trimmed = df[~df[col_g].isin(DROP_VALUES)].copy()
    removed = before - len(trimmed)

    sort_cols = list(trimmed.columns[: min(7, len(trimmed.columns))])
    trimmed = trimmed.sort_values(by=sort_cols, kind="mergesort", na_position="last")
    trimmed = trimmed.reset_index(drop=True)

    stats = {
        "before": before,
        "after": len(trimmed),
        "removed": removed,
        **{f"dropped_{v.replace(' ', '_')}": int(counts.get(v, 0)) for v in DROP_VALUES},
    }
    return trimmed, col_g, stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="Path to ASP* spreadsheet")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path (default: <input stem>-trimmed.xlsx next to input)",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite input after creating a timestamped .bak backup",
    )
    args = parser.parse_args()

    src = find_asp_file(args.input)
    print(f"Input:  {src} ({src.stat().st_size / (1024 * 1024):.1f} MB)")

    df = load_sheet(src)
    col_g = column_g_name(df)
    print(f"Column G header: {col_g!r}")
    print(f"Unique values in column G ({df[col_g].nunique()}):")
    for value, count in df[col_g].value_counts().head(20).items():
        mark = " [DROP]" if value in DROP_VALUES else ""
        print(f"  {value!r}: {count}{mark}")

    trimmed, _, stats = trim_and_sort(df)

    if args.in_place:
        backup = src.with_suffix(src.suffix + f".bak.{datetime.now():%Y%m%d-%H%M%S}")
        shutil.copy2(src, backup)
        out = src
        print(f"Backup: {backup}")
    else:
        out = args.output or src.with_name(f"{src.stem}-trimmed.xlsx")

    trimmed.to_excel(out, index=False, engine="openpyxl")

    print("\nResults:")
    print(f"  Rows before:  {stats['before']:,}")
    print(f"  Rows removed: {stats['removed']:,}")
    print(f"  Rows after:   {stats['after']:,}")
    for value in DROP_VALUES:
        key = f"dropped_{value.replace(' ', '_')}"
        print(f"  Removed {value!r}: {stats[key]:,}")
    print(f"Output: {out}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
