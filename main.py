##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib
import os

################ nacitanie suboru
df = pandas.read_csv("birthdays.csv")
#my_dict = df.to_dict() #(orient="records")
my_dict = df.to_dict(orient="records")

print(my_dict)
################ dnesok

now = dt.datetime.now()
today = now.date()
print(now.day)
print(now.month)

birthday_record = [item for item in my_dict if item["day"]==now.day if item["month"]==now.month]
print(birthday_record)
print(type(birthday_record))
#print(birthday_record[0]["name"])


print(bool(birthday_record))


letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
selected_letter = random.choice(letters)

selected_letter_path = f'./letter_templates/{selected_letter}'

with open(selected_letter_path,"r") as letter_txt:
    letter_content = letter_txt.read()

letter_content = letter_content.replace('[NAME]',birthday_record[0]['name'])

my_email = "samko@centrum.sk"
my_password = "OkreSLevicE"

with smtplib.SMTP("smtp.centrum.sk") as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=birthday_record[0]['email'],
                        msg=f'Subject:Happy Birthday\n\n{letter_content}'
                        )



# #print(df[df["email"]=="test@emaxil.com"])
#print(my_dict)
#print(type(my_dict))
#
#print(list(item for item in my_dict if item["email"]=="test@email.com"))
#print(my_dict[0]["email"])

# result = [item for item in my_dict if item["email"] == "test@email.com"]
# print(result)
# print([item for item in my_dict if item["email"] == "test@email.com"])
# print(my_dict[0])

# for key, value in dict.values():
#     if value==8:
#         print(dict[0])

#result = [key for key, value in my_dict.items() if value == 93]


