import datetime

now = datetime.date.today()
five_days_back = now + datetime.timedelta(days=-5)

print(f"Now: \t {now}")
print(f"Five: \t {five_days_back}")