from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Эта функция читает текст.
    """
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)

import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None, encoding: str = "utf-8") -> None:
    """
    Эта функция создает csv файл.
    """
    p = Path(path)
    rows = list(rows)
    if len(rows) != 0:
        cnt_elem = len(rows[0])
    else:
        cnt_elem = 0
    with p.open("w", newline="", encoding=encoding) as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            if len(r) != cnt_elem:
                raise ValueError()
            w.writerow(r)
        

