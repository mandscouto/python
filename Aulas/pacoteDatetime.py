import datetime
hoje = datetime.datetime.today().date()
print(hoje)
print(type(hoje))

rio = datetime.date(2025, 11, 18)
print(rio - hoje)