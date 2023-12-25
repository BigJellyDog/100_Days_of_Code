def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(years, month_count):

    """Remove 1 from the month count to adjust to the list month_days"""
    month_count -= 1
    """All months in year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    """Checking if years is a leap or not"""
    if not is_leap(years):
        """If not leap year, we return the month_days without changes"""
        return month_days[month_count]
    else:
        "If leap year, we return the months by adding +1 to February bcs leap year has 29 days"
        month_days[1] = 29
        """Return the modified list+the user input"""
        return month_days[month_count]


year = 2020  # Enter a year
month = 2  # Enter a month
days = days_in_month(year, month)
print(days)

