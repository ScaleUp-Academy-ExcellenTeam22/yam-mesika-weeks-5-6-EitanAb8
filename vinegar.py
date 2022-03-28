import datetime
import random

# Note: I studied the solution from the following link site:
# https://www.adamsmith.haus/python/answers/how-to-generate-a-random-date-between-two-dates-in-python


def day_for_vinegar(start_date, end_date):
    """
    The function prints "I don't have vinegar" if a random generated date is monday.
    :param start_date: datetime object of the start date.
    :param end_date: datetime object of the end date.
    :return: None
    """
    random_date = generate_random_date(start_date, end_date)

    if random_date.weekday() == 0:
        print("I don't have vinegar.")


def generate_random_date(start_date, end_date) -> datetime:
    """
    The function generates a random date between two given dates.
    :param start_date: datetime object of the start date.
    :param end_date: datetime object of the end date.
    :return: datetime object of a random date.
    """
    return start_date + datetime.timedelta(days=random.randrange((end_date - start_date).days))


def main():
    start_time = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 2, 1)
    day_for_vinegar(start_time, end_date)


if __name__ == '__main__':
    main()