import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime as dt
import random


# -------------------------------------------- SENDING EMAILS -------------------------------------------------------- #

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=test_email, password=test_password)
#     connection.sendmail(
#         from_addr=test_email,
#         to_addrs=my_email,
#         msg="Subject:Hello\n\n"
#             "This is an automatic email send with Python code, and it's really cool"
#     )

# -------------------------------------------- SENDING EMAILS WITH EMOJIS -------------------------------------------- #
# subject = "Day 32"
# body = "smtplib is a cool library"

# Encoding to handle emojis
# msg = MIMEText(body, 'plain', 'utf-8')
# msg['Subject'] = Header(subject, 'utf-8')
# msg['From'] = test_email
# msg['To'] = my_email


# with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=test_email, password=test_password)
#     connection.sendmail(test_email, [my_email], msg.as_string())


# Angela lesson
# connection.sendmail(
#     from_addr=test_email,
#     to_addrs="my_email",
#     msg="Subject:Hello\n\n"
#         "This email was sent with Python"
# )

# ------------------------------------------------- DATE-TIME MODULE ------------------------------------------------- #

# Get datetime object
now = dt.datetime.now()

# Get current weekday
day_of_week = now.weekday()

# Get random line from text file
with open("quotes.txt") as file:
    random_quote = random.choice(file.readlines())

# Send email if day == today
if day_of_week == 0:
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=test_email, password=test_password)
        connection.sendmail(
            from_addr=test_email,
            to_addrs=my_email,
            msg="Subject:Your daily Motivation\n\n"
                f"{random_quote}"
        )

