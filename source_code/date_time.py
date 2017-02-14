# Roybal, Monte 2-13-2017
# Homework 2
# I am implementing a simple source code utilizing the DateTime module and pytz module.

from datetime import datetime
import pytz

N_Y_C = pytz.timezone('US/Eastern')

date = datetime.now(pytz.utc)
date = N_Y_C.normalize(date.astimezone(N_Y_C))

print "The current time and date in New York City is ", date



