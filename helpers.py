import datetime


def generate_text_with_date(base_text, offset_days=0):
    date = datetime.date.today() + datetime.timedelta(days=offset_days)
    return f"{base_text} - {date}"
