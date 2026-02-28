from datetime import datetime

def get_time():
    now = datetime.now()
    return now.strftime("The current time is %I:%M %p.")

def get_date():
    today = datetime.now()
    return today.strftime("Today is %A, %d %B %Y.")

def get_date_time():
    now = datetime.now()
    return now.strftime(
        "Today is %A, %d %B %Y and the time is %I:%M %p."
    )
