from Tools.datetime_utils import get_time, get_date, get_date_time

class DateTimeCommand:

    def execute(self, text):

        text = text.lower()

        if "date" in text and "time" in text:
            return get_date_time()

        elif "time" in text:
            return get_time()

        else:
            return get_date()