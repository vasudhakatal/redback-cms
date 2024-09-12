import garminconnect
from getpass import getpass
import os
from datetime import date, timedelta

email = getpass("Enter email address: ")
password = getpass("Enter Password: ")

garmin = garminconnect.Garmin(email, password)
garmin.login()
#need an account to login to.
print(garmin.display_name)

GARTH_HOME = os.getenv("GARTH_HOME", "~/.garth")
garmin.garth.dump(GARTH_HOME)

today = date.today() - timedelta(days=1)
today = today.isoformat()

lastrun = garmin.get_last_activity()['splitSummaries'][0]
stats = garmin.get_max_metrics(today)


vo2max = stats[0]['generic']['vo2MaxPreciseValue']
miles = round(lastrun['distance']/1609.34, 2)
effect = garmin.get_last_activity()['trainingEffectLabel']
duration = round(garmin.get_last_activity()['duration'], 2)

#print(vo2max, miles, effect, duration)
records = garmin.get_personal_record()
print(records)
print(len(records))