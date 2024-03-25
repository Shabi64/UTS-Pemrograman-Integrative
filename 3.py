import datetime

days = int(input("Masukkan angka: "))

current_date = datetime.date.today()

future_date = current_date + datetime.timedelta(days=days)

formatted_date = future_date.strftime("%A on %d %B %Y")

print(formatted_date)