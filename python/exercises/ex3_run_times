
def run_timings():
# Set default values for function
    number_of_runs = 0
    total_time = 0
    total_distance = 0

    while True:
# Get user's run times and distances
        one_time = input('how long did your run take? (just press enter if you\'re done inputing times): ')
        one_length = input('how far, in miles, did you run? (just press enter if you\'re done inputing distances): ')
# Break while loop when user does not enter any more times
        if not one_time :
            break
# Update the number of runs and total time ran
        number_of_runs += 1
        total_distance += float(one_length)
        total_time += float(one_time)

# Calculate the average time per run
    average_run_time = total_time/number_of_runs
    average_distance = total_distance/number_of_runs
    average_pace = total_time/total_distance
    average_run_speed = total_distance/(total_time/60)

    print(f'\nYour average run time was {average_run_time} minutes per run, \nwith an average daily distance ran of {average_distance} mile(s), \nwith an average pace of {average_pace} minutes per mile, \nand an average speed of {average_run_speed} miles per hour')

run_timings()