import datetime

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def time_until_next_birthday(birth_date):
    today = datetime.date.today()
    next_birthday = birth_date.replace(year=today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    time_until = next_birthday - today
    return time_until

def double_day(b1, b2):
    delta = abs(b2 - b1)
    double = max(b1 + delta, b2 + delta)
    return double

def n_times_older_day(b1, b2, n):
    delta = abs(b2 - b1)
    older_day = max(b1 + delta, b2 + delta * n)
    return older_day

# Get the current date
current_date = datetime.datetime.now()

# Print the day of the week
print("Current day of the week:", current_date.strftime("%A"))

# Input birthday from the user
year = int(input("Enter the birth year: "))
month = int(input("Enter the birth month: "))
day = int(input("Enter the birth day: "))
birthday = datetime.date(year, month, day)

# Calculate age
age = calculate_age(birthday)
print("Age:", age)

# Calculate time until next birthday
time_until_birthday = time_until_next_birthday(birthday)
print("Time until next birthday:", time_until_birthday)

# Input birthdays from the user
year1 = int(input("Enter the year of the first person's birth: "))
month1 = int(input("Enter the month of the first person's birth: "))
day1 = int(input("Enter the day of the first person's birth: "))
birthday1 = datetime.date(year1, month1, day1)

year2 = int(input("Enter the year of the second person's birth: "))
month2 = int(input("Enter the month of the second person's birth: "))
day2 = int(input("Enter the day of the second person's birth: "))
birthday2 = datetime.date(year2, month2, day2)

# Find Double Day
dd = double_day(birthday1, birthday2)
print("Double Day:", dd)

# Input N from the user
n = int(input("Enter the value of N: "))

# Find N Times Older Day
older_day = n_times_older_day(birthday1, birthday2, n)
print(f"Day when one person is {n} times older than the other:", older_day)
