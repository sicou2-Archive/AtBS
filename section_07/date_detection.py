import re
import datetime

text = 'Howdy! Today is 18/06/2020'

class DateValidator:

    def __init__(self, text):
        self.text = text
        months_dict = {
            '28': ['02'],
            '29': ['02'],
            '30': ['04', '06', '09', '11'],
            '31': ['01', '03', '05', '07', '08', '10', '12']
        }

    def date_regex(self):
        print(text)

        date_regex = re.compile(
            r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([1-2][0-9]{3})')
        # TODO: regex to detect dates DD/MM/YYYY
        # Days 01-31 Months 01-12 Years 1000-2999 No single digit DD or MM
        mo = date_regex.search(self.text)

        month, day, year = mo.group(1), mo.group(2), mo.group(3)
        return f'{month}-{day}-{year}'

    # regex not account for leap years or correct days

    # TODO: store DD MM YYYY as variables month, day, year

    # TODO: Detect if valid date.
    # 28 - Feb; 30 - Apr June Sep Nov; 31 - Jan Mar May Jul Aug Oct Dec
    # Leap yrs / by 4 except when / by 100 , but includes 400 (ie 400 is LY)

    # Leap year check

    def leap_year(year, leap):
        year_int = int(year)
        if (year_int % 400) == 0:
            leap = 1
        elif (year_int % 100) == 0:
            leap = 0
        elif (year_int % 4) == 0:
            leap = 1
        else:
            leap = 0


vd = DateValidator(text)
date = vd.date_regex()
print(datetime.datetime.strptime(date, '%d-%m-%Y'))
