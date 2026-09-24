"""Small CSV parser fixture preserving quoted newline characters."""
import csv
import io


def parse_csv(text: str) -> list[list[str]]:
    return list(csv.reader(io.StringIO(text, newline="")))
