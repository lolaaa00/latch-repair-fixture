"""Small CSV parser fixture with an intentionally documented newline defect."""
import csv


def parse_csv(text: str) -> list[list[str]]:
    return list(csv.reader(text.splitlines()))
