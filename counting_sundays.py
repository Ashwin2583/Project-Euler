# function to check leap year
def is_leap(x):
    return (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)

months_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_weekday = 2 # Jan 1, 1901 was a Tuesday (0=sunday, 1=Monday, ... ,6=saturday)
sundays = 0

for year in range(1901, 2000+1):
    days_in_months = months_leap if is_leap(year) else months_normal

    for days in days_in_months:
        if current_weekday == 0:
            sundays += 1
        current_weekday = (current_weekday + days) % 7

print("Number of sundays fell on the first of the month during the twentienth centuary: ",sundays) 

