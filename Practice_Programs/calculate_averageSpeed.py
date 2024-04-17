
# "If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their
# average speed traveled was 30mph.
# Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate.
# Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.
# Examples
# ave_spd(18, 20, 60) ➞ 30
# ave_spd(30, 10, 30) ➞ 15
# ave_spd(30, 8, 24) ➞ 12"

def calculate_avg_speed(uphill_time, uphill_speed, downhill_speed):
    uphill_distance = uphill_speed*(uphill_time/60)
    downhill_time = (uphill_distance/downhill_speed)*60
    total_distance = uphill_distance*2
    total_time_taken = (uphill_time+downhill_time)/60
    average_speed = total_distance/total_time_taken
    return average_speed


if __name__ == "__main__":
    time_taken = int(input("Enter the Time taken in minutes for going uphill:"))
    upstream_speed = int(input("Enter the Uphill speed in mph:"))
    downstream_speed = int(input("Enter the Downhill speed in mph:"))
    print(calculate_avg_speed(time_taken, upstream_speed, downstream_speed))
