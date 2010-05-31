'''
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import date

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
def is_leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def acc(items):
    s = 0
    accumulated = []
    for i in items:
        s += i
        accumulated += [s]
    return accumulated

def days_in_months(year):
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        days_list[1] += 1
    return days_list
     
    

def solve(rng, start_day):
    day = start_day
    num_sundays = 0
    for y in rng:
        m = 1
        for days in days_in_months(y):
            if (day % 7) == 6:
                assert date(y, m, 1).weekday() == 6
                num_sundays += 1
            day += days
            m+=1
    
    print("Number of sundays on the first of the month is %(num_sundays)d" % vars())

if __name__ == "__main__":
    # Jan 1 1901 is a tuesday
    solve(range(1901, 2001), 1)
