**##Tidy Data Project: 2008 Olympic Medalists**

**#Project Overview**

For this project, I used a dataset containing information about medalists from the 2008 Summer Olympics.
The goal was to practice cleaning, reshaping, and analyzing data using Python and pandas while following tidy data principles.


**#Dataset Information:**

The dataset used in this project is 2008_medalists_all.csv, which contains information about medalists from the 2008 Summer Olympics.


The original dataset contained 46 columns. For my analysis, I selected five variables:
medalist_name: Name of the Olympic medalist
country_medal: Country represented by the medalist
sport: Sport in which the medalist competed
event_name: Name of the Olympic event
medal: Type of medal received (gold, silver, or bronze)

I checked for missing values using isnull().sum() and found no missing values in the five selected columns. 
I also used str.replace() to shorten event names and drop_duplicates() to remove duplicate records.

**#Data Analysis: **

I used several pandas functions throughout the project:

pd.read_csv() to load the dataset.
head(), shape, and info() to explore the data.
isnull().sum() to check for missing values.
drop_duplicates() to remove duplicate records.
str.replace() to clean event names.
pd.melt() to practice reshaping data.
str.split() to practice separating text into columns.
pd.pivot_table() with aggfunc="count" to summarize medalist records by country and medal type.


**Visualizations: **

I created three visualizations using pandas and Matplotlib:

Olympic Medal Distribution: A bar chart comparing gold, silver, and bronze medalist records.
Medalist Records by Sport: A bar chart comparing the number of medalist records across Olympic sports.
Top Five Countries by Medalist Records: A pie chart showing the distribution of records among the five countries with the highest counts.

**#Instructions: **

1. Download the TidyData-Project folder from GitHub.
2. Make sure Python and Jupyter Notebook are installed.
4. pip install pandas matplotlib notebook
5. Open the Jupyter Notebook file in the project folder.
6. Make sure 2008_medalists_all.csv is in the same folder as the notebook.
7. Run the notebook cells to view the data cleaning steps, pivot table, and visualizations.

**#References:**

1. [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
2. Course notebooks: Week 5.1 and Week 5.2
3. Dataset: 2008_medalists_all.csv

