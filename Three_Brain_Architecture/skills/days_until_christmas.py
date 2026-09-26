from datetime import datetime, timedelta

def run():
    today = datetime.today()
    christmas_day = datetime(today.year, 12, 25)
    if today > christmas_day:
        days_until_christmas = (datetime(today.year + 1, 12, 25) - today).days
    days_until_christmas = (christmas_day - today).days
    return days_until_christmas