##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import smtplib

EMAIL = ""
PASSWORD = ""
MY_MAIL = ""

# Getting dates from the birthday csv file
dates = pd.read_csv("birthdays.csv")

# Getting today dates with the datetime module
today_day = dt.date.today().day
today_month = dt.date.today().month
today_year = dt.date.today().year


# Checking if there is someone's birthday today and getting the name else returning NO
birthday_today = dates[(dates['month'] == today_month) & (dates['day'] == today_day)]
name = birthday_today['name'].iloc[0] if not birthday_today.empty else "NO"
year = birthday_today['year'].iloc[0] if not birthday_today.empty else 0
years_old = today_year - year

# If there is a name there is a birthday!!!
if name != "NO":

    with open(file="letter_templates/text.txt") as file:
        text = file.read()
        text = text.replace("[NAME]", f"{name}")
        text = text.replace("[YEARS]", f"{years_old}")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=MY_MAIL,
            msg=f"Subject:Happy Birthday {name}!!!\n\n"
                f"{text}"
        )
