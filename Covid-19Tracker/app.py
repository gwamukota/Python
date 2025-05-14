# COVID-19 Global Trends Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Data Collection & Loading
# data from Our World in Data (or use the provided file)
# owid-covid-data.csv

# Load the data
df = pd.read_csv('owid-covid-data.csv')

# 2. Data Exploration
# View first few rows to understand the structure
print("First 5 rows of the dataset:")
df.head()

# Check basic information about the dataset
print("\nBasic information about the dataset:")
df.info()

# 3. Data Cleaning
# Convert date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Select relevant columns for our analysis
columns_to_use = ['date', 'location', 'total_cases', 'new_cases', 
                  'total_deaths', 'new_deaths', 'total_vaccinations', 
                  'people_vaccinated', 'population']
covid_data = df[columns_to_use]

# Filter for a few specific countries (easy to visualize)
countries_of_interest = ['United States', 'India', 'United Kingdom', 'Brazil', 'Kenya']
filtered_data = covid_data[covid_data['location'].isin(countries_of_interest)]

# 4. Data Analysis & Visualization

# 4.1 Total Cases Over Time
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4.2 Daily New Cases
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    # Use 7-day rolling average to smooth the data
    plt.plot(country_data['date'], 
             country_data['new_cases'].rolling(window=7).mean(), 
             label=country)

plt.title('Daily New COVID-19 Cases (7-day rolling average)')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4.3 Total Deaths Over Time
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)

plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4.4 Vaccination Progress
plt.figure(figsize=(10, 6))
for country in countries_of_interest:
    country_data = filtered_data[filtered_data['location'] == country]
    # Calculate vaccination percentage
    country_data['vaccination_percentage'] = (country_data['people_vaccinated'] / 
                                              country_data['population']) * 100
    plt.plot(country_data['date'], country_data['vaccination_percentage'], label=country)

plt.title('COVID-19 Vaccination Progress (% of Population)')
plt.xlabel('Date')
plt.ylabel('Percentage Vaccinated')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Calculate Key Metrics (latest available data)
# Get the latest date for each country
latest_data = filtered_data.sort_values('date').groupby('location').last().reset_index()

# Calculate death rate (deaths per case)
latest_data['death_rate'] = (latest_data['total_deaths'] / latest_data['total_cases']) * 100

# Display summary table
summary_table = latest_data[['location', 'total_cases', 'total_deaths', 'death_rate', 'people_vaccinated']]
summary_table = summary_table.sort_values('total_cases', ascending=False)
summary_table

# 6. Create a bar chart comparing total cases
plt.figure(figsize=(10, 6))
sns.barplot(x='location', y='total_cases', data=summary_table)
plt.title('Total COVID-19 Cases by Country')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 7. Summary Insights
print("Key COVID-19 Insights:")
print("---------------------")

# Country with highest cases
max_cases_country = summary_table.loc[summary_table['total_cases'].idxmax()]
print(f"1. {max_cases_country['location']} has the highest number of cases with {max_cases_country['total_cases']:,.0f} confirmed infections.")

# Country with highest death rate
max_death_rate_country = summary_table.loc[summary_table['death_rate'].idxmax()]
print(f"2. {max_death_rate_country['location']} has the highest death rate at {max_death_rate_country['death_rate']:.2f}%.")

# Country with highest vaccination rate
if 'people_vaccinated' in summary_table.columns and not summary_table['people_vaccinated'].isna().all():
    summary_table['vaccination_rate'] = (summary_table['people_vaccinated'] / summary_table['population']) * 100
    max_vax_country = summary_table.loc[summary_table['vaccination_rate'].idxmax()]
    print(f"3. {max_vax_country['location']} has the highest vaccination rate at {max_vax_country['vaccination_rate']:.2f}%.")