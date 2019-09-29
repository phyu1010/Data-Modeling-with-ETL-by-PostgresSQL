# Data-Modeling-with-ETL-by-PostgresSQL

# Description 
In this project, I applid the knowledge on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, I need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Dataset

## Song dataset

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. 

## Log dataset

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.The log files in the dataset you'll be working with are partitioned by year and month. 

## Data Modeling
Created a STAR schema, optimized for song play analysis.
* **Fact Table**: songplays: attributes referencing to the dimension tables.
* **Dimension Tables**: users, songs, artists and time table. 

This database will help the internal departments of the Sparkify company to do different kinds of analysis to recommend a Sparkify user. 

* Favorite songs of user based on the week day: By joining songplay and songs and user table based on level. 
* Recent listened to songs: By joining songplays and user table can show recommendation on the app based on subscription level. 
* Can help in recommending most popular songs of the day/week.

## ETL
1. Created **songs**, **artist** dimension tables from extracting songs_data by selected columns.
2. Created **users**, **time** dimension tables from extracting log_data by selected columns.
3. Created the most important table fact table from the dimensison tables and log_data called **songplays**. 

