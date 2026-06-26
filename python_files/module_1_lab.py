
# 3.1 How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60)
# by the number of minutes in an hour (also 60).
print(60 * 60)

# 3.2 Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.
seconds_per_hour = 60 * 60
# print(f"Seconds per hour: {seconds_per_hour}")

# 3.3 How many seconds are in a day? Use your seconds_per_hour variable.
print(60 * 60 * 24)

# 3.4 Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.
seconds_per_day = 60 * 60 * 24

# 3.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.
print(seconds_per_hour / seconds_per_day)

# 3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division. 
print(seconds_per_hour // seconds_per_day)

# Did this number agree with the floating-point value from the previous question, aside from the final .0?
# I don't think it does, it seems to be 0 while the result form the floating-point was a very large decimal, 0.041666666666666664