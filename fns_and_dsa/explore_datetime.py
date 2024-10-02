from datetime module  import datetime, timedelta
def explore_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strf("%Y-%m-%d %H:%M:%S")
    return formatted_date
def calculate future_date():
    days = int(input("enter number of days: "))
