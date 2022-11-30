import calendar


def month_no(month_name: str) -> int:
    full_names = dict(
        (month, index)
        for index, month in enumerate(calendar.month_name) if month
    )

    abbreviations = dict(
        (month, index)
        for index, month in enumerate(calendar.month_abbr) if month
    )

    return (
        full_names[month_name] if month_name in full_names
        else abbreviations[month_name]
    )

