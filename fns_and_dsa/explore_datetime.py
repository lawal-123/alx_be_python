from datetime module  import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strf("%Y-%m-%d %H:%M:%S")
    return formatted_date
def calculate_future_date():
    days = int(input("enter number of days: "))
    future_date = timedelta(days=number_of_days)
    formatted_future_date = future_date.strf("%y-%m-%d")
    return formattted_future_date
