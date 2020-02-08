"""
This file will be responsible for housing the functions that pull and clean the data
"""
# DEPENDENCIES
import pandas as pd
import numpy as np
import sqlite3


# Query the DB and select a random 100k rows.
# export it to CSV

try:
    # import the data from csv
    data = pd.read_csv('reddit_user_subreddit.csv')
    
except:
    # import and run the sql query
    connection = sqlite3.connect('reddit_data.db')
    
    data = pd.read_sql_query(
        """
        SELECT O.username_id, O.subreddit_id, COUNT(O.utc) AS visits
            FROM
                Observation O
            GROUP BY O.username_id, O.subreddit_id
            ORDER BY RANDOM()
            LIMIT 100000;
        """,
        connection
        )

    data.to_csv('reddit_user_subreddit.csv')


# Query the DB and build our mapper
try: 
    # a second table to map the subreddit_id to the subreddit name, to be accessed after our recommender
    mapper_df = pd.read_csv('subreddit_mapper.csv')
    
except:
    connection = sqlite3.connect('reddit_data.db')
    mapper_df = pd.read_sql_query(
        """
        SELECT S.subreddit_id, S.subreddit FROM Subreddit S;
        """, connection)
    
    mapper_df.to_csv('subreddit_mapper.csv')

df2 = data.join(mapper_df, on = 'subreddit_id', lsuffix = '_original', rsuffix = '_mapper')
sr_map = df2[['subreddit_id_mapper', 'subreddit']]
# sr_map.drop_duplicates(subset = 'subreddit_id_mapper', inplace = True) # obtain unique values of subreddits
sr_map.drop_duplicates(subset = 'subreddit', inplace = True) # obtain unique values of subreddits
sr_map = sr_map.astype(str)

# Ramon's mapper - need to turn this into a function to build the mapper automatically
# this mapper will include all subreddits from the original db, not just from our 100k rows
# dict_subreddits = mapper_df['subreddit_id'] # create a Series of IDs from the df
# dict_subreddits.index = mapper_df['subreddit'] # Set the index of that Series as the Subreddit names
# dict_subreddits = dict_subreddits.to_dict() # turn that into a dict
# sr_map = {v: k.lower() for k, v in dict_subreddits.items()} # reverse the key-value 

# print(sr_map[ sr_map['subreddit_id_mapper'] == 24749]) # print a specific key's value
# print(sr_map.head())