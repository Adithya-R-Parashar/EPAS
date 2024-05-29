

def start_sequence(check_in, check_out, error_rate, submission_status):
		expected_time = "10.00"
		actual_time = check_in
		time_score_checkin = time_difference_checkin(expected_time, actual_time)
		expected_time = "9.30"
		actual_time = check_out
		time_score_checkout = time_difference_checkout(expected_time, actual_time)
		timeliness_score = avg_time_score(time_score_checkin, time_score_checkout)
		rating = calculate_rating(timeliness_score, error_rate, submission_status)
		return rating

def time_difference_checkin(expected_time, actual_time):
    # Split the time strings into hours and minutes
    expected_hours, expected_minutes = map(int, expected_time.split('.'))
    actual_hours, actual_minutes = map(int, actual_time.split('.'))

    # Calculate the total minutes for expected and actual times
    expected_total_minutes = expected_hours * 60 + expected_minutes
    actual_total_minutes = actual_hours * 60 + actual_minutes

    # Calculate the difference in minutes
    difference_minutes = actual_total_minutes - expected_total_minutes

    # Convert the difference to hours and remaining minutes
    time_diff = difference_minutes / 60

    if difference_minutes < 0:
        # Actual time is before the expected time (early arrival)
        time_score_checkin = 1 + time_diff
    else:
        # Actual time is after the expected time (late arrival)
        time_score_checkin = 1 - abs(time_diff)

    # Cap the time score between 0 and 1
    time_score_checkin = max(0, min(1, time_score_checkin))

    return time_score_checkin


def time_difference_checkout(expected_time, actual_time):
    # Split the time strings into hours and minutes
    expected_hours, expected_minutes = map(int, expected_time.split('.'))
    actual_hours, actual_minutes = map(int, actual_time.split('.'))

    # Calculate the total minutes for expected and actual times
    expected_total_minutes = expected_hours * 60 + expected_minutes
    actual_total_minutes = actual_hours * 60 + actual_minutes

    # Calculate the difference in minutes
    difference_minutes = expected_total_minutes - actual_total_minutes

    # Convert the difference to hours and remaining minutes
    time_diff = difference_minutes / 60
    time_score_checkout =  max(0, 1 - abs(time_diff))

    return time_score_checkout

def avg_time_score(time_score_checkin, time_score_checkout):
    timeliness_score = (time_score_checkin + time_score_checkout)/2
    return timeliness_score


def calculate_rating(timeliness_score, error_rate, submission_status):

  timeliness_score_weight = 0.2
  error_weight = 0.2
  submission_weight = 0.2
  error_rates = error_rate/10


  # Invert error rate for better rating with lower errors
  error_rate = 1 - error_rates

  # Assign point values based on submission status
  submission_score = 1 if submission_status == 1 else 0.5

  # Calculate weighted average score
  rating = (timeliness_score_weight * timeliness_score +
            error_weight * error_rate + 
            submission_weight * submission_score)

  # Scale rating to 1-5 range
  rating = rating * 10

  return round(rating, 2)