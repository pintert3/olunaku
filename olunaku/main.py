import datetime

leero = datetime.date.today()
print(f'Leero {leero}')
OFFSET = datetime.timedelta(hours=-3)
BUG = datetime.timezone(OFFSET, "Buganda")

check = datetime.datetime.now().astimezone(BUG)
