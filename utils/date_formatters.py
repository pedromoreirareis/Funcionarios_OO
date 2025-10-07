from datetime import datetime


def str_to_date(date_str):

    return datetime.strptime(date_str, "%d/%m/%Y")


def date_to_str(date_timestamp):

    return datetime.strftime(date_timestamp, "%d/%m/%Y")


def today_str():
    return datetime.today().strftime("%d/%m/%Y")
