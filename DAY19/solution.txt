from datetime import date


def main(period):
    try:
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        today = date.fromisoformat(period)
        wd = date.weekday(today)
        print(days[wd])

    except:

        print("Not a registered date format")


# date format = year-month-day
main('2022-04-25')
