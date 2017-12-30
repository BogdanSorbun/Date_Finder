days = ['wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday', 'tuesday']
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# day 1 started on a monday

def num_of_leap(year):
    leap_years = int(year/4)
    return leap_years
        

def date(year, month, day):
    months = sum(days_in_month[:month])
    total_days = (year*365) + num_of_leap(year) + day + months
    cycle_of_days = total_days % len(days)
    print(days[cycle_of_days].capitalize())
    
