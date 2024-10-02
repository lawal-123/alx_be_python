from datetime module  import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strf("%Y-%m-%d %H:%M:%S")
    return formatted_date
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days)
  formatted_date = future_date.strftime("%y-%m-%d")
    return future_date
