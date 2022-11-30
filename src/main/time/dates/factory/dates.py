from src.main.time.dates.formats import factory
from src.main.time.dates.implementation.date import Date
from src.main.time.dates.interface.date import DateInterface


def from_string(date: str) -> DateInterface:
    date_formatter = factory.formatter(date)

    return Date(date_formatter.day, date_formatter.month, date_formatter.year)


def from_integers(day: int, month: int, year: int):
    return Date(day, month, year)
