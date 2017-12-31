days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# day 1 started on a saturday

def num_of_leap(year):
    leap_years = int(year/4)-(int(year/100) - int(year/400))
    return leap_years
        

def date(year, month, day):
    months = sum(days_in_month[:(month)])
    total_days = ((year)*365) + num_of_leap(year) + day + months
    if month == 2 and day == 29:
        total_days = total_days - 1
    cycle_of_days = total_days % len(days)
    print(days[cycle_of_days].capitalize())
    
