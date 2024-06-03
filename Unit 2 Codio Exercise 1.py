class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def mul_time(time_obj, number):
    """Multiplies a Time object by a number.
    
    Args:
        time_obj: A Time object with hours, minutes, and seconds attributes.
        number: A number to multiply the time by.
        
    Returns:
        A new Time object containing the product of the original Time and the number.
    """
    total_seconds = time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds
    total_seconds *= number
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    
    return Time(hours, minutes, seconds)

def average_pace(finish_time, distance):
    """Calculates the average pace (time per mile) based on finishing time and distance.
    
    Args:
        finish_time: A Time object representing the finishing time in a race.
        distance: A number representing the distance in miles.
        
    Returns:
        A Time object representing the average pace (time per mile).
    """
    total_seconds = finish_time.hours * 3600 + finish_time.minutes * 60 + finish_time.seconds
    pace_seconds = total_seconds / distance
    
    hours = int(pace_seconds // 3600)
    minutes = int((pace_seconds % 3600) // 60)
    seconds = int(pace_seconds % 60)
    
    return Time(hours, minutes, seconds)

# Define the race time
race_time = Time()
race_time.hours = 3
race_time.minutes = 34
race_time.seconds = 5

# Calculate the average pace for a marathon (26.2 miles)
marathon_distance = 26.2
pace = average_pace(race_time, marathon_distance)

# Print the result
print("Average Pace for the Marathon:", pace.hours, "hours", pace.minutes, "minutes", pace.seconds, "seconds per mile")
