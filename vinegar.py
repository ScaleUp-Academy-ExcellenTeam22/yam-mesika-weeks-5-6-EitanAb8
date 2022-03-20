import datetime
import random


def i_dont_have_vinegar(start_time, end_time):
    # This program receives 2 date objects.
    # prints "i don't have vinegar if a random date between
    # the 2 of them is monday.

    start_date = start_time
    end_date = end_time

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    if random_date.weekday() == 0:
        print("I don't have vinegar")


def main():
    start_time = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 2, 1)
    i_dont_have_vinegar(start_time, end_date)


if __name__ == '__main__':
    main()
