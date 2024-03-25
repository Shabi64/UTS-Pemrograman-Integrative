import datetime

today = datetime.date.today()

days_this_year = (today - datetime.date(today.year, 1, 1)).days + 1

whole_number = int(input("Masukkan angka: "))

result = whole_number / days_this_year

print("Hasil pembagian:", format(result, '.11f'))
