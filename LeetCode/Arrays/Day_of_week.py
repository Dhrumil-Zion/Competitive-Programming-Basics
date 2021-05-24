from datetime import date

def dayOfTheWeek(day, month, year):
    return date(year,month ,day).strftime("%A")