from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "your@email.here"
MY_PASSWORD = "password"
SMTP = "smtp.gmail.com"
#SMTPs = Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

today = datetime.now()
today_tupple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tupple in birthdays_dict:
    birthday_person = birthdays_dict[today_tupple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(birthday_person["name"])

    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )


