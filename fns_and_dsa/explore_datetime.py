from datetime  import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_datetime.strf("%y-%m-%d %H:%M:%S")
    print(formatted_date)
def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = timedelta(days=number_of_days)
    return future_date
     
    