## Assignment #1 - SQL and NoSQL Distrubuted Databases

Please submit the code and answers to me in a Google Doc, email, or an alternative method is also ok. I'd prefer for you to answer these questions using [Google BigQuery (free Sandbox version)](https://console.cloud.google.com/bigquery). If that doesn't work, then you can use SparkSQL within [Google Colab Notebooks](https://colab.sandbox.google.com). Here's my [starter Colab notebook](https://github.com/zaratsian/iaa_2020/blob/master/session_02/pyspark_sql.ipynb) to get you up and running. If for some reason those methods do not work, then you may use a different approach but please specify your approach as part of your respone. 

Use the Austin Bike sharing data to answer the following questions. There are two ways to access the data:

**Option #1 to Access the Data**: Download the files from here [bikesharing_trips.csv](https://raw.githubusercontent.com/zaratsian/iaa_2020/master/data/bikeshare_trips.csv) and [bikesharing_stations.csv](https://raw.githubusercontent.com/zaratsian/iaa_2020/master/data/bikeshare_stations.csv)

**Option #2 to Access the Data**: You can query the data directly in [Google Cloud BigQuery](https://console.cloud.google.com/bigquery) using a syntax such as this:

```
SELECT * FROM `bigquery-public-data.austin_bikeshare.bikeshare_stations` LIMIT 1000
```

-----------------


## **Questions:**

1. Which bike station in Austin is the most popular when starting a trip?


2. Which routes (start to end point) are the most popular. Please list the top 5. A route is a defined as a (start_station_name, end_station_name).


3. Which stations are the furthest distance apart? Hint: I'd calculated the distance in meters based on the longitue and latitute of the start and end points ([reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions))


-----------------
