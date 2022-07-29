# FACts - Deven Maheshwari, Aaron Contreras, Oscar Wang, Owen Yaggy
# Softdev
# P04 - Le Fin
# 2022-06-10

# Source: https://dev.socrata.com/foundry/data.cityofnewyork.us/qmc5-z72r
#!/usr/bin/env python 

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None' in place of application token, and no username or password:
client = Socrata("data.cityofnewyork.us", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.cityofnewyork.us,
#                  MyAppToken,
#                  userame="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of dictionaries by sodapy.
results = client.get("qmc5-z72r", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)