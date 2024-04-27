'''
Python Script to calculate the number of countries and
total population for each region.
'''
import json
from db import Region, Country

def calculate_region_stats():
    '''
    @Description: Calculate the number of countries and total population for each region
    '''
    regions = []

    # Iterate through all regions
    for region_obj in Region.list_all():
        region_name = region_obj.data["name"]
        number_countries = 0
        total_population = 0

        # Iterate through all countries
        for country_obj in Country.list_all():
            if country_obj.data["region_name"] == region_name:
                number_countries += 1
                total_population += country_obj.data["population"]

        # Create a dictionary with the region stats
        region_stats = {
            "name": region_name,
            "number_countries": number_countries,
            "total_population": total_population
        }

        # Append the region stats to the list of regions
        regions.append(region_stats)

    return {"regions": regions}


if __name__ == "__main__":
    stats = calculate_region_stats()

    # Print the stats in a pretty format
    print(json.dumps(stats, indent=4))
