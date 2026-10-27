Tidy Data Project: 2008 Olympic Medalists

Project Overview

For this project, I used a dataset containing information about medalists from the 2008 Summer Olympics.
The goal was to practice cleaning, reshaping, and analyzing data using Python and pandas while following tidy data principles.


Dataset Information: 

The dataset used in this project is 2008_medalists_all.csv, which contains information about medalists from the 2008 Summer Olympics.


The original dataset contained 46 columns. For my analysis, I selected five variables:
medalist_name: Name of the Olympic medalist
country_medal: Country represented by the medalist
sport: Sport in which the medalist competed
event_name: Name of the Olympic event
medal: Type of medal received (gold, silver, or bronze)

I checked for missing values using isnull().sum() and found no missing values in the five selected columns. 
I also used str.replace() to shorten event names and drop_duplicates() to remove duplicate records.

Data Analysis: 

I used several pandas functions throughout the project:

pd.read_csv() to load the dataset.
head(), shape, and info() to explore the data.
isnull().sum() to check for missing values.
drop_duplicates() to remove duplicate records.
str.replace() to clean event names.
pd.melt() to practice reshaping data.
str.split() to practice separating text into columns.
pd.pivot_table() with aggfunc="count" to summarize medalist records by country and medal type.


Visualizations: 

I created three visualizations using pandas and Matplotlib:

Olympic Medal Distribution: A bar chart comparing gold, silver, and bronze medalist records.
Medalist Records by Sport: A bar chart comparing the number of medalist records across Olympic sports.
Top Five Countries by Medalist Records: A pie chart showing the distribution of records among the five countries with the highest counts.
