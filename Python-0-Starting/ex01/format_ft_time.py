import datetime
import time

epoch_now = time.time()
date_now = datetime.datetime.now()

print(f"Seconds since January 1, 1970: {epoch_now:,.4f} or {epoch_now:.2e} in scientific notion")
print(date_now.strftime("%b %d %Y"))
