import pandas as pd
import requests

# List of countries (ISO 3166-1 alpha-3 codes) and the time range
countries = ['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'FRA', 'BRA', 'ITA', 'CAN', 
             'RUS', 'KOR', 'AUS', 'ESP', 'MEX', 'IDN', 'NLD', 'SAU', 'TUR', 'CHE']
years = list(range(1900, 2025))

# Function to fetch GDP data from the World Bank API for a given country code
def fetch_gdp_data(country_code):
    # API endpoint for GDP data
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json&per_page=500"
    response = requests.get(url)
    
    # Check if the API request was successful
    if response.status_code != 200:
        raise Exception(f"API request failed for {country_code}")
    
    # Parse the JSON response
    data = response.json()[1]
    
    # Return a dictionary of year-value pairs for GDP data
    return {item['date']: item['value'] for item in data if item['value'] is not None}

# Initialize an empty DataFrame with years as index and countries as columns
gdp_data = pd.DataFrame(index=years, columns=countries)

# Loop through each country to fetch and store its GDP data
for country in countries:
    print(f"Fetching data for {country}")
    gdp_dict = fetch_gdp_data(country)
    
    # Populate the DataFrame with the fetched data
    for year in years:
        gdp_data.at[year, country] = gdp_dict.get(str(year), None)

# Save the DataFrame to a CSV file
gdp_data.to_csv('historical_gdp_data.csv')

print("Data fetching complete. Saved to 'historical_gdp_data.csv'.")
