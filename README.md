
# Historical GDP Data Fetcher

This repository contains a Python script to fetch historical GDP data for multiple countries from 1900 to 2024 using the World Bank API. The script retrieves GDP data, organizes it into a Pandas DataFrame, and saves it as a CSV file.

## Features

- Fetches GDP data for 20 countries from the World Bank API
- Covers the time period from 1900 to 2024
- Saves the data into a CSV file for further analysis

## Prerequisites

Ensure you have the following libraries installed:

- `pandas`
- `requests`

You can install these libraries using pip:

```bash
pip install pandas requests
```

## Usage

### Clone the Repository:

```bash
git clone https://github.com/yourusername/historical-gdp-fetcher.git
cd historical-gdp-fetcher
```

### Run the Script:

Execute the Python script to fetch the data and save it to a CSV file:

```bash
python fetch_gdp.py
```

### Output:

The script will create a CSV file named `historical_gdp_data.csv` in the repository directory.

### fetch_gdp.py


## Script Details

The script performs the following steps:

1. Defines a list of countries using their ISO 3166-1 alpha-3 codes and a range of years.
2. Contains a function `fetch_gdp_data` that fetches GDP data from the World Bank API for a given country.
3. Initializes an empty DataFrame to store the GDP data.
4. Loops through each country, fetches its GDP data, and populates the DataFrame.
5. Saves the DataFrame to a CSV file.

### Example

Below is a sample snippet of how the data will look in the CSV file:

| Year | USA         | CHN         | JPN         | DEU         | IND         | GBR         | ... |
|------|-------------|-------------|-------------|-------------|-------------|-------------|-----|
| 1900 | 553.25B     | 610.32B     | 362.05B     | 168.93B     | 317.27B     | 890.89B     | ... |
| 1901 | 718.04B     | 290.01B     | 941.02B     | 798.42B     | 379.30B     | 766.91B     | ... |
| ...  | ...         | ...         | ...         | ...         | ...         | ...         | ... |
| 2024 | 22.68T      | 16.32T      | 5.38T       | 4.44T       | 3.20T       | 3.32T       | ... |

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [World Bank API](https://data.worldbank.org/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Requests Documentation](https://requests.readthedocs.io/en/master/)
