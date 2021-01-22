from datetime import date, datetime, timedelta   # don't need time

james_bd = date(2014, 8, 1)
today = date.today()

print(james_bd, today)
print(today.month, today.day, today.year)

diff = today - james_bd
print(diff)
james_age = diff.days / 365.25
print("James age is", round(james_age, 2))

dt = datetime(2020, 7, 1, 13, 47, 52)
print(dt)


