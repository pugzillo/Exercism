from datetime import datetime, timedelta

def add_gigasecond(moment):
    gigasec = timedelta(seconds = 1000000000)
    date2 = moment + gigasec
    return(date2)
