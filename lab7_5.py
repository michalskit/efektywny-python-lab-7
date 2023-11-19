import json
from datetime import datetime
import pytz

# Wykorzystując countries.json podaj aktualną godzinę we
# wszystkich krajach, wyświetlając je zgrupowane względem kontynentów


# Open JSON
with open('countries.json') as file:
    countries = json.load(file)

def get_current_time_in_countries(countries):
    """
    Get the current time in each country, grouped by continent.
    """
    pass

# Get the current time in each country grouped by continent
current_times = get_current_time_in_countries(countries)

# Display the result
for continent, times in current_times.items():
    print(f"Continent: {continent}")
    for country, time in times.items():
        print(f"  {country}: {time}")
    print("\n")
